
from utils.input_handler import handle_input
from utils.classifier import classify_input
from agents.json_agent import json_agent
from agents.email_agent import email_agent
from memory.context_store import update_context

def route(input_data):
    classification = classify_input(input_data["content"])
    update_context(input_data["content"], classification)

    if classification["format"].strip().lower() == "json":
        return json_agent(input_data["content"])
    elif classification["format"].strip().lower() == "email":
        return email_agent(input_data["content"])
    else:
        return {"status": "unsupported format"}

if __name__ == "__main__":
    sample = open("sample_email.txt", "r").read()
    input_data = handle_input(sample)
    result = route(input_data)
    print(result)
