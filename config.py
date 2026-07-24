import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

if os.environ["GOOGLE_API_KEY"]:
    print("API key is set")



embedding_model = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2-preview")

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature = 0)