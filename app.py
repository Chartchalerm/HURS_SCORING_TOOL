import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# Path to save scores
data_file = Path("scores.csv")

# Initialize or load existing scores
if not data_file.exists():
    df = pd.DataFrame(columns=["Assessor", "Question", "Key Aspect", "Score", "Comments"])
    df.to_csv(data_file, index=False)
else:
    df = pd.read_csv(data_file)

# Application Title
st.title("Healthy University Rating System (HURS) - Scoring Tool")

# Dictionary of Questions and Key Aspects
questions_data = {
    "SI 1.1 Healthy University Policy Statement": {
        "Key Aspects": {
            "Policy Documents": [
                "Does the policy outline health-related objectives, strategies, and compliance with HUF?",
                "Does the policy highlight organizational commitment at university/faculty levels?",
                "Is the policy approved and reflective of the HUF framework?"
            ],
            "Activities and Programs": [
                "Are health-related programs implemented across faculties and campuses?",
                "Are there examples like workshops or curriculum changes?",
                "Do activities align with HUF and cover faculties proportionally?"
            ],
            "Compliance and Audit Reports": [
                "Are detailed reports available showing percentage of implementation?",
                "Is the data reliable and demonstrates adherence to the framework?",
                "Are there monitoring practices evident in the reports?"
            ],
            "Evidence Integrity": [
                "Is there alignment between claimed implementation and supporting documents?",
                "Is the evidence recent, specific, and relevant?"
            ]
        }
    },
    "SI 1.2 Establishment of Responsible Body": {
        "Key Aspects": {
            "Organizational Charts": [
                "Does the organizational chart show clear recognition of the responsible body at both university and faculty levels?",
                "Is there documentation explicitly identifying the responsible bodies as per HUF?"
            ],
            "Meeting Minutes": [
                "Do meeting minutes illustrate deliberations and decisions regarding health promotion according to HUF?",
                "Are there examples of meetings covering both university-wide and faculty-specific activities?"
            ],
            "Annual Reports": [
                "Do the annual reports detail activities undertaken by the responsible bodies?",
                "Are challenges and achievements explicitly highlighted in line with HUF?",
                "Are reports available for multiple years to demonstrate consistency?"
            ]
        }
    },
    "SI 1.3 Progression of the Responsible Bodies in Conducting Active Implementation of Health Activities": {
        "Key Aspects": {
            "Action Plan Document": [
                "Does the action plan document outline clear objectives, strategies, and intended outcomes?",
                "Is the action plan comprehensive and aligned with the Healthy University Framework (HUF)?"
            ],
            "Implementation Evidence": [
                "Is there evidence of health promotion activities undertaken (e.g., project reports, event photographs)?",
                "Does the evidence show active participation across the university?"
            ],
            "Monitoring and Evaluation Reports": [
                "Are there evaluation reports or review documents demonstrating the assessment of health promotion activities?",
                "Are adjustments made based on evaluations for continuous improvement?"
            ],
            "Impact Assessments": [
                "Are impact assessments or evaluation studies available to measure the effectiveness of health promotion activities?",
                "Do the impact assessments include qualitative and quantitative results?"
            ]
        }
    },
    "SI 2.1 Safety Regulations and Standards for Buildings and Infrastructure": {
        "Key Aspects": {
            "Regulations/Standards Documentation": [
                "Are formal safety regulations and standards documented and available at the university?",
                "Do the safety regulations align with national or international safety standards?"
            ],
            "Active Implementation": [
                "Are safety regulations actively enforced with specific management practices in place?",
                "Are there examples of safety measures such as safety drills, maintenance records, or inspection reports?"
            ],
            "Monitoring and Evaluation": [
                "Are safety management practices regularly monitored and evaluated for compliance?",
                "Are corrective actions taken based on the results of safety audits?"
            ],
            "Incident Reporting": [
                "Is there documented evidence of no safety-related incidents over the last year?",
                "Are incident logs or safety reports maintained and updated regularly?"
            ]
        }
    },
    "SI 2.2 Implementation of Waste Management Systems": {
        "Key Aspects": {
            "Recycling and Separation Bins": [
                "Are there various bins provided to effectively separate recyclable and reusable waste?",
                "Are bins clearly labeled and accessible across the campus?"
            ],
            "Behavioral Change Programs": [
                "Are there programs promoting behavioral changes to reduce landfill waste?",
                "Do these programs include awareness campaigns or workshops?"
            ],
            "Paper and Plastic Minimization": [
                "Is a paper and plastic minimization campaign implemented?",
                "Are there monitoring mechanisms in place to assess the campaign’s effectiveness?"
            ],
            "Hazardous Waste Management": [
                "Is hazardous waste managed in compliance with relevant regulations?",
                "Are there records or reports demonstrating compliance with these regulations?"
            ],
            "Recycling Facilities": [
                "Is there a recycling facility on campus where recycled materials are actively used?",
                "Are examples of recycling initiatives, such as composting, documented and monitored?"
            ],
            "Other Initiatives": [
                "Are there any other specialized waste management initiatives implemented?",
                "Are these initiatives documented with supporting evidence (e.g., policy documents or photographs)?"
            ]
        }
    },
    "SI 2.3 Comprehensive Water Management Systems": {
        "Key Aspects": {
            "Monitoring and Targeted Reductions": [
                "Is water usage monitored, and are targeted reductions established?",
                "Are there records or reports demonstrating water usage tracking and reduction targets?"
            ],
            "Behavioral Change Programs": [
                "Are there programs to promote behavioral changes for water conservation?",
                "Do these programs include awareness campaigns or workshops?"
            ],
            "Water-Saving Devices": [
                "Are water-saving devices installed throughout the campus?",
                "Is there photographic or documentary evidence of installed water-saving devices?"
            ],
            "Leak Analysis and Repairs": [
                "Is infrastructure regularly analyzed to identify and repair leaks?",
                "Are there reports or records documenting leak repairs and infrastructure improvements?"
            ],
            "Alternative Water Sources": [
                "Are alternative water sources (e.g., rainwater harvesting, recycling) utilized for non-potable uses?",
                "Is there evidence of systems like rainwater harvesting or recycled water being actively used for gardening or toilet flushing?"
            ],
            "Other Initiatives": [
                "Are there any other innovative or specialized water management practices implemented?",
                "Are these initiatives documented with supporting evidence (e.g., policy documents or photographs)?"
            ]
        }
    },
    "SI 2.4 Advanced Energy Management Systems": {
        "Key Aspects": {
            "Monitoring Energy Usage": [
                "Is energy usage monitored, and are reduction targets established?",
                "Are there reports or records showing energy usage monitoring and reduction targets?"
            ],
            "Behavioral Change Programs": [
                "Are there programs promoting behavioral changes to conserve energy?",
                "Do these programs include awareness campaigns or workshops?"
            ],
            "Analysis of Energy Usage": [
                "Are detailed analyses conducted on behavioral energy usage and infrastructure performance?",
                "Are system failures identified and addressed based on these analyses?"
            ],
            "Greenhouse Gas Emissions Monitoring": [
                "Is greenhouse gas emission monitoring conducted as part of energy management?",
                "Are strategies implemented to reduce greenhouse gas emissions?"
            ],
            "Alternative Energy Sources": [
                "Are alternative energy sources like biogas or solar energy used on campus?",
                "Is there evidence of the impact of alternative energy usage (e.g., measurable energy savings)?"
            ],
            "Other Initiatives": [
                "Are there any other innovative or specialized energy management initiatives implemented?",
                "Are these initiatives documented with supporting evidence (e.g., reports or photographs)?"
            ]
        }
    },
    "SI 2.5 Comprehensive Eco-friendly Transportation Systems": {
        "Key Aspects": {
            "Covered Walkways and Bike Lanes": [
                "Are covered walkways and bike lanes available to encourage walking and cycling?",
                "Is there evidence of widespread use of these facilities?"
            ],
            "Non-polluting/Low-emission Shuttles": [
                "Are non-polluting or low-emission shuttles or trams deployed within the campus?",
                "Are there maintenance and usage records for these vehicles?"
            ],
            "Integration with Public Transportation": [
                "Are campus transportation services integrated with public transportation networks?",
                "Is there evidence of effective utilization of public transportation integration?"
            ],
            "Private Parking Control Policy": [
                "Is a private parking control policy implemented to reduce vehicle usage on campus?",
                "Are there reports or data showing the impact of this policy?"
            ],
            "Other Innovative Measures": [
                "Are there any other innovative eco-friendly transportation measures implemented?",
                "Are these initiatives documented with supporting evidence (e.g., photographs or policy documents)?"
            ]
        }
    },
    "SI 3.1 Coverage of Medical Check-ups with Counseling Services": {
        "Key Aspects": {
            "Participation Data": [
                "Is there aggregated data on the number of staff participating in medical check-ups and counseling services?",
                "Does the data include breakdowns by department or faculty where applicable?"
            ],
            "Health Service Reports": [
                "Are there annual health service reports or summaries of health promotion activities?",
                "Do these reports include detailed statistics on staff engagement and program outcomes?"
            ],
            "Staff Feedback": [
                "Is anonymized staff feedback available regarding the service quality and effectiveness?",
                "Are there examples of satisfaction surveys, quotes, or case studies illustrating the impact of the services?"
            ]
        }
    },
    "SI 3.2 Comprehensive Mental Health Support Systems": {
        "Key Aspects": {
            "Academic Guidance on Mental Health": [
                "Is academic guidance on mental health provided to students and staff?",
                "Are there policy documents or descriptions outlining this guidance?"
            ],
            "Academic Services for Disabilities": [
                "Are academic services available for disabilities, dyslexia, and other specific learning difficulties?",
                "Are these services documented with evidence of implementation?"
            ],
            "Counseling for Life Difficulties": [
                "Is counseling available for addressing life difficulties such as stress, anxiety, or personal challenges?",
                "Are there reports or feedback validating the quality of these counseling services?"
            ],
            "Psychological Counseling and Crisis Support": [
                "Are psychological counseling services provided for crisis support, including personal violence and suicide prevention?",
                "Are examples of intervention outcomes or documented processes available?"
            ],
            "Psychiatric Psychotherapy": [
                "Is psychiatric psychotherapy, including a referral system, available on campus?",
                "Is there evidence of an effective referral system for psychiatric cases?"
            ],
            "Other Innovative Mental Health Services": [
                "Are there any other specialized or innovative mental health services implemented?",
                "Are these initiatives documented with supporting evidence (e.g., reports, photos, or testimonials)?"
            ]
        }
    },
    "SI 3.3 Comprehensive Healthy Lifestyle Support Programs": {
        "Key Aspects": {
            "Ergonomics Advice": [
                "Is advice provided on ergonomics to improve workplace and academic environment safety?",
                "Are there documents or workshops demonstrating this advice?"
            ],
            "Physical Activity Programs": [
                "Is physical activity advice provided, including structured fitness programs?",
                "Are these programs documented and actively promoted?"
            ],
            "Dietary Advice": [
                "Is dietary advice offered through nutrition workshops or counseling?",
                "Are there reports or evidence showing participation and effectiveness?"
            ],
            "Financial Well-being Programs": [
                "Is advice provided on investment and savings for financial well-being?",
                "Are there programs, workshops, or counseling sessions available for financial guidance?"
            ],
            "Substance Use Advice": [
                "Is advice to abstain from smoking, alcohol, and drugs provided, including cessation programs?",
                "Are these programs actively promoted and utilized?"
            ],
            "Other Innovative Healthy Lifestyle Services": [
                "Are there any other specialized healthy lifestyle support services implemented?",
                "Are these initiatives documented with supporting evidence (e.g., reports, photos, or testimonials)?"
            ]
        }
    },
    "SI 4.1 Comprehensive Disability Accessibility Measures": {
        "Key Aspects": {
            "Accessible Parking Spaces": [
                "Are parking spaces reserved for vehicles marked with the international symbol of access?",
                "Is there photographic or documentary evidence of these marked spaces?"
            ],
            "Accessible Public Lavatories": [
                "Are public lavatories equipped with facilities designed for wheelchair users?",
                "Are there photographs or architectural plans demonstrating these features?"
            ],
            "Sloped Paths": [
                "Are sloped paths provided to facilitate access to different levels of space?",
                "Are these paths integrated into the campus environment effectively?"
            ],
            "Accessible Campus Transportation": [
                "Is accessibility integrated into the campus transportation system?",
                "Is there evidence of adapted transportation options and their utilization?"
            ],
            "Other Innovative Measures": [
                "Are there any other innovative disability accessibility measures implemented?",
                "Are these measures documented with supporting evidence (e.g., reports, feedback, or testimonials)?"
            ]
        }
    },
    "SI 5.1 Integration of Health Promotion in Core University Curriculum": {
        "Key Aspects": {
            "Course Listings and Descriptions": [
                "Is there a list of core curriculum courses that incorporate health promotion topics?",
                "Are course descriptions available, detailing the health promotion topics covered?"
            ],
            "Participation Data": [
                "Are enrollment numbers for these courses available to demonstrate their reach and impact?",
                "Is there evidence of participation trends over time?"
            ],
            "Course Evaluations": [
                "Are course evaluations or feedback from students available?",
                "Do the evaluations assess the effectiveness and relevance of health promotion topics in these courses?"
            ]
        }
    },
    "SI 5.2 Integration of Health Promotion in Faculty-Specific Curricula": {
        "Key Aspects": {
            "Faculty Course Listings": [
                "Are detailed lists and descriptions of faculty-specific courses with health promotion topics available?",
                "Do the course descriptions clearly outline the health promotion aspects covered?"
            ],
            "Enrollment and Participation Data": [
                "Is there data showing student enrollment in these faculty-specific courses?",
                "Does the data highlight engagement levels across faculties and institutes?"
            ],
            "Feedback and Evaluations": [
                "Are there course evaluations or feedback from faculty and students regarding these courses?",
                "Do evaluations provide insights into the impact and quality of the health promotion topics taught?"
            ]
        }
    },
    "SI 6.1 Health Promotion Training Programs": {
        "Key Aspects": {
            "Training Session Schedules and Descriptions": [
                "Are schedules, brochures, or descriptions of health promotion training sessions available?",
                "Do the descriptions outline the topics covered in each training session?"
            ],
            "Participant Data": [
                "Are participant lists and attendance figures available for the training sessions and workshops?",
                "Is there evidence of consistent participation over time?"
            ],
            "Training Materials and Feedback": [
                "Are materials used in training sessions or workshops documented and provided?",
                "Is participant feedback or evaluation data available to assess the effectiveness of the training?"
            ],
            "Application of Training Outcomes": [
                "Are there examples of how training has been applied within the university or community settings?",
                "Do these examples demonstrate measurable outcomes or impacts from the training?"
            ]
        }
    },
    "SI 6.2 Online Tools and Resources for Health Promotion Capacity Building": {
        "Key Aspects": {
            "Applications or Online Tools": [
                "Are there applications or online tools specifically designed for health promotion activities?",
                "Is there evidence (e.g., screenshots, guides) showing their implementation and usage?"
            ],
            "Digital Health Promotion Resources": [
                "Are digital health promotion resources, such as e-learning modules for fitness and wellness, accessible through the university's network?",
                "Are these resources actively utilized, with evidence of engagement?"
            ],
            "Virtual Trainers or Advisors": [
                "Are virtual trainers or advisors available for health promotion training?",
                "Is there documentation or feedback highlighting their effectiveness?"
            ],
            "Online Monitoring and Evaluation Systems": [
                "Are online systems in place for monitoring and evaluating health promotion initiatives?",
                "Is there evidence demonstrating their functionality and usage?"
            ],
            "Other Innovative Online Resources": [
                "Are there any other innovative online resources developed or utilized by the university for health promotion?",
                "Are these initiatives documented with supporting evidence (e.g., user guides, testimonials)?"
            ]
        }
    },
    "SI 7.1 Core Health Promotion Research Activities at University Level": {
        "Key Aspects": {
            "Research Project List": [
                "Is there a comprehensive list of ongoing and completed university-level health promotion research projects?",
                "Does the list include project titles, lead researchers, and abstracts?"
            ],
            "Research Activity Reports": [
                "Are annual or biannual reports available detailing the scope and impact of these research activities?",
                "Do the reports include statistics on funding, collaboration, and outcomes?"
            ],
            "Publications and Presentations": [
                "Are there examples of publications and conference presentations derived from these research efforts?",
                "Do these publications highlight significant findings in health promotion research?"
            ]
        }
    },
    "SI 7.2 Faculty-Specific Health Promotion Research Activities": {
        "Key Aspects": {
            "Faculty Research Listings": [
                "Are there detailed listings of health promotion research projects conducted by each faculty?",
                "Do the listings include project summaries, lead researchers, and relevant details?"
            ],
            "Participation Data": [
                "Is there data showing the number and percentage of faculty members involved in health promotion research?",
                "Does the data include engagement trends over time?"
            ],
            "Impact Reports": [
                "Are faculty-specific reports or case studies available that illustrate the effectiveness and reach of the research?",
                "Do the reports highlight measurable outcomes or significant contributions to health promotion?"
            ]
        }
    },
    "SI 7.3 Support for Health Promotion Research": {
        "Key Aspects": {
            "Policy to Promote Research": [
                "Is there a formal policy or guideline to promote health promotion research?",
                "Is the policy document available, and does it outline specific objectives or mandates?"
            ],
            "University Funding Support": [
                "Is direct financial support provided by the university for health promotion research?",
                "Are there reports or documentation showing funding allocations or grants received?"
            ],
            "External Funding Support": [
                "Is there evidence of financial grants from external organizations (e.g., government, NGOs, private sectors) for health promotion research?",
                "Are funding agreements or reports detailing the usage of external funding available?"
            ],
            "Training for Health Promotion Research": [
                "Are there regular training sessions or workshops aimed at enhancing research skills in health promotion?",
                "Are schedules, program outlines, or participant feedback from these sessions available?"
            ],
            "Other Innovative Supports": [
                "Are there any other innovative supports provided by the university to facilitate health promotion research?",
                "Are these supports documented with evidence (e.g., reports, feedback, or testimonials)?"
            ]
        }
    },
    "SI 8.1 Comprehensive University Volunteerism in Health Promotion": {
        "Key Aspects": {
            "Community-Based Health Promotion Campaigns": [
                "Are there regular volunteer activities focused on health promotion campaigns within the local community?",
                "Are descriptions and schedules of these activities available?"
            ],
            "Engagement with Community Members": [
                "Are community members actively engaged in health promotion programs organized by the university?",
                "Is there documentation, such as participation records or photographs, showing this engagement?"
            ],
            "Participation in National or Subnational Programs": [
                "Do university personnel participate in national or subnational health promotion programs?",
                "Are there records or reports demonstrating the university's involvement in these programs?"
            ],
            "Policy Development and Implementation": [
                "Does the university contribute to the development or implementation of health promotion policies at the national or international level?",
                "Are there acknowledgments or documentation from policy bodies or organizations recognizing this contribution?"
            ],
            "Other Volunteer Activities": [
                "Are there any other volunteer activities conducted by the university to support health promotion?",
                "Are these activities documented with evidence (e.g., testimonials, photographs, or reports)?"
            ]
        }
    },
    "SI 9.1 Allocation of Budgetary Support for Health Promotion Programs": {
        "Key Aspects": {
            "Financial Reports and Budget Documents": [
                "Are there financial reports or budget allocation documents detailing funding for health promotion programs?",
                "Do these documents specify allocations to faculties or institutes for health promotion initiatives?"
            ],
            "Impact Statements": [
                "Are there statements or testimonials from faculty deans or program directors describing the impact of the financial support?",
                "Do the statements provide specific examples of how the funding has improved health promotion efforts?"
            ],
            "Supported Health Promotion Initiatives": [
                "Are there examples of health promotion initiatives enabled or significantly supported by the allocated budgets?",
                "Do these examples demonstrate measurable outcomes or improvements due to financial support?"
            ]
        }
    },
    "SI 9.2 Proportion of University Budget Allocated to Health Promotion": {
        "Key Aspects": {
            "Budget Summaries and Financial Reports": [
                "Are there budget summaries or financial reports detailing expenditures on health promotion?",
                "Do these reports specify health promotion spending as a proportion of the total university budget?"
            ],
            "Financial Planning Documents": [
                "Are there extracts from financial planning documents or board-approved budgets highlighting allocations for health promotion?",
                "Do these documents demonstrate a clear commitment to funding health promotion activities?"
            ],
            "Breakdown of Specific Programs": [
                "Is there a breakdown of specific health promotion programs or initiatives funded?",
                "Are the corresponding budget allocations for each program or initiative detailed?"
            ]
        }
    },
    "ZT 1.1 Comprehensive Tobacco Control Policy": {
        "Key Aspects": {
            "Prohibition of Tobacco Sales": [
                "Is the sale of tobacco products prohibited within university premises?",
                "Are there policies or regulations documenting this prohibition?"
            ],
            "Ban on Smoking in University Properties": [
                "Is smoking completely banned within all university-owned or controlled properties?",
                "Are there enforcement mechanisms, such as signage or reports, ensuring compliance?"
            ],
            "Educational Campaigns": [
                "Are educational campaigns conducted to inform students and staff about the risks associated with smoking?",
                "Is there evidence, such as participation data or materials, showing the effectiveness of these campaigns?"
            ],
            "Prohibition of Tobacco Advertisements": [
                "Are tobacco-related advertisements prohibited on campus?",
                "Are policies or enforcement measures in place to prevent such advertisements?"
            ],
            "Counseling and Referral Services": [
                "Are counseling and referral services for smoking cessation available to students and staff?",
                "Is there evidence of utilization rates and outcomes for these services?"
            ],
            "Other Innovative Measures": [
                "Are there any other innovative tobacco control measures implemented?",
                "Are these measures documented with evidence (e.g., reports, testimonials)?"
            ]
        }
    },
    "ZT 1.2 Smoking and Vaping Prevalence Among Students and Personnel": {
        "Key Aspects": {
            "Survey Instrument": [
                "Is there a survey instrument used to collect data on smoking and vaping habits among students and staff?",
                "Are the survey questions relevant and designed to encourage honest reporting?"
            ],
            "Summary of Results": [
                "Is there a summary of the survey results, including the number of participants and calculated smoking rates?",
                "Does the summary highlight smoking prevalence for both students and staff?"
            ],
            "Sampling Methodology": [
                "Is there a description of the sampling methodology used to ensure the representativeness of the data?",
                "Does the methodology account for a diverse and inclusive sample of the university population?"
            ],
            "Comparative Data": [
                "Is there comparative data from previous years available to demonstrate trends over time?",
                "Does the comparative data align with the current smoking prevalence findings?"
            ],
            "Population and Data Analysis": [
                "Is the total population size of students and staff included in the survey clearly described?",
                "Is the process or method used to gather and analyze the smoking prevalence data documented?"
            ]
        }
    },
    "ZT 2.1 Comprehensive Alcohol Control Measures": {
        "Key Aspects": {
            "Prohibition of Alcohol Sales": [
                "Is the sale of alcohol prohibited within and immediately around (300 meters) the university premises?",
                "Are there policies or regulations documenting this prohibition?"
            ],
            "Ban on Alcohol Consumption at University Functions": [
                "Is alcohol consumption banned at all social functions hosted by the university?",
                "Are there enforcement actions or event guidelines supporting this policy?"
            ],
            "Educational Campaigns": [
                "Are educational campaigns conducted to inform students and staff about the risks and negative impacts of alcohol consumption?",
                "Is there evidence, such as campaign materials or participation data, demonstrating the effectiveness of these campaigns?"
            ],
            "Prohibition of Alcohol Advertisements": [
                "Are alcohol-related advertisements prohibited within university property?",
                "Are policies or enforcement measures in place to ensure compliance?"
            ],
            "Counseling and Referral Services": [
                "Are counseling and referral services available for individuals seeking help with alcohol issues?",
                "Is there evidence of utilization rates and feedback on these services?"
            ],
            "Other Innovative Measures": [
                "Are there any other innovative alcohol control measures implemented?",
                "Are these measures documented with evidence (e.g., reports, testimonials)?"
            ]
        }
    },
    "ZT 2.2 Prevalence of Alcohol Consumption Among Students and Personnel": {
        "Key Aspects": {
            "Survey Instrument": [
                "Is there a survey instrument used to collect data on alcohol consumption habits among students and staff?",
                "Are the survey questions comprehensive and designed to include frequency and quantity of alcohol consumption?"
            ],
            "Summary of Results": [
                "Is there a summary of the survey results, including the number of participants and alcohol consumption rates?",
                "Does the summary highlight drinking behaviors for both students and staff?"
            ],
            "Sampling Methodology": [
                "Is there a description of how the survey ensures anonymity and represents a diverse cross-section of the university population?",
                "Does the methodology demonstrate efforts to capture accurate and unbiased data?"
            ],
            "Comparative Data": [
                "Is there comparative data from previous years to show trends in alcohol consumption?",
                "Does the comparative data align with the current findings?"
            ],
            "Data Analysis and Reporting": [
                "Is the total population size of students and staff included in the survey clearly described?",
                "Are the statistical methods used for data analysis documented and appropriate?"
            ]
        }
    },
    "ZT 3.1 Comprehensive Measures Against Narcotic Drug Use": {
        "Key Aspects": {
            "Prohibition of Narcotic Drugs Use": [
                "Is the use of narcotic drugs prohibited within all university properties?",
                "Are there policies or regulations documenting this prohibition?"
            ],
            "Active Surveillance and Monitoring": [
                "Is there active surveillance and monitoring to detect narcotic drug sale and usage on campus?",
                "Are there reports or data demonstrating the effectiveness of surveillance measures?"
            ],
            "Educational Campaigns": [
                "Are educational campaigns conducted to inform students and staff about the risks and legal consequences of narcotic drug use?",
                "Is there evidence, such as campaign materials or participation data, showing the effectiveness of these campaigns?"
            ],
            "Counseling and Referral Services": [
                "Are counseling and referral services available for individuals seeking help with drug-related issues?",
                "Is there evidence of utilization rates and feedback on these services?"
            ],
            "Other Innovative Measures": [
                "Are there any other innovative measures implemented to combat narcotic drug use?",
                "Are these measures documented with evidence (e.g., reports, testimonials)?"
            ]
        }
    },
    "ZT 4.1 Comprehensive Anti-Gambling Measures": {
        "Key Aspects": {
            "Prohibition of Gambling": [
                "Is the prohibition of all forms of gambling within university properties enforced?",
                "Are there policies or regulations documenting this prohibition?"
            ],
            "Educational Programs": [
                "Are educational programs conducted to inform students and staff about the adverse effects of gambling?",
                "Is there evidence, such as campaign materials or participation data, demonstrating the effectiveness of these programs?"
            ],
            "Active Surveillance and Monitoring": [
                "Is there active surveillance and monitoring to detect gambling activities on campus?",
                "Are there reports or data demonstrating the effectiveness of these monitoring measures?"
            ],
            "Counseling and Probation Programs": [
                "Are counseling and probation programs available for habitual gamblers?",
                "Is there evidence of utilization rates and feedback on these programs?"
            ],
            "Other Innovative Measures": [
                "Are there any other innovative measures implemented to prevent gambling?",
                "Are these measures documented with evidence (e.g., reports, testimonials)?"
            ]
        }
    },
    "ZT 5.1 Comprehensive Measures Against Violence, Bullying, and Sexual Harassment": {
        "Key Aspects": {
            "Formal Policies": [
                "Are there formal policies that clearly prohibit violence, bullying, and sexual harassment on campus?",
                "Are these policies effectively communicated to all members of the university community?"
            ],
            "Educational Programs": [
                "Are educational programs conducted to prevent violence, bullying, and sexual harassment?",
                "Is there evidence, such as program materials or feedback, demonstrating the effectiveness of these programs?"
            ],
            "Surveillance Programs": [
                "Are surveillance programs in place to monitor and address incidents of sexual harassment effectively?",
                "Are there reports or data showing the impact and outcomes of these programs?"
            ],
            "Confidential Reporting System": [
                "Is there a confidential system for students and staff to report incidents of violence, bullying, and sexual harassment without fear of reprisal?",
                "Is there evidence of the system’s effectiveness, such as usage statistics or testimonials?"
            ],
            "Rehabilitation and Empowerment Programs": [
                "Are there rehabilitation and empowerment programs available for individuals affected by violence, bullying, and sexual harassment?",
                "Is there evidence of utilization rates and feedback on these programs?"
            ],
            "Other Innovative Measures": [
                "Are there any other innovative measures implemented to address violence, bullying, and sexual harassment?",
                "Are these measures documented with evidence (e.g., reports, testimonials)?"
            ]
        }
    },
    "ZT 6.1 Comprehensive Road Safety Measures": {
        "Key Aspects": {
            "Enforcement of Road Safety Policies": [
                "Are there policies strictly enforcing road safety measures, such as mandatory seat belt and helmet use?",
                "Is there evidence of policy enforcement, such as reports or compliance data?"
            ],
            "Road Safety Education Programs": [
                "Are road safety education programs conducted to inform students and staff about safe driving practices and traffic laws?",
                "Is there evidence, such as program materials or participant feedback, demonstrating the effectiveness of these programs?"
            ],
            "Safety Environment Enhancements": [
                "Have safety environment enhancements been implemented, such as well-maintained roads, proper signage, and pedestrian zones?",
                "Are there photographs or other evidence showcasing these improvements?"
            ],
            "Emergency Management Protocols": [
                "Are there comprehensive emergency management protocols for handling traffic injuries?",
                "Is there evidence of training sessions or examples of protocol activation?"
            ],
            "Other Innovative Measures": [
                "Are there any other innovative road safety measures implemented to enhance safety on campus?",
                "Are these measures documented with evidence (e.g., reports, testimonials)?"
            ]
        }
    },
    "ZT 6.2 Compliance with Helmet Use Among Motorcyclists": {
        "Key Aspects": {
            "Data Collection Methodology": [
                "Is there a detailed methodology explaining how helmet use data was collected?",
                "Does the methodology include an observation protocol, sampling strategy, and the number of observations made?"
            ],
            "Summary of Observations": [
                "Is there a summary of the data collected, including the number of motorcyclists observed and the percentage wearing helmets?",
                "Does the summary include details of observations made at different times and locations?"
            ],
            "Assistive Technologies Used": [
                "Were assistive technologies, such as CCTV surveillance or time-lapse photography, utilized to collect helmet usage data?",
                "Is there evidence, such as screenshots or reports, demonstrating how these technologies were applied?"
            ],
            "Policies and Initiatives": [
                "Are there initiatives or policies in place to encourage helmet use among motorcyclists on campus?",
                "Is there evidence of the impact of these initiatives, such as changes in compliance rates over time?"
            ],
            "Supplementary Data": [
                "Were any additional surveys or questionnaires used to supplement the observation data?",
                "Is there evidence, such as survey results or feedback, validating the helmet use compliance rates?"
            ]
        }
    },
    "ZT 6.3 Monitoring Road Accident Incidents Relative to Campus Population": {
        "Key Aspects": {
            "Accident Reports": [
                "Are there official accident reports detailing the nature, cause, and outcome of each incident?",
                "Do the reports include all types of accidents (motor vehicles, motorcycles, bicycles, pedestrians)?"
            ],
            "Statistical Analysis": [
                "Is there a comprehensive analysis of the accident data, including rates per 100,000 and trends over time?",
                "Does the analysis highlight high-risk locations and times of day when accidents are most frequent?"
            ],
            "Preventive Measures Taken": [
                "Have preventive measures been implemented during the year in response to reported accidents?",
                "Is there evidence, such as improved signage, traffic flow changes, or enhanced lighting, to support these measures?"
            ],
            "Surveillance Footage or Photos": [
                "Is there surveillance footage or photos from accident scenes to provide context for the reported data?",
                "Do these visuals support the accident analysis and preventive measures taken?"
            ],
            "Feedback from Campus Community": [
                "Is there feedback or testimonials from students, staff, and visitors regarding road safety on campus?",
                "Does the feedback align with the reported accident data and preventive measures?"
            ]
        }
    },
    "HP 1.1 Comprehensive Health Literacy Initiatives": {
        "Key Aspects": {
            "Exhibitions and Posters": [
                "Are regular exhibitions or boards/posters on health promotion displayed within university premises?",
                "Is there evidence, such as photographs or examples of the displayed materials?"
            ],
            "Health Promotion Events and Materials": [
                "Are regular health promotion events conducted, or is knowledge provided through printed materials or websites?",
                "Is there evidence of these events or materials, such as agendas, participant lists, or website links?"
            ],
            "Online and Media Channels": [
                "Is health promotion knowledge regularly shared through radio, TV, or web-based channels?",
                "Is there evidence, such as links, screenshots, or descriptions of these media efforts?"
            ],
            "Training Programs": [
                "Are regular health promotion or lifestyle training programs conducted?",
                "Is there evidence, such as schedules, curriculum details, or participant feedback?"
            ],
            "Other Innovative Activities": [
                "Are there any other innovative activities designed to promote health literacy?",
                "Are these activities documented with evidence, such as reports, testimonials, or feedback?"
            ]
        }
    },
    "HP 1.2 Effective Assessment and Utilization of KAP on Healthy Lifestyle": {
        "Key Aspects": {
            "Survey Instrument and Data": [
                "Is there a survey instrument used to assess knowledge, attitudes, and practices (KAP) related to healthy lifestyles?",
                "Is there evidence of data collected through this survey?"
            ],
            "Utilization of Survey Results": [
                "Have the results of the KAP survey been used to improve health literacy programs?",
                "Is there documentation or examples of how the results were utilized for program planning and execution?"
            ],
            "Frequency of Surveys": [
                "Are KAP surveys conducted annually or on a regular basis?",
                "Is there evidence of consistent survey administration and analysis?"
            ],
            "Evidence of Improvement": [
                "Is there documented evidence of measurable changes in health literacy, attitudes, or behaviors as a result of interventions informed by the KAP surveys?",
                "Are there reports or studies that detail these improvements?"
            ],
            "Participant Feedback": [
                "Are there testimonials or feedback from participants reflecting the perceived impact of changes to health literacy programs?",
                "Is this feedback recent and relevant to the current academic year?"
            ]
        }
    },
    "HP 2.1 Coverage of Stress Reduction Programs": {
        "Key Aspects": {
            "Program Availability": [
                "Is there a list or database of faculties/institutes that offer stress reduction programs?",
                "Does the data specify the types of programs offered and their availability?"
            ],
            "Program Details": [
                "Are quantitative data provided on the number of programs, their frequency, and participation rates?",
                "Is there evidence demonstrating the scope and reach of these programs?"
            ],
            "Program Types": [
                "Do the programs include mindfulness sessions, mental health workshops, counseling services, relaxation zones, or de-stress activities?",
                "Is there evidence of diverse and comprehensive program offerings?"
            ],
            "Feedback and Effectiveness": [
                "Are there testimonials or feedback from participants to gauge the effectiveness of these programs?",
                "Is the feedback recent and directly relevant to the stress reduction initiatives?"
            ]
        }
    },
    "HP 2.2 Comprehensive Mental Health Assessment Programs": {
        "Key Aspects": {
            "Program Structure and Scope": [
                "Is there documentation detailing the structure and scope of the mental health programs offered?",
                "Do these programs include provisions for expert mental health professionals, such as psychologists or psychiatrists?"
            ],
            "Screening and Counseling Services": [
                "Are comprehensive mental health screening programs implemented?",
                "Are counseling services provided to address issues identified during screenings?"
            ],
            "Surveillance or Vigilance Programs": [
                "Is there a surveillance or vigilance program for ongoing monitoring of mental health?",
                "Does the program offer proactive measures for intervention and immediate support?"
            ],
            "Care and Referral Support": [
                "Does the surveillance program include extensive care and referral support to specialized services for affected individuals?",
                "Is there evidence of successful referrals and follow-up outcomes?"
            ],
            "Participant Feedback and Outcomes": [
                "Are there testimonials or feedback from participants and staff about the impact of these programs?",
                "Is there data demonstrating the effectiveness and outcomes of the mental health initiatives?"
            ]
        }
    },
    "HP 3.1 Coverage of Student Clubs on Health Promotion": {
        "Key Aspects": {
            "Club Availability": [
                "Is there a list or database of faculties/institutes offering health promotion-related student clubs?",
                "Does the data specify the types of clubs and their health promotion focus?"
            ],
            "Membership and Participation": [
                "Are quantitative data provided on membership numbers and participation rates in these clubs?",
                "Is there evidence of active engagement through regular meetings or events?"
            ],
            "Event Materials and Documentation": [
                "Are there examples of event flyers, meeting minutes, or promotional materials showcasing club activities?",
                "Is there evidence of diverse activities within these clubs?"
            ],
            "Participant Feedback": [
                "Are there testimonials or feedback from participants regarding the effectiveness of these clubs?",
                "Is the feedback recent and relevant to the health promotion activities of the clubs?"
            ]
        }
    },
    "HP 4.1 Availability and Utilization of Physical Activity Facilities": {
        "Key Aspects": {
            "Policies and Events": [
                "Are there policies and organized special health-promoting exercise events?",
                "Is there evidence, such as policy documents or event schedules, to support these initiatives?"
            ],
            "Outdoor Exercise Platforms": [
                "Are outdoor exercise platforms accessible within the campus?",
                "Is there evidence, such as photographs or maps, showing the availability of outdoor exercise spaces?"
            ],
            "Indoor Exercise Spaces": [
                "Are indoor exercise spaces, such as fitness centers, available to students and staff?",
                "Is there evidence of active usage, such as booking records or attendance data?"
            ],
            "Specialized Facilities": [
                "Are multiple specialized facilities, such as bicycle tracks, swimming pools, or sports courts, accessible?",
                "Is there evidence of their availability and active utilization?"
            ],
            "Other Innovative Facilities": [
                "Are there any other innovative physical activity facilities or policies implemented?",
                "Is there evidence of their implementation and impact on promoting physical health?"
            ]
        }
    },
    "HP 4.2 Availability of Sport or Physical Activity Events": {
        "Key Aspects": {
            "Event Database and Details": [
                "Is there a list or database of all sport and physical activity events held across faculties/institutes?",
                "Does the database include details such as dates and types of events?"
            ],
            "Participation and Engagement": [
                "Are attendance records or participation rates available to demonstrate engagement in these events?",
                "Is there evidence of strong participation by students and staff?"
            ],
            "Promotional Materials and Summaries": [
                "Are there promotional materials or event summaries highlighting the scope and frequency of these activities?",
                "Do these materials showcase a diverse range of events across faculties?"
            ],
            "Feedback and Impact": [
                "Are there feedback or testimonials from participants regarding the impact of these events on promoting physical health?",
                "Is the feedback recent and relevant to the activities held in the last academic year?"
            ]
        }
    },
    "HP 4.3 Promotion of Sleep and Mindfulness Programs": {
        "Key Aspects": {
            "Program Listings and Descriptions": [
                "Is there a comprehensive list of sleep and mindfulness programs offered by faculties/institutes?",
                "Do the descriptions include goals and objectives for these programs?"
            ],
            "Participation Data": [
                "Are enrollment or attendance data available for these programs to demonstrate their reach and engagement?",
                "Is there evidence of active participation by students and staff?"
            ],
            "Program Materials": [
                "Are there samples of educational materials or session outlines provided during these programs?",
                "Do these materials reflect comprehensive and structured approaches to sleep and mindfulness promotion?"
            ],
            "Feedback and Impact Assessments": [
                "Are there testimonials or feedback from participants regarding the impact of these programs on sleep quality and mental well-being?",
                "Are there impact assessments or evaluations that demonstrate the effectiveness of these programs?"
            ]
        }
    },
    "HP 5.1 Comprehensive Healthy Diet Programs": {
        "Key Aspects": {
            "Policies on Healthy Diets": [
                "Is there a formal policy on promoting a healthy diet within the university?",
                "Does the policy include clear measures and objectives?"
            ],
            "Educational Programs": [
                "Are there regular educational programs aimed at informing students and personnel about nutritional guidelines and healthy eating habits?",
                "Are these programs well-structured and supported by evidence, such as schedules or curricula?"
            ],
            "Marketplace Availability": [
                "Are marketplaces within or near the university arranged to ensure the availability of healthy food options?",
                "Is there evidence, such as photographs or records, demonstrating access to healthy food?"
            ],
            "Demonstration Programs": [
                "Are there demonstration programs showcasing the production of healthy food and vegetables either on campus or in the local community?",
                "Do these programs include practical and educational components?"
            ],
            "Other Innovative Initiatives": [
                "Are there other innovative initiatives designed to promote a healthy diet?",
                "Is there evidence of their implementation and effectiveness?"
            ]
        }
    },
    "HP 5.2 Implementation of Healthy Canteen Initiatives": {
        "Key Aspects": {
            "Policy and Training Programs": [
                "Is there a specific policy promoting healthy food options in canteens?",
                "Are training programs provided for food sellers to promote the preparation and sale of healthy food?"
            ],
            "Promotion of Healthy Food": [
                "Are healthy food options actively promoted in canteens and food outlets of some faculties/institutes?",
                "Are healthy food options promoted in all canteens and food outlets across the university?"
            ],
            "Surveillance and Monitoring": [
                "Is there ongoing monitoring of unhealthy food in canteens, food outlets, and surrounding areas?",
                "Are reports of findings and actions taken following surveillance available?"
            ]
        }
    },
    "HP 6.1 Availability of Sex Education Programs": {
        "Key Aspects": {
            "Program Listings and Details": [
                "Is there a list or database of faculties/institutes offering sex education programs?",
                "Do the details include topics such as safe sexual behaviors, contraception, and STI prevention?"
            ],
            "Program Frequency and Participation": [
                "Are quantitative data available on the number of programs, their frequency, and participation rates?",
                "Is there evidence of active engagement by students and staff in these programs?"
            ],
            "Educational Materials": [
                "Are there examples of curricula, teaching materials, or promotional materials used for these programs?",
                "Do these materials reflect comprehensive and up-to-date information on sexual health?"
            ],
            "Feedback and Impact": [
                "Are there testimonials or feedback from participants regarding the relevance and impact of these programs?",
                "Is there evidence of measurable outcomes or improvements related to sexual health awareness?"
            ]
        }
    },
    "HP 6.2 Comprehensive Safer Sex Programs": {
        "Key Aspects": {
            "Counseling and Support": [
                "Are counseling programs focused on promoting safer sex behaviors available?",
                "Is there evidence of structured and accessible counseling services for students and staff?"
            ],
            "Surveillance Program": [
                "Is there a surveillance program to monitor and address sexual risk behaviors?",
                "Are reports or findings from the surveillance program available?"
            ],
            "Campaigns and Awareness": [
                "Are there campaigns aimed at preventing sexual risk behaviors among students and staff?",
                "Are campaign materials, such as posters, workshops, or events, available for review?"
            ],
            "Safer Sex Commodities": [
                "Are safer sex commodities, such as condoms and information leaflets, readily available on campus?",
                "Are there distribution records or usage statistics demonstrating the reach of these commodities?"
            ],
            "Other Innovative Measures": [
                "Are there other innovative measures implemented to promote safer sex?",
                "Is there evidence of their implementation and effectiveness?"
            ]
        }
    },
    "HP 7.1 Coverage of Work-Life Balance Programs": {
        "Key Aspects": {
            "Program Listings and Details": [
                "Is there a list or database of faculties/institutes offering work-life balance programs?",
                "Do the program descriptions include initiatives like flexible working arrangements, parenting support, or fitness activities?"
            ],
            "Participation Data": [
                "Is quantitative data available on the number of programs, their frequency, and participation rates?",
                "Is there evidence of consistent engagement by students and staff in these programs?"
            ],
            "Program Materials": [
                "Are there examples of schedules, promotional materials, or content used for these programs?",
                "Do the materials reflect comprehensive and well-structured work-life balance initiatives?"
            ],
            "Feedback and Impact": [
                "Are there testimonials or feedback from participants regarding the relevance and impact of these programs?",
                "Is there evidence of measurable outcomes or improvements related to work-life balance and well-being?"
            ]
        }
    },
    "HP 7.2 Comprehensive Healthy Ageing Programs": {
        "Key Aspects": {
            "Awareness Programs": [
                "Are awareness programs on healthy and active ageing targeted at university personnel and the community implemented?",
                "Is there evidence of regular and impactful awareness activities?"
            ],
            "Skill Development": [
                "Are there ageing skill programs designed to equip pre-ageing personnel with necessary skills for later life?",
                "Do the programs include structured learning and measurable outcomes?"
            ],
            "Employment Support": [
                "Are there employment programs providing job opportunities specifically for ageing individuals?",
                "Are records of job roles created and placement success rates available?"
            ],
            "Empowerment Initiatives": [
                "Are there empowerment programs aimed at enhancing the wellbeing of the ageing population in the surrounding community?",
                "Is there evidence of outreach efforts and community impact?"
            ],
            "Other Innovative Measures": [
                "Are there other innovative measures implemented to support healthy ageing?",
                "Is there evidence of their implementation and effectiveness?"
            ]
        }
    }
}

