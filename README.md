# `lawson`

Building a legal document retrieval agent.

## Overview
`lawson` is a Retrieval-Augmented Generation (RAG) system designed for efficient and accurate retrieval of legal documents. The system combines state-of-the-art retrieval techniques with advanced natural language processing models to provide precise and contextual responses to legal queries.

## Features
- **Efficient Document Retrieval**: Utilizes a scalable search mechanism to handle large volumes of legal documents.
- **Contextual Understanding**: Employs NLP models to interpret legal language and provide relevant results.
- **Customizable**: Adaptable to specific legal domains and jurisdictions.
- **User-Friendly**: Simple and intuitive interface for querying and viewing results.

## Architecture
The `lawson` system is built around the following components:
- **Retriever**: Finds relevant documents from the corpus based on user queries.
- **Reader**: Extracts and synthesizes information from retrieved documents to answer specific questions.
- **Knowledge Base**: A curated collection of legal documents, statutes, and case law.
- **Frontend Interface**: Allows users to interact with the system via text-based or graphical input.

### Back-end
The back-end is responsible for:
- Managing the knowledge base and vector store.
- Handling user queries and orchestrating retrieval and generation processes.
- Serving API endpoints for the AI inference and front-end components.

### Front-end
The front-end provides:
- An intuitive interface for users to input queries and view results.
- Visualizations of retrieved documents and generated responses.
- Configuration options for customizing the system’s behavior.

### AI Backbone

#### Vector Store
The vector store is a high-performance database for storing and retrieving document embeddings. It enables efficient similarity searches and ensures fast query responses.

#### Dataset
The dataset comprises:
- Legal statutes, regulations, and case law.
- User-provided documents or domain-specific texts.
- Pre-processed and indexed for optimal retrieval performance.

#### AI Inference Endpoints

**Required**
- **Document Retrieval Endpoint**: Accepts a query and returns the most relevant documents from the knowledge base.
- **Answer Generation Endpoint**: Synthesizes answers from retrieved documents.

**Additional**
- **Summarization Endpoint**: Generates concise summaries of legal texts.
- **Custom Query Tuning Endpoint**: Allows users to fine-tune retrieval parameters or adapt the model to specific legal domains.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ethereoh/lawson.git
   cd lawson
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your knowledge base by indexing your legal document corpus. Refer to the documentation for details.

**Note**
- For those who want to try `uv`, instructions are left at [here](assets/UV_SETUP.md). 

## Usage
1. Start the application:
   ```bash
   fastapi dev lawson/main.py --port 8001 --host 0.0.0.0
   ```
2. Open your browser and navigate to `http://localhost:8001` to interact with `lawson`.
3. Input your legal queries and view the results.

## Acknowledgments
- Inspired by advancements in AI and legal technology.
- Thanks to contributors and the open-source community for their support.
