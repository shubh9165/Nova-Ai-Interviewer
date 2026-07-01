from src.State.state import State
from src.LLMs.GroqLLm import GroqLLm

llm = GroqLLm().get_llm()

def evaluator_node(state: State):

    try:

        question = state["questions"][-1]
        answer = state["answers"][-1]

        prompt = f"""
        You are a senior interviewer.

        Question:
        {question}

        Candidate Answer:
        {answer}

        Evaluate answer.

        Return:

        Score: x/10

        Strengths:
        Weaknesses:
        Feedback:
        """

        response = llm.invoke(prompt)

        return {
            "evaluation_reports":
                state["evaluation_reports"] + [response.content]
        }

    except Exception as e:
        raise ValueError(str(e))