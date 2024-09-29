from flask import Flask, render_template, jsonify, request
from src.helper import embedding_model
from src.prompt import prompt_template
from langchain_community.vectorstores import Pinecone as PineconeStores
from pinecone import Pinecone
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

#Setting up Pinecone API KEY
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

#Downloading embedding model.
embedding = embedding_model()

print(f"Pinecone API Key: {PINECONE_API_KEY}")


# Initialize Pinecone instance
pc = Pinecone(
        api_key=PINECONE_API_KEY
    )
index_name="recruit"
docsearch = PineconeStores.from_existing_index(index_name, embedding)

print(f"Pinecone index {index_name} loaded successfully")

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

try:
    llm = CTransformers(model="G://Auto Recruit AI//model//llama-2-7b-chat.ggmlv3.q4_0.bin",
                        model_type="llama",
                        config={'max_new_tokens':500, 'temperature':0.4}
                        )
    print("Model loaded successfully")

except Exception as e:
    print(f"Error loading model: {e}")

qa = RetrievalQA.from_chain_type(llm=llm,
                                 chain_type='stuff',
                                 retriever=docsearch.as_retriever(search_kwargs={'k':2}),
                                 return_source_documents=True,
                                 chain_type_kwargs=chain_type_kwargs)


@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    try:
        msg = request.form["msg"]
        input = msg
        print(input)
        result = qa.invoke({"query":input})
        print("Raw response:", result)
        response_text = result.get("result", "No response found")
        print("Response:", response_text)
        print("Response:", result["result"])
        return str(result["result"])
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while processing the request."}), 500



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug=True)