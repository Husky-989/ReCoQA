# ReCoQA: A Benchmark for Tool-Augmented and Multi-Step Reasoning in Real Estate Question and Answering

**This work has been accepted as the Main Conference of ACL 2026.**

---

This repository contains the benchmark and source code released for the paper "ReCoQA: A Benchmark for Tool-Augmented and Multi-Step Reasoning in Real Estate Question and Answering".

<img src="figures\overall.png">

ReCoQA is the first large-scale benchmark for tool-augmented and multi-step reasoning in real estate question answering. It comprises 29,270 question-answer pairs featuring hybrid workflows that combine structured database querying with external API calls.

This dataset poses unique challenges for question answering due to its heterogeneous integration requirements, dynamic geospatial computations, and complex multi-step reasoning chains. To address these challenges, the paper also introduces the HIRE-Agent framework, which implements a hierarchical understand–plan–execute architecture coordinating specialized agents for intent parsing, task orchestration, and tool execution to enhance multi-source reasoning accuracy.

## Requirements and Installation
First, you need to install the [PostgreSQL database](https://www.postgresql.org/download/) based on your operating system and follow the settings below
```
user='postgres' 
password='1234'
port='5432' (default)
```
You can also use your own username and password, but you need to **update them** in `database\CreatDatabase.ipynb` and `HIRE_Agent\DatabaseUtils.py`

Then, install the necessary Python packages
```
pip install -r requirements.txt
```
## Usage

### Read and Import Tables
- First, you need read all the tables located in the `tables` directory, and import them into the newly created database. Run the code `database\CreatDatabase.ipynb` to complete the database setup.

### Train the BERT Model
- Download the [BERT weight files](https://huggingface.co/google-bert/bert-base-chinese) and store them in the `model` directory.
- Run the code `BERT-fine-tune.ipynb` to complete the database setup.
- After running all the cells successfully, the BERT predicted results will be saved in the `results` directory.

### Run the HIRE-Agent
We provide two methods as the baseline:
- `HIRE_Agent\HIRE_Agent(FT).ipynb` applies the BERT model as the Front-end Agent to predict the intent and slots.
- `HIRE_Agent\HIRE_Agent(ICL).ipynb` applies the LLM as the Front-end Agent and uses ICL to predict the intent and slots.

## Contact Us
If you have any questions regarding the project's code or dataset, please feel free to contact me at yindongzhang@uic.edu.cn.

## Citation
If you find this work useful for you, please cite it and we will update the arxiv link soon.

## Acknowledgements
The acquisition of real estate data is supported by [Elmleaf Ltd.(Shanghai)](https://www.elmleaf.com.cn/dataset).
