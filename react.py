from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

from langchain import hub
from langchain.agents import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

react_prompt: PromptTemplate = hub.pull("hwchase17/react")

@tool 
def triple(num: float) -> float: 
    """_summary_

    Args:
        num (float): input float value

    Returns:
        float: tripled input float value (multiplied by 3)
    """
    
    tripled_num=3*float(num) 
    
    return tripled_num

tools=[TavilySearchResults(max_results=1), triple]