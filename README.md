# Sentiment Analisys POC

## Idea
The goal of this project is to implement a small API that using AI capabilities is able to determine the sentiment of a given text.

## Stack
Tech stack currently being used :

-Poetry
-Fast-API

## Architecture
The design architecture and structure is based on Hexagonal Architecture. 
The main reasons are the flexibility on exchanging services without impacting or having a minimal impact on implementation and also the scalability in order to add new features.

sentiment-analysis/
├── app/                     # Application Layer
│   ├── services.py          # Core business logic (orchestrates domain and adapters)
│   ├── __init__.py          # Makes `app` a Python package
│
├── domain/                  # Domain Layer
│   ├── interfaces.py        # Defines interfaces for SentimentAnalyzer
│   ├── __init__.py          # Makes `domain` a Python package
│
├── adapters/                # Adapters Layer
│   ├── transformers.py      # Adapter for Transformers library
|   ├── interfaces.py        # Abstract interfaces
│   ├── __init__.py          # Makes `adapters` a Python package
│
├── infrastructure/          # Infrastructure Layer
│   ├── dependency_injection.py # Instantiates and injects dependencies
│   ├── __init__.py          # Makes `infrastructure` a Python package
│
├── main.py                  # Entry point for the application (FastAPI endpoint)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Ignored files for Git



