
import os

from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    VisitWebpageTool,
    InferenceClientModel
)


# Get Hugging Face token
hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise RuntimeError("HF_TOKEN environment variable is not set.")


# Create model
model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=hf_token
)


# Create tools
search_tool = DuckDuckGoSearchTool()
webpage_tool = VisitWebpageTool()


# Create research agent
agent = CodeAgent(
    tools=[search_tool, webpage_tool],
    model=model
)


# Get user's research question
question = input("I am JEFF, What would you like me to research? ")


# Run the agent
result = agent.run(question)


# Display result
print("\nResearch Result:")
print(result)
