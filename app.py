import streamlit as st

from src.Graph.graph import create_graph
from src.Node.final_report_node import final_report_node
from src.voice_tools.voice_recorder import Recoder
from src.voice_tools.text_to_speech import text_to_speech
from src.voice_tools.speech_to_text import SpeechToText
import os
#speaker=text_to_speech()
#Recoder=Recoder()

st.set_page_config(
    page_title="Nova AI Interviewer",
    page_icon="🤖",
    layout="wide"
)



st.title("🤖 Nova AI Interviewer")

# -------------------------
# Session State Initialization
# -------------------------

if "interview_state" not in st.session_state:

    st.session_state.interview_state = {
        "questions": [],
        "answers": [],
        "evaluation_reports": [],
        "question_number": 0,
        "role": "",
        "difficulty": "",
        "subject": "",
        "final_report": ""
    }

if "started" not in st.session_state:
    st.session_state.started = False

if "speaker" not in st.session_state:
    st.session_state.speaker=text_to_speech()

if "last_spoken_question" not in st.session_state:
    st.session_state.last_spoken_question = ""

if "recorder" not in st.session_state:
    st.session_state.recorder=Recoder()

if "current_answer" not in st.session_state:
    st.session_state.current_answer = ""

if "transcriber" not in st.session_state:
    st.session_state.transcriber = SpeechToText()



# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.header("Interview Configuration")

    role = st.text_input(
        "Job Role",
        placeholder="AI/ML Engineer"
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    total_questions = st.number_input(
        "Number of Questions",
        min_value=1,
        max_value=20,
        value=5
    )

    start_button = st.button(
        "Start Interview"
    )

# -------------------------
# Start Interview
# -------------------------

if start_button:

    st.session_state.started = True


    st.session_state.interview_state = {
        "questions": [
            "Please introduce yourself."
        ],
        "answers": [],
        "evaluation_reports": [],
        "question_number": 1,
        "role": role,
        "difficulty": difficulty,
        "subject": "",
        "final_report": ""
    }

    st.rerun()

# -------------------------
# Interview Running
# -------------------------

if st.session_state.started:

    state = st.session_state.interview_state

    # Interview Complete
    if state["question_number"] > total_questions:

        st.success("Interview Completed ✅")

        if not state["final_report"]:

            report = final_report_node(state)

            state["final_report"] = report["final_report"]

            st.session_state.interview_state = state

        st.markdown("## Final Interview Report")

        st.write(state["final_report"])

    else:

        current_question = state["questions"][-1]


       

        st.markdown(
            f"### Question {state['question_number']}"
        )

        st.info(current_question)

        if st.session_state.last_spoken_question != current_question:
            audio_buffer=st.session_state.speaker.speak(current_question)

            st.session_state.last_spoken_question = current_question
            st.audio(audio_buffer, format="audio/wav")

        #Recoder.recorder()

        audio=st.session_state.recorder.recorder()
        
        if audio:
            audio_text = st.session_state.transcriber.transcribe("answer.wav")
            st.session_state.current_answer=audio_text
            st.success(audio_text)
            os.remove("answer.wav")




        submit_answer = st.button(
            "Submit Answer"
        )

        if submit_answer:
            answer=st.session_state.current_answer
            if answer.strip() == "":

                st.warning(
                    "Please enter an answer."
                )

            else:

                # Store answer
                state["answers"].append(answer)

                # Build Graph
                graph = create_graph()

                # Run Graph
                updated_state = graph.invoke(state)

                # Increment question counter
                updated_state["question_number"] += 1

                # Save State
                st.session_state.interview_state = updated_state
                #st.session_state.spoken_question = -1
                st.rerun()

# -------------------------
# Show Progress
# -------------------------

if st.session_state.started:

    state = st.session_state.interview_state

    st.divider()

    st.subheader("Interview Progress")

    st.write(
        f"Questions Answered: {len(state['answers'])}"
    )

    st.write(
        f"Evaluations Generated: {len(state['evaluation_reports'])}"
    )

    if len(state["evaluation_reports"]) > 0:

        with st.expander("Latest Evaluation"):

            st.write(
                state["evaluation_reports"][-1]
            )