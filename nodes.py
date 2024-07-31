from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv(), override=True) 

from langgraph.prebuilt.tool_executor import ToolExecutor 

from react import react_agent_runnable, tools 
from state import AgentState 

def run_agent_reasoning_engine(state: AgentState): # reasoning node
    agent_outcome=react_agent_runnable.invoke(state) # state has the attribute of input 
    return {"agent_outcome": agent_outcome} 

tool_executor=ToolExecutor(tools) 

def execute_tools(state: AgentState): # state should have agent_outcome fild
    agent_action=state["agent_outcome"] 
    output=tool_executor.invoke(agent_action) 
    return {"intermediate_steps": [(agent_action, str(output))]}