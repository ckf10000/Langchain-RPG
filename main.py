# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  Langchain-RPG
# FileName:     main.py
# Description:  TODO
# Author:       zhouhanlin
# CreateDate:   2025/04/29
# Copyright ©2011-2025. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from app.loader import load_pdf
from app.chain import build_qa_chain
from app.splitter import split_document
from app.embeddings import create_vector_store


# 1. 加载文档

docs = load_pdf("data/demo.pdf")

# 2. 分割文本
splits = split_document(docs=docs)

# 3. 创建向量存储
vector_store = create_vector_store(splits)

# 4. 构建QA链
qa_chain = build_qa_chain(vector_store.as_retriever())

# 5. 测试查询
result = qa_chain.invoke({"query": "文档的主要内容是什么？"})

print(result["result"])