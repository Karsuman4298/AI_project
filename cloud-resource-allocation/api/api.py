from fastapi import FastAPI
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from optimizer.optimizer import ga_instance  

from optimizer.optimizer import ga_instance

app = FastAPI()

@app.get("/allocate")
def allocate():
    solution, _, _ = ga_instance.best_solution()
    return {"cpu": solution[0], "ram": solution[1]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
