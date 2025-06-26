from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.langchain_chain import run_chain

app = FastAPI()

class LLMRequest(BaseModel):
    task: str
    user_input: str

@app.post("/generate")
def generate_response(request: LLMRequest):
    try:
        # Basic validation
        if not request.task.strip():
            raise HTTPException(status_code=400, detail="Task cannot be empty.")
        if not request.user_input.strip():
            raise HTTPException(status_code=400, detail="User input cannot be empty.")
        
        result = run_chain(request.task, request.user_input)
        
        # Clean up result (e.g., remove stray quotes)
        cleaned = result.strip().strip('"')
        return {"result": cleaned}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
