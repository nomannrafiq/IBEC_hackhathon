from langchain.llms import HuggingFacePipeline
from transformers import pipeline
from torch import Tensor  


# Load a Hugging Face model and tokenizer
generator = pipeline('text-generation', model='gpt2')

llm = HuggingFacePipeline(pipeline=generator)

response = llm("What's the capital of France?")
print(response)
