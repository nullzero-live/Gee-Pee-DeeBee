from langchain.vectorstores import Pinecone
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def upsert(reports_chunked):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # Initialize Pinecone
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_API_ENV
    )
    #Update index name for Jai
    index_name = "sklearn-docs"

    # Upsert annual reports to Pinecone via LangChain.
    # There's likely a better way to do this instead of Pinecone.from_texts()
    for chunks in reports_chunked:
        Pinecone.from_texts([chunk.page_content for chunk in chunks], embeddings, index_name=index_name)
        
    vectorstore = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
    
    return vectorstore

def query_chain(vectorstore):
    # Create the chain
    qa = ConversationalRetrievalChain.from_llm(
        llm=OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY),
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,
    )

