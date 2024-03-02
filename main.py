from client_setup import get_client
import dataset
from weaviate.util import generate_uuid5
import json


## Load data
df = dataset.load_dataset('datasci.csv') #(1983, 2)

## Create client
client = get_client()

## Create class for schema
class_schema = {
        # class name
        "class": "DSCode",

        # properties
        "properties": [
            {
                "name": "Prompt", # Prompt
                "dataType": ["text"],
            },
            {
                "name": "Answer", # Answer with code
                "dataType": ["text"],
            },
        ],

        # specify the vectorizer to use for text-based properties
        "vectorizer": "text2vec-openai",

        # module config
        "moduleConfig": {
            "text2vec-openai": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text"
            },
            "qna-openai": {
                "model": "gpt-3.5-turbo-instruct"
            },
            "generative-openai": {
                "model": "gpt-3.5-turbo"
            }
        },
    }

## Create class for schema
#client.schema.create_class(class_schema)
## remove class
#client.schema.delete_all()

# check if class is created
#print(client.schema.get("Material"))

## import data
client.batch.configure(  
    batch_size=200, # Specify batch size  
    num_workers=2, # Parallelize the process  
) 

with client.batch as batch:  
    for _, row in df.iterrows():  
        dscode_object = {  
            "Prompt": row["prompt"],  
            "Answer": row["answer"],    
        } 
        batch.add_data_object(dscode_object, class_name="DSCode", uuid=generate_uuid5(dscode_object))
        
#check if data is imported
print(client.query.aggregate("DSCode").with_meta_count().do())


