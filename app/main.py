from fastapi import FastAPI, HTTPException
from app.agent import Agent
import os

app = FastAPI()
agent = Agent()

@app.post("/run")
async def run_task(task: str):
    try:
        result = agent.execute_task(task)
        return {"status": "success", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str):
    try:
        if not path.startswith("/data/"):
            raise ValueError("Access denied. Only files in /data/ directory are accessible.")
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
