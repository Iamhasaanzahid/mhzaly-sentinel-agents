from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI(title="MHZALY Sentinel Agents API")

# Enable CORS so frontend can communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskRequest(BaseModel):
    task: str
    apiKey: str = None

@app.get("/")
def home():
    return {"status": "MHZALY Sentinel Core is Online", "agents": ["Manager", "SOC Analyst", "Executor"]}

@app.post("/run-workflow")
def run_workflow(req: TaskRequest):
    if not req.task.strip():
        raise HTTPException(status_code=400, detail="Task cannot be empty.")
    
    # Simulating multi-agent virtual office execution steps
    time.sleep(1)
    step1 = f"[Manager Agent]: Received task '{req.task}'. Delegating sub-tasks..."
    
    time.sleep(1)
    step2 = f"[SOC Sub-Agent]: Performing security triage, log checks, and threat analysis..."
    
    time.sleep(1)
    step3 = f"[Execution Sub-Agent]: Compiled final defense strategy and action report successfully."
    
    return {
        "status": "success",
        "logs": [step1, step2, step3],
        "summary": "All office sub-agents completed their designated operations."
    }
