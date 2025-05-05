from transformers import pipeline

# Load a text-generation pipeline (uses GPT-2 by default)
generator = pipeline("text-generation", device=0)  # Use device=0 for GPU, device=-1 for CPU

# Generate text
prompt = "who is the current president of the united states?"   
output = generator(prompt, max_length=50, num_return_sequences=1)

print("Prompt:", prompt)
print("Generated text:")
print(output[0]['generated_text'])
