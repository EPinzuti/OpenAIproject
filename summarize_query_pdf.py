# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:35:04 2024

@author: edoardo
"""
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from langchain import OpenAI, PromptTemplate
import glob
import openai


#setx OPENAI_API_KEY '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'

#openai.api_key=APIKEY

#api_key='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'
from openai import OpenAI


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)





llm=  OpenAI(temperature=0.2)#(model="gpt-4"

def summarize_pdfs_from_folder(pdfs_folder):
    
    summaries=[]
    for pdf_file in glob.glob(pdfs_folder+ "\\*.pdf"):
        loader=PyPDFLoader(pdf_file)
        docs=loader.load_and_split()
        chain=load_summarize_chain(llm,chain_type='map_reduce') 
        summary=chain.run(docs)
        print("Summary for:",pdf_file)
        print(summary)
        print("\n")
        summaries.append(summary)
        
    return summaries


summaries=summarize_pdfs_from_folder("C:\\Users\\edoardo\\Desktop\\PhD_thesis\\hdm_gonogo\\pdf")

with open("summaries.txt",'w') as f:
    for summary in summaries:
        f.wrote(summary + "\n"*3)


# QUERY MULTIPLE PAPAPERS ##

from langchain.indexes import VectorstoreIndexCreator 
from langchain.document_loaders import PyPDFDirectoryLoader



loader=PyPDFLoader("C:\\Users\\edoardo\\Desktop\\PhD_thesis\\hdm_gonogo\\pdf")
docs=loader.load()

index=VectorstoreIndexCreator().from_loaders([loader]) 

query=''
index.query(query)


