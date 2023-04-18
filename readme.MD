

# Introduction
  

This repository contains code and data for my article "[Learn Japanese Onomatopoeia with Neo4j](https://dgg32.medium.com/learn-japanese-onomatopoeia-with-neo4j-a7306c7933ec)". The chatbot is an adaptation from Tomaz Bratanic's [Context-Aware Knowledge Graph Chatbot With GPT-4 and Neo4j](https://medium.com/neo4j/context-aware-knowledge-graph-chatbot-with-gpt-4-and-neo4j-d3a99e8ae21e). A big thank to Tomaz.

1. The scripts are for data download, formatting and the chatbot.

2. The  data folder contains the CSV downloaded from the JapanDict and Onomato Project.
  

# Prerequisite

Neo4j Desktop or AuraDB

Gemini Cloud account

OpenAI account
  

# Run
1. run download_onomatopoeic.ipynb to download the vocabulary data. The data nodes_with_examples_final.csv is also included in the data folder
  
2. run onomatopoeia_embedding.ipynb to run the ada-002 embedding, cosine similarity and format the nodes. The output data are nodes(1).csv and edge(1).csv in the data folder 

3. Import the data into Aura/Gemini Cloud

4. Set up the chatbot. Set up a conda environment (requirements.txt) and run the chatbot:

```console
 streamlit run chatbot.py
```

## Authors

  

*  **Sixing Huang** - *Concept and Coding*

  

## License

  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
