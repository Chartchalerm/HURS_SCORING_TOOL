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
