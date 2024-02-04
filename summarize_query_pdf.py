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





llm=  OpenAI(temperature=0.2)

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

query='Which frequency is analysed?'
index.query(query)


