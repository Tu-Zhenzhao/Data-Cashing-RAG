import json
from client_setup import get_client
import unittest


def perform_vector_search(concepts, properties=["answer", "prompt"], limit=3):
    """
    Perform vector search on the database.
    """
    ## Vector Search
    client = get_client()
    response = client.query.get("DSCode", properties)\
            .with_additional(["id", "distance"])\
            .with_near_text({"concepts": concepts})\
            .with_limit(limit)\
            .do()


    print(json.dumps(response, indent=2))

def keyword_search(keyword, properties=["material", "su", "sy"], limit=5):
    """
    Perform keyword search on the database.
    """
    ## Keyword Search
    client = get_client()
    response = (client.query.get("Material", properties)\
            .with_additional("id")\
            .with_bm25(
                    query=keyword,
            )\
            .with_where({
                "path": ["su"],
                "operator": "GreaterThan",
                "valueInt": "580",
            })\
            .with_where({
                "path": ["su"],
                "operator": "LessThan",
                "valueInt": "590",
            })\

            .with_limit(limit)\
            .do()
    )
    print(json.dumps(response, indent=2))

# hybrid search
def hybrid_search(keyword, properties=["material", "su", "sy"], limit=5):
    """
    Perform hybrid search on the database.
    Alpha 1 is pure vector search, alpha 0 is pure keyword search.
    """
    ## Hybrid Search
    client = get_client()
    response = (client.query.get("Material", properties)\
            .with_additional("id")\
            .with_hybrid(
                    query=keyword,
                    alpha=0.8,
            )\
            .with_where({
                "path": ["su"],
                "operator": "GreaterThan",
                "valueInt": 580,
            })\
            .with_where({
                "path": ["su"],
                "operator": "LessThan",
                "valueInt": 590,
            })\
            .with_limit(limit)\
            .do()
    )
    print(json.dumps(response, indent=2))



## Question Search
def question_search(questions, properties=["material", "su", "sy", "a5", "bhn", "e", "g", "mu", "ro", "heat_treatment", "_additional {answer {hasAnswer property result} }"], limit=1):
    """
    Perform question search on the database.
    """
    client = get_client()
    question = {
            "question": questions,
            "properties": ["material"],
            }

    response = (client.query.get("Material", properties)\
            .with_ask(question)\
            .with_limit(limit)\
            .do()
    )

    print(json.dumps(response, indent=2))

## Generate Search
def generate_search(prompt, properties=["material", "sy", "heat_treatment", "std", "su"], limit=1):
    """
    Perform generate search on the database.
    """
    client = get_client()
    response = (client.query.get("Material", properties)\
            .with_near_text({"concepts": ["Steel SAE 1040"]})\
            .with_limit(limit)\
            .with_generate(single_prompt=prompt)\
            
            .do()
    )

    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    # regular search
    perform_vector_search("capital of France")

    # keyword search
    #keyword_search("Steel")

    # hybrid search
    #hybrid_search("Steel")


    # question search
    #question_search("What other steel are similar to Steel SAE 1022?")

    # generate search
    #generate_search("Simply explain the Yield Strength (Sy) in MPa {sy}, Heat treatment {heat_treatment}, std {std}  of Steel SAE 1040 mean?")
    unittest.main()

