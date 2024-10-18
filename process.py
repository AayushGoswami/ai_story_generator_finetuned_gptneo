import torch
from transformers import pipeline

def load_model():
    # Check if GPU is available
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load the pipeline with the model
    model = pipeline('text-generation', model='a-g-2000/gpt-neo-2.7B-tiny_skspr_finetuned', device=0 if device == "cuda" else -1)
    return model, device

def generate_story(model, user_input, max_length, num_sequences):
    response = model(user_input, max_length=max_length, num_return_sequences=num_sequences)
    return response
