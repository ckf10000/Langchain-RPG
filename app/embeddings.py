# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  Langchain-RPG
# FileName:     embeddings.py
# Description:  向量存储模块
# Author:       zhouhanlin
# CreateDate:   2025/04/29
# Copyright ©2011-2025. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from typing import List
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


def create_vector_store(docs: List[Document]) -> Chroma:
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma.from_documents(documents=docs, embedding=embeddings)
