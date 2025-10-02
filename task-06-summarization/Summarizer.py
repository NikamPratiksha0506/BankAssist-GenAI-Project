import os
from config import SAMPLE_DOCS_PATH, GEMINI_API_KEY

# Document loaders
from langchain_community.document_loaders import PyPDFLoader, TextLoader

# Chains and prompts
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
#from langchain.chains.combine_documents import MapReduceDocumentsChain
from langchain.chains import AnalyzeDocumentChain, LLMChain
from langchain.prompts import PromptTemplate

# Google GenAI LLM (correct import)
from langchain_google_genai import ChatGoogleGenerativeAI

# Load documents
documents = []
for filename in os.listdir(SAMPLE_DOCS_PATH):
    file_path = os.path.join(SAMPLE_DOCS_PATH, filename)
    if filename.lower().endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())
    elif filename.lower().endswith(".txt"):
        loader = TextLoader(file_path)
        documents.extend(loader.load())

# Initialize Google GenAI LLM
#llm = ChatGoogleGenerativeAI(api_key=GEMINI_API_KEY)
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",   # required field
    api_key=GEMINI_API_KEY    # your API key from config
)

# Prompt template
prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following document:\n\n{text}\n\nSummary:"
)

# MapReduce chain
summarize_chain = MapReduceDocumentsChain(
    llm_chain=LLMChain(llm=llm, prompt=prompt)
)

# Run summarization
summary = summarize_chain.run(documents)

# Output summary
print("\n📄 Summary of all documents:\n")
print(summary)
