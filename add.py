from client_setup import get_client
from weaviate.util import generate_uuid5

client = get_client()

# Create a new object
new_object = {
        "Prompt": "What is the capital of France?",
        "Answer": "Paris",
}

# define the add function
def add_object(new_object):
    new_data_uuid = generate_uuid5(new_object)

    # Add the object to Weaviate
    client.data_object.create(
            data_object=new_object,
            class_name="DSCode",
            uuid=new_data_uuid
    )


print(client.data_object.get_by_id(new_data_uuid, with_vector=False))
print(client.query.aggregate("DSCode").with_meta_count().do())

