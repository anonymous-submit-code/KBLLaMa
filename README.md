# Source Code
This is the source code for KBllama, we propose a learn-then-reason framework for knowledge base question answering, and our end-to-end model is trained based on llama-7B.
## Process Data
The code is shown in process data, where for benchmark dataset, we first translate the SPARQL into readable s-expression, and as for KB corpus, we generate question and logical expression pairs through GPT-3.5.
## Train Model
We fully fine-tuned a LLaMA-7B, and the weight is uploaded to google drive.
## Evaluate
