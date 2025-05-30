
from transformers import pipeline

# Load pipelines
format_classifier = pipeline("text-classification", model="facebook/bart-large-mnli")
intent_classifier = pipeline("text-generation", model="google/flan-t5-base")

def classify_input(content):
    format_result = format_classifier(content)[0]['label']
    intent_result = intent_classifier(content + "\nIntent:", max_length=50)[0]['generated_text']
    return {
        "format": format_result,
        "intent": intent_result
    }
