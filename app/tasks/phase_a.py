import os
import json
import subprocess
from datetime import datetime
from app.utils.helpers import use_llm, get_embeddings

def task_a1(params):
    email = params["email"]
    subprocess.run(["pip", "install", "uv"])
    subprocess.run(["python", "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py", email])

def task_a2(params):
    subprocess.run(["npx", "prettier@3.4.2", "--write", "/data/format.md"])

def task_a3(params):
    with open("/data/dates.txt", "r") as f:
        dates = f.readlines()
    wednesdays = sum(1 for date in dates if datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)
    with open("/data/dates-wednesdays.txt", "w") as f:
        f.write(str(wednesdays))

# Implement tasks A4 to A10 similarly

tasks = {
    "A1": task_a1,
    "A2": task_a2,
    "A3": task_a3,
    # Add tasks A4 to A10
}
