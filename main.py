from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph

from nodes import execute_tools, run_agent_reasoning_engine
from state import AgentState

AGENT_REASON = "agent_reason"
ACT = "act"


def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    else:
        return ACT


graph = StateGraph(AgentState)

graph.add_node(AGENT_REASON, run_agent_reasoning_engine)
graph.set_entry_point(AGENT_REASON)
graph.add_node(ACT, execute_tools)

graph.add_conditional_edges(AGENT_REASON, should_continue)

graph.add_edge(ACT, AGENT_REASON)

app = graph.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph_illustration.png")

if __name__ == "__main__":
    print("Hello ReAct with LangGraph")

    response = app.invoke(
        input={
            "input": "What is the weather in San Francisco? List it and then triple it."
        }
    )

    print(response)
    print("-" * 50)
    print(response["agent_outcome"].return_values["output"])
