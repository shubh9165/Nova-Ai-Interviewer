from src.State.state import State
from src.LLMs.GroqLLm import GroqLLm

llm = GroqLLm().get_llm()

def question_generator_node(state: State):

    try:

        if len(state["questions"]) == 0:

            prompt = f"""
            You are a senior interviewer.

            Role: {state['role']}
            Difficulty: {state['difficulty']}

            Generate the first interview question.
            """

        else:

            last_question = state["questions"][-1]

            prompt = f"""
            You are a senior interviewer.

            Role: {state['role']}
            Difficulty: {state['difficulty']}

            Previous Question:
            {last_question}

            Generate next interview question.
            """

        response = llm.invoke(prompt)

        return {
            "questions": state["questions"] + [response.content]
        }

    except Exception as e:
        raise ValueError(str(e))