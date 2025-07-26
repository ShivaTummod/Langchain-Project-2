from langchain.agents import  initialize_agent, load_tools
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
import os

#set your API key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# 1. Load the LLM
llm = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature = 0)

# 2. Load the tool(s)
tools = load_tools(["llm-match"], llm=llm)

agent= initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

response = agent.run("What is (125 * 3.14) + sqrt(256)?")
print(response)
