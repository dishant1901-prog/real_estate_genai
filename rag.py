
from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
#from langchain.chains import RetrievalQAWithSourcesChain
#from langchain.chains.combine_documents import create_stuff_documents_chain
#from langchain.chains.retrieval import create_retrieval_chain
#from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import UnstructuredURLLoader
#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

load_dotenv()
import os
#print(os.getenv("GROQ_API_KEY"))

# Constants
CHUNK_SIZE = 1000
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
COLLECTION_NAME = "real_estate"

llm = None
vector_store = None


def initialize_components():
    global llm, vector_store

    if llm is None:
        llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),model="llama-3.3-70b-versatile", temperature=0.9, max_tokens=500)

    if vector_store is None:
        VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)
        ef = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"trust_remote_code": True}
        )

        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=ef,
            persist_directory=str(VECTORSTORE_DIR)
        )


def process_urls(urls):
    """
    This function scraps data from a url and stores it in a vector db
    :param urls: input urls
    :return:
    """
    yield "Initializing Components"
    initialize_components()

    yield "Resetting vector store...✅"
    vector_store.reset_collection()

    yield "Loading data...✅"
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    yield "Splitting text into chunks...✅"
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=CHUNK_SIZE
    )
    docs = text_splitter.split_documents(data)

    yield "Add chunks to vector database...✅"
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(docs, ids=uuids)

    yield "Done adding docs to vector database...✅"

#def generate_answer(query):
 #   if not vector_store:
  #      raise RuntimeError("Vector database is not initialized ")

   # chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vector_store.as_retriever())
    #result = chain.invoke({"question": query}, return_only_outputs=True)
    #sources = result.get("sources", "")

    #return result['answer'], sources
def generate_answer(query):
    if not vector_store:
        raise RuntimeError("Vector database is not initialized")

    retriever = vector_store.as_retriever()

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = ChatPromptTemplate.from_template(
        """
Use the following context to answer the user's question.
If the answer is not present in the context, say so.
Context:
{context}
Question:
{question}
Answer:
"""
    )

    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({
        "context": context,
        "question": query
    })

    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "")
        if source and source not in sources:
            sources.append(source)

    return answer, sources

if __name__ == "__main__":
    urls = [
        #"https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
        #"https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html"
        #"https://en.wikipedia.org/wiki/Mortgage_loan",
        #"https://en.wikipedia.org/wiki/Federal_Reserve"
        "https://www.freddiemac.com/pmms",
        "https://www.freddiemac.com/pmms/pmms-archives"
    ]

    #process_urls(urls)
    for status in process_urls(urls):
        print(status)
    answer, sources = generate_answer("Tell me what was the 30 year fixed mortagate rate along with the date?")
    print(f"Answer: {answer}")
    print(f"Sources: {sources}")
