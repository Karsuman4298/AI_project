from fastapi import FastAPI, WebSocket, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import asyncio
import random
import numpy as np
from optimizer.optimizer import ga_instance  # Genetic Algorithm for allocation

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve static files (JS, CSS, images)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Simulated cloud resources
cloud_resources = {
    "cpu": 100,  # Total available CPU in %
    "ram": 256,  # Total RAM in MB
    "storage": 1000,  # Storage in MB
    "network": 1000,  # Bandwidth in Mbps
}

file_allocations = []  # Store allocated resources for each file


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
    priority = random.randint(1, 10)  # Assign priority randomly

    file_allocations.append({
        "filename": file.filename,
        "size": round(file_size, 2),
        "priority": priority,
        "allocated": False
    })

    return {"message": f"File '{file.filename}' uploaded successfully!"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        solution, _, _ = ga_instance.best_solution()
        allocated_files = heuristic_allocate_files(solution)
        await websocket.send_json({
            "cpu": round(solution[0], 2),
            "ram": round(solution[1], 2),
            "files": allocated_files
        })
        await asyncio.sleep(2)  # Update every 2 seconds


def heuristic_allocate_files(solution):
    allocated_files = []
    available_cpu, available_ram = solution[0], solution[1]

    for file in sorted(file_allocations, key=lambda f: f["priority"], reverse=True):
        if file["size"] < available_ram:
            file["allocated"] = True
            available_ram -= file["size"]
            allocated_files.append(file)
        else:
            file["allocated"] = False  # Not enough RAM
    return allocated_files


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)
