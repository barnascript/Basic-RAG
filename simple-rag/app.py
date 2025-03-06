import streamlit as st
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from duckduckgo_search import DDGS
from pytube import Search
import requests

# This is to check if secret keys are available
if "OPENAI_API_KEY" not in st.secrets or "OMDB_API_KEY" not in st.secrets:
    st.error("API keys are missing. Please add them to the `.streamlit/secrets.toml` file.")
    st.stop()

# Setting up the RAG agent
def setup_rag_agent():
    llm = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    loader = WebBaseLoader("https://en.wikipedia.org/wiki/Movie")
    index = VectorstoreIndexCreator().from_loaders([loader])
    rag_agent = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=index.vectorstore.as_retriever()
    )
    return rag_agent

# This function will search the web using DuckDuckGo
def search_web(query):
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
    return results

# This will also search YouTube for trailers
def search_youtube(query):
    search = Search(query)
    if search.results:
        return search.results[0].watch_url  
    return "No trailer found."

# Get movie information using OMDB API
def get_movie_info(movie_name):
    api_key = st.secrets["OMDB_API_KEY"]
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(url).json()
    
    if response.get("Response") == "True":
        return {
            "Title": response.get("Title"),
            "Year": response.get("Year"),
            "IMDB Rating": response.get("imdbRating"),
            "Release Date": response.get("Released"),
            "Plot": response.get("Plot")
        }
    else:
        return "Movie not found."

# The Streamlit app itself
def main():
    st.title("🎬 Movie/Series Information and Web Search")
    st.write("This app retrieves information about movies/series, provides YouTube trailer links, and allows general web searches.")

    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Dropdown to choose search type
    search_type = st.selectbox(
        "What would you like to search for?",
        ("Movie/Series Information", "General Web Search")
    )

    # User input
    user_input = st.text_input("Enter your query:", placeholder="e.g., Inception or Python programming")

    if st.button("Search"):
        if user_input:
            
            st.session_state.messages = []
            # Add user input to session messages
            st.session_state.messages.append(f"👤 User: {user_input}")

            if search_type == "Movie/Series Information":
                # Get movie info
                movie_info = get_movie_info(user_input)
                st.session_state.messages.append(f"🎥 Movie Info: {movie_info}")

                # Search YouTube for trailer
                trailer_link = search_youtube(f"{user_input} trailer")
                st.session_state.messages.append(f"🎬 Trailer Link: {trailer_link}")

            elif search_type == "General Web Search":
                # Perform a general web search
                web_results = search_web(user_input)
                st.session_state.messages.append("🌐 Web Search Results:")
                for result in web_results:
                    st.session_state.messages.append(f"- {result['title']}: {result['href']}")

    # Display session messages
    st.subheader("Session Messages")
    for message in st.session_state.messages:
        st.write(message)

    # Display movie info and trailer link (if applicable)
    if "movie_info" in locals() and search_type == "Movie/Series Information":
        st.subheader("Movie Information")
        st.json(movie_info)

        st.subheader("YouTube Trailer")
        st.video(trailer_link)

    # Display web search results (if applicable)
    if "web_results" in locals() and search_type == "General Web Search":
        st.subheader("Web Search Results")
        for result in web_results:
            st.write(f"- [{result['title']}]({result['href']})")

# Run the app
if __name__ == "__main__":
    main()