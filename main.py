from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
from dotenv import load_dotenv
import os
import datetime

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# --- Enable CORS for local dev and Streamlit compatibility ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origins like ["http://localhost:8501"] in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Define request schema ---
class QueryRequest(BaseModel):
    question: str

# --- Endpoint to handle travel planning queries ---
@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(f"Received query: {query.question}")

        # Build the agentic workflow graph
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        # Save the graph visualization as PNG (for debugging or display)
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)
        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")

        # Create message input format
        messages = {"messages": [query.question]}

        # Invoke the agent with messages
        output = react_app.invoke(messages)

        # Extract the final AI message
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}

    except Exception as e:
        print(f"Error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
