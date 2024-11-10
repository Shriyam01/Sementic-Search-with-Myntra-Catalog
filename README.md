# Sementic-Search-with-Myntra-Catalog
This repository contains the source code for a Natural Language Processing project utilizing the 'all-mpnet-base-v2' model. The project focuses on implementing semantic search in the Myntra catalog through vector embeddings.

Project Title: Product Search with Elasticsearch
Introduction:

This project aims to build a product search engine using Elasticsearch and Sentence Transformers. The system is designed to help users search for products from a catalog by entering a keyword. The backend uses Elasticsearch to store product data and perform fast, efficient searches. Sentence Transformers is used to generate dense vector representations of product descriptions, enabling semantic similarity search.
Features:

    Vector-based product search using Elasticsearch.
    Fast retrieval of top-k relevant products.
    Use of Sentence Transformers for converting descriptions into vectors.

Setup:

    Install necessary dependencies.
    Set up Elasticsearch and start it locally.
    Load product data and create an index in Elasticsearch.
    Implement search functionality to retrieve similar products.

Technologies Used:

    Elasticsearch: For indexing and searching the product data.
    Sentence Transformers: For converting product descriptions into vector representations.
    Pandas: For handling and processing the product data.

Requirements

    Elasticsearch (local setup)
    Sentence Transformers
    Pandas

Requirements

To run the project, you will need to install the following Python packages:

    elasticsearch: For interacting with the Elasticsearch engine.
    pandas: For handling product data.
    sentence_transformers: For generating vector embeddings for product descriptions.

You can install these dependencies using pip:

pip install elasticsearch pandas sentence_transformers
