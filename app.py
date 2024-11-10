import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "all_products"

# Elasticsearch connection
try:
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("elastic", "fWsN9HhvRZC+04Jajp5Q"),
        ca_certs="E:\ElasticSearch\elasticsearch-8.15.3\config\certs\http_ca.crt"
    )
except ConnectionError as e:
    st.error(f"Connection Error: {e}")

if es.ping():
    st.success("Successfully connected to Elasticsearch!")
else:
    st.error("Oops!! Cannot connect to Elasticsearch!")


# Function to perform semantic search
def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "DescriptionVector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": 500
    }
    res = es.knn_search(index=indexName, knn=query, _source=["ProductName", "Description"])
    results = res["hits"]["hits"]
    return results


# Main function to render the app UI
def main():
    # Title and layout
    st.title("🔍 Fashion Product Search")
    st.write("Search for fashion products from Myntra using semantic search powered by Elasticsearch!")

    # Search bar with a centered layout
    with st.container():
        col1, col2, col3 = st.columns([1, 6, 1])  # Create columns for better centering
        with col2:
            search_query = st.text_input("Enter your search query", placeholder="e.g., 'summer dresses'")

    # Search button triggers the search
    if st.button("Search"):
        if search_query:
            with st.spinner("Searching for products..."):
                results = search(search_query)

            # Display the results if available
            if results:
                st.subheader("Search Results")
                for result in results:
                    if '_source' in result:
                        with st.container():
                            st.markdown("---")
                            # Display the product name
                            st.markdown(f"### {result['_source'].get('ProductName', 'No Product Name')}")
                            # Display the product description
                            st.write(f"**Description:** {result['_source'].get('Description', 'No Description')}")
            else:
                st.warning("No results found. Try a different query.")
        else:
            st.warning("Please enter a search query.")


# Run the app
if __name__ == "__main__":
    main()
