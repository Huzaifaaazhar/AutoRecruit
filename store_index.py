from src.helper import extract_resume_text, embedding_model, text_split
from pinecone import Pinecone
from langchain.vectorstores import Pinecone as PineconeStores
from dotenv import load_dotenv
import os

load_dotenv()

#Setting up Pinecone API KEY
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

#Getting the PDFs
data_folder_path = 'G://Auto Recruit AI//data'
resumes_df = extract_resume_text(data_folder_path)

#Dividing into chunks
chunks = text_split(resumes_df)

#Downloading embedding model.
embedding = embedding_model()

# Initialize Pinecone instance
pc = Pinecone(
        api_key=PINECONE_API_KEY
    )

index_name="recruit"

docsearch = PineconeStores.from_existing_index(index_name, embedding)