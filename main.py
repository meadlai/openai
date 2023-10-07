from langchain.document_loaders import OutlookMessageLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import AzureOpenAI
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA

import os
# import nltk
# nltk.download('punkt')

## https://blog.nillsf.com/index.php/2023/07/08/how-to-configure-langchain-to-use-azure-openai-in-python/

depoymentName = 'tortoise-test'
modelName = 'text-embedding-ada-002'

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"
os.environ["OPENAI_API_BASE"] = "https://tortoise-openai-001.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "26b77bffb0cc4b729a6cd646123ff023"

##
os.environ["OPENAI_DEPLOYMENT_NAME"] = depoymentName
# os.environ["OPENAI_DEPLOYMENT_VERSION"] = "1"
os.environ["OPENAI_MODEL_NAME"] = modelName
azureOpenAI = AzureOpenAI(deployment_name=depoymentName)



# print(azureOpenAI("hi"))


emailLoader = DirectoryLoader('D:\\project\\data', glob='**/*.msg', show_progress=True, loader_cls=OutlookMessageLoader)
documents = emailLoader.load()

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
split_docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
docSearch = Chroma.from_documents(split_docs, embeddings)

qa = RetrievalQA.from_chain_type(llm=azureOpenAI, chain_type="stuff",retriever= docSearch.as_retriever(), return_source_documents= True)
result = qa({{"query":"我一共有多少订单？"}})
print(result)