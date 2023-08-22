"""Python file to serve as the frontend"""
import faiss
from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
import pickle
import bot

if __name__ == "__main__":
    bot.run_discord_bot()