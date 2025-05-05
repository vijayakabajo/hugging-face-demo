from transformers import pipeline

generator = pipeline("text-generation", device=0) 
prompt = "who is the current president of the united states?"   
output = generator(prompt, max_length=50, num_return_sequences=5, do_sample=True)


print("Outputs: ")
print(output[0]['generated_text'])
# print(output[1]['generated_text'])
# print(output[2]['generated_text'])
# print(output[3]['generated_text'])
# print(output[4]['generated_text'])   #as number of return sequences is 5



###############################################################################################


# from transformers import pipeline

# analyzer = pipeline("sentiment-analysis", device=0)  
# result = analyzer("how to hack facebook!") 

# print(result)



