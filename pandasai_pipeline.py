from pandasai.pipelines import Pipeline, BaseLogicUnit
from vector_search import perform_vector_search

# Define your custom logic unit for vector search
class VectorSearchLogicUnit(BaseLogicUnit):
    def execute(self, data):
        # Your vector search code here
        # For example:
        results = perform_vector_search(data['concepts'])
        return results


# Instantiate and use your custom pipeline
pipeline = Pipeline(
        units=[
            VectorSearchLogicUnit()
        ]
    )

result = pipeline.run({'concepts': ['I want to merge two columns']})

print(result)

