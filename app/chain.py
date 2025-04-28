# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  Langchain-RPG
# FileName:     chain.py
# Description:  RAG链模块
# Author:       zhouhanlin
# CreateDate:   2025/04/29
# Copyright ©2011-2025. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_core.vectorstores import VectorStoreRetriever


def build_qa_chain(retriever: VectorStoreRetriever) -> RetrievalQA:
    llm = OllamaLLM(model="deepseek-r1:1.5b")
    prompt = PromptTemplate(
        template="""基于以下上下文回答问题：
        {context}
        问题：{question}
        答案：""",
        input_variables=["context", "question"]
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )
