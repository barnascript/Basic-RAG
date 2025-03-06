# Basic RAG System with Search and Movie Trailer Capabilities

This project implements a Retrieval-Augmented Generation (RAG) system with search capabilities using Python and Streamlit. The app allows users to:

Retrieve information about movies/series (e.g., title, release date, IMDB rating, plot) using the OMDB API.
Fetch YouTube trailer links for movies/series using pytube.
Perform general web searches using DuckDuckGo.
Display session messages for the current search activity.
The app is built with Streamlit for the user interface and integrates multiple APIs and libraries to provide a seamless experience.

## Features

1. Movie/Series Information

Users can search for a movie or series by name.
The app retrieves details such as:
Title
Release year
IMDB rating
Release date
Plot summary
A YouTube trailer link is also provided.
2. General Web Search

Users can perform general web searches.
The app displays the top 5 search results with titles and links.
3. Session Messages

The app displays a log of the current search activity, including:
User input
Movie information (if applicable)
YouTube trailer link (if applicable)
Web search results (if applicable)
4. Streamlit GUI

The app features a clean and interactive user interface built with Streamlit.
Users can choose between Movie/Series Information and General Web Search using a dropdown menu.
Approach

## 1. RAG System

The RAG system is built using LangChain.
A RetrievalQA chain is used to retrieve information from a document (in this case, a Wikipedia page about movies).
The system is powered by OpenAI's GPT model for generating responses.
2. Search Integrations

OMDB API: Used to fetch movie/series information.
DuckDuckGo Search: Used for general web searches.
YouTube Search: Implemented using pytube to fetch trailer links.
3. Streamlit App

The app is built using Streamlit, a Python framework for creating web apps.
The interface includes:
A dropdown menu to select the search type.
A text input field for user queries.
A "Search" button to trigger the search.
A section to display session messages and search results.
4. Session Management

The app uses Streamlit's session_state to manage session messages.
Session messages are reset at the start of each search to ensure only the current activity is displayed.
Setup

1. Install Dependencies

Install the required Python libraries:

pip install streamlit langchain openai duckduckgo-search pytube requests
2. Add API Keys

Create a .streamlit/secrets.toml file in your project directory and add your API keys:

 .streamlit/secrets.toml
OPENAI_API_KEY = "your-openai-api-key"
OMDB_API_KEY = "your-omdb-api-key"
Replace your-openai-api-key and your-omdb-api-key with your actual API keys.

3. Run the App

Run the app using the following command:

streamlit run app.py
Usage

Select Search Type:

Choose between Movie/Series Information and General Web Search using the dropdown menu.
Enter Query:

For Movie/Series Information, enter the name of a movie or series (e.g., "Inception").
For General Web Search, enter any search query (e.g., "Python programming").
View Results:

For Movie/Series Information, the app will display:
Movie details (title, release date, IMDB rating, etc.).
A YouTube trailer link.
For General Web Search, the app will display the top 5 web search results.
Session Messages:

The app will display a log of the current search activity in the "Session Messages" section.
Example Workflow

## Movie/Series Search

Select Movie/Series Information from the dropdown.
Enter a movie name like "Inception".
The app will display:
Movie information (title, release date, IMDB rating, etc.).
A YouTube trailer link.
General Web Search

Select General Web Search from the dropdown.
Enter a query like "Python programming".
The app will display the top 5 web search results with titles and links.
Notes

Ensure the secrets.toml file contains valid API keys for OpenAI and OMDB.
The app resets session messages at the start of each search to ensure only the current activity is displayed.
For production, consider adding error handling and asynchronous programming for better performance.
Future Enhancements

Expand Search Capabilities:
Add more search integrations (e.g., Google Search, Bing Search).
Improve UI:
Add more interactive elements (e.g., buttons, dropdowns).
Support for More Media Types:
Extend the app to support TV shows, books, and other media types.
