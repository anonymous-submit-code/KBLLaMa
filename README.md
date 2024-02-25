## Source Code
This is the source code for KBllama, we propose a learn-then-reason framework for knowledge base question answering, and our end-to-end model is trained based on llama-7B.

###  Freebase KG Setup

Below steps are according to [Freebase Virtuoso Setup](https://github.com/dki-lab/Freebase-Setup). 
#### How to install virtuoso backend for Freebase KG.

1. Clone from `dki-lab/Freebase-Setup`:
```
cd Freebase-Setup
```

2. Processed [Freebase](https://developers.google.com/freebase) Virtuoso DB file can be downloaded from [Dropbox](https://www.dropbox.com/s/q38g0fwx1a3lz8q/virtuoso_db.zip)  (WARNING: 53G+ disk space is needed):
```
tar -zxvf virtuoso_db.zip
```

3. Managing the Virtuoso service:

To start service at `localhost:3001/sparql`:
```
python3 virtuoso.py start 3001 -d virtuoso_db
```

and to stop a currently running service at the same port:
```
python3 virtuoso.py stop 3001
```

A server with at least 100 GB RAM is recommended.

### Process Data
The code is shown in process data, where for benchmark dataset, we first translate the SPARQL into readable s-expression, and as for KB corpus, we generate question and logical expression pairs through GPT-3.5. We give a exmaple of data construction on Freebase corpus and WebQSP dataset.

### Freebase and WebQSP

[WebQSP](https://www.microsoft.com/en-us/research/publication/the-value-of-semantic-parse-labeling-for-knowledge-base-question-answering-2/) dataset has been downloaded under `data/WebQSP/origin`.

Run `python parse_sparql_fb.py` and the augmented data based on Freebase are saved as `data/sexpr/FB.train.json`. 

Run `python data_process.py --action merge_all --dataset WebQSP` and `python data_process.py --action merge_all --dataset WebQSP --split train` to process benchmark dataset WebQSP. 

Run `python process.py --dataset_type WebQSP --kb Freebase` to combine both benchmark dataset and generated data, which prepare data for LLM.

### Train Model
We fully fine-tuned a LLaMA-7B, and the weight is uploaded to google drive.

Here gives a training shell example for Freebase and WebQSP:

```bash
CUDA_VISIBLE_DEVICES=3 sh train_bash.sh --stage sft --model_name_or_path meta-llama/Llama-2-7b-hf --do_train  --dataset_dir LLMs/data --dataset Freebase_train 
```
## Evaluate
