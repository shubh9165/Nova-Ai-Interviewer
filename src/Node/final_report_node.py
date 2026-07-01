from src.State.state import State
from src.LLMs.GroqLLm import GroqLLm

llm = GroqLLm().get_llm()

def final_report_node(state: State):

    try:

        prompt = f"""
        Generate final interview report.

        Questions:
        {state['questions']}

        Answers:
        {state['answers']}

        Evaluation Reports:
        {state['evaluation_reports']}

        Give:

        Overall Score
        Technical Skill
        Communication
        Recommendation

        Final Verdict
        """

        response = llm.invoke(prompt)

        return {
            "final_report": response.content
        }

    except Exception as e:
        raise ValueError(str(e))