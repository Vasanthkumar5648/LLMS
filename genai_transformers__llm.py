# -*- coding: utf-8 -*-
"""GenAI_Transformers__LLM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gnOik8gcamKqm5IE-Cu3CoW6DMvWTZ1z

Exploring Hugging Face Pretrained Models for Text Generation, Summerization & Translation
"""

!pip install transformers

!pip install transformers datasets

"""Text Generation

## Text Generation using GPT-2 Model

- Let's use the provided codes in model card at Huggingface to explore how GPT-2 Model works

- can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, we set a seed for reproducibility:
"""

from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(40)

generator("Hello, I'm language model,",max_length=30, num_return_sequences=5)

"""Limitations and bias"""

from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generator('The White man worked as a', max_length=35,num_return_sequences=15)

"""## Text Generation using GPT2-XL Model

**Important**
- Do not run the cell for GPT2-XL Model if your system has RAM less than 12GB
- The size of the Flan-T5 Base LLM is more than 6.5GB

"""

from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2-xl')
set_seed(42)
generator("hello i'm a language model,", max_length=30, num_return_sequences=5)

generator("Hello i'm A Language Model,",max_length=40,num_return_sequences=10)

"""Text Generation with GPT-2"""

from transformers import pipeline

model_name = "gpt2"
prompt = "Long Long ago , there is a village...."

generator = pipeline("text-generation", model=model_name)

generated_text = generator(prompt, max_length=600)

print(generated_text)

"""  #### **SentencePiece Libray:**

  - A powerful and efficient text processing library for NLP tasks. It provides subword segmentation, vocabulary management, and multilingual support. SentencePiece improves model performance, reduces memory footprint, and enables multilingual applications. It's a vital tool for large language models, machine translation, text summarization, chatbots, and text analysis.

"""

!pip install sentencepiece
import sentencepiece
print(sentencepiece.__version__)

"""#### Flan-T5
- T5, short for "Text-to-Text Transfer Transformer," is a powerful Large Language Model (LLM) developed by Google AI. It is based on the Transformer architecture and utilizes a novel text-to-text approach to perform a wide range of natural language processing (NLP) tasks.
"""

from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer =T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

input_text = "translate English to tamil:How old are you?"
input_ids = tokenizer(input_text,return_tensors="pt").input_ids

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))

"""##### The conversation used in below codes are taken from hugging face library dataset

- Dataset Name: [knkarthick/dialogsum ](https://huggingface.co/datasets/knkarthick/dialogsum/viewer/default/train)
"""

input_conversation = '''
#person1#:Look! This picture of mom in her cup and gown.
#person2#:Isn't it lovely! That's when she got her Master's Degree from Miami University.
#Person1#: Yes, we are very proud of her.
#Person2#: Oh, that's a nice one of all of you together. Do you have the negative? May I have a copy?
#Person1#: Surely, I'll have one made for you. You want a print? #Person2#: No. I'd like a slide, I have a new projector.
#Person1#: I'd like to see that myself. #Person2#: Have a wallet size print made for me, too. #Person1#: Certainly.
'''

Baseline_human_summary = '#person2# thinks the picture is lovely and asks #person1# to give a slide and a wallet_size print.'

input_conversation = "summarize:"+input_conversation
input_ids = tokenizer(input_conversation, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
Model_summary = tokenizer.decode(outputs[0])

print("-"*100)
print('Baseline human summary:',Baseline_human_summary)
print("-"*100)
print("Model Summary:", Model_summary)

