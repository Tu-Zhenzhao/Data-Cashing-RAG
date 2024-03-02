import weaviate

"""
This setup is Python v3 compatible.
It is different from the setup in the Weaviate docs for their new Python client (Python v4).
"""
def get_client():
    """Return a client object for the current user."""
    ## Set up API keys
    auth_config = weaviate.AuthApiKey(api_key="R6Jlm7sAwhA2fx6xEjyJMyHOGTS4yjZOsS2C") # Replace w/ your Weaviate instance API key  
  
    # Instantiate the client  
    client = weaviate.Client(  
    url="https://python-plot-code-01ukjngg.weaviate.network", # Replace w/ your Weaviate cluster URL  
    auth_client_secret=auth_config,  
    additional_headers={  
                        "X-OpenAI-Api-Key": "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", # Replace with your OpenAI key  
                        }  
                             )
    return client


