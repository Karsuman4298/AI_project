import requests
import os


def adjust_allocation():
    try:
        response = requests.get("http://127.0.0.1:5000")
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        allocation = response.json()  # Attempt to parse the response as JSON

        # Safely check if the key "cpu" exists in the allocation dictionary
        if "cpu" not in allocation:
            print("Error: 'cpu' key not found in the server response.")
            return  # Exit the function gracefully

        # Perform scaling based on the "cpu" value
        if allocation["cpu"] > 60:
            print("Scaling Up 🚀")
            os.system("kubectl scale deployment my-app --replicas=3")
        elif allocation["cpu"] < 30:
            print("Scaling Down ⬇️")
            os.system("kubectl scale deployment my-app --replicas=1")
        else:
            print("CPU usage is optimal. No scaling needed.")
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except ValueError:
        print("Error: Unable to decode JSON from the server response.")


adjust_allocation()
