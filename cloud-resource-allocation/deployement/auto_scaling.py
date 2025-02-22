import requests
import os


def adjust_allocation():
    response = requests.get("http://localhost:5000/allocate")
    allocation = response.json()

    if allocation["cpu"] > 60:
        print("Scaling Up 🚀")
        os.system("kubectl scale deployment my-app --replicas=3")
    elif allocation["cpu"] < 30:
        print("Scaling Down ⬇️")
        os.system("kubectl scale deployment my-app --replicas=1")


adjust_allocation()