# Sidebar for Navigation
question = st.sidebar.selectbox("Select Question to Score", list(questions_data.keys()))

# Input for Assessor Name
assessor = st.text_input("Enter Your Name", "")

# Scoring Section
if assessor and question:
    st.header(f"Scoring for: {question}")
    key_aspects = questions_data[question]["Key Aspects"]  # Fetch key aspects dynamically

    responses = []
    for key, questions in key_aspects.items():
        st.subheader(key)
        for idx, q in enumerate(questions):
            # Use unique keys for each input
            score = st.slider(q, 0, 1, 0, key=f"{question}_{key}_{idx}_score")
            comment = st.text_input(f"Comments for: {q}", key=f"{question}_{key}_{idx}_comment")
            responses.append({
                "Assessor": assessor,
                "Question": question,
                "Key Aspect": key,
                "Score": score,
                "Comments": comment
            })

    if st.button(f"Save All Scores for {question}"):
        # Convert responses to DataFrame and append to the main DataFrame
        new_rows_df = pd.DataFrame(responses)
        df = pd.concat([df, new_rows_df], ignore_index=True)
        df.to_csv(data_file, index=False)
        st.success(f"All scores for {question} saved successfully!")

# Display Results Summary in Tabs
if st.sidebar.checkbox("View Results Summary"):
    st.header("Results Summary")
    
    # Ensure questions is a list of unique questions or an empty list
    questions = list(df["Question"].unique()) if not df.empty else []

    if questions:
        tabs = st.tabs(questions)
        for idx, question_tab in enumerate(tabs):
            with question_tab:
                st.subheader(f"Results for {questions[idx]}")
                filtered_df = df[df["Question"] == questions[idx]]  # Filter data by question
                st.dataframe(filtered_df)

                if not filtered_df.empty:
                    fig = px.bar(
                        filtered_df.groupby("Key Aspect")["Score"].mean().reset_index(),
                        x="Key Aspect",
                        y="Score",
                        color="Key Aspect",
                        title=f"Scores for {questions[idx]}",
                        labels={"Score": "Average Score"}
                    )
                    st.plotly_chart(fig)
                else:
                    st.write(f"No data available for {questions[idx]}.")
    else:
        st.write("No questions available in the dataset.")

# Allow Downloading Results as CSV
@st.cache_data
def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False).encode("utf-8")

if st.sidebar.checkbox("Download Results"):
    csv = convert_df_to_csv(df)
    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name="results_summary.csv",
        mime="text/csv"
    )
