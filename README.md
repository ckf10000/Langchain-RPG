# Langchain-RPG

基于Langchain架构的文档支持库

## 部署步骤

启动Ollama服务：

```cmd
ollama pull deepseek-r1:1.5b
ollama pull nomic-embed-text
```

运行项目：

```cmd
python main.py
```



该项目完整实现了：

本地PDF文档处理
基于DeepSeek-R1的问答系统
模块化的代码结构
可扩展的RAG流程

可根据需要扩展前端界面（如使用Streamlit或Gradio）或增加更多文档类型支持
