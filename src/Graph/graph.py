from langgraph.graph import StateGraph, START, END
from src.Node.evaluator_node import evaluator_node
from src.Node.question_genration_node import question_generator_node
from src.State.state import State
def create_graph():

    graph = StateGraph(State)

    graph.add_node(
        "Evaluator",
        evaluator_node
    )

    graph.add_node(
        "Question_Generator",
        question_generator_node
    )

    graph.add_edge(
        START,
        "Evaluator"
    )

    graph.add_edge(
        "Evaluator",
        "Question_Generator"
    )

    graph.add_edge(
        "Question_Generator",
        END
    )

    return graph.compile()