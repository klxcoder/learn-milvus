from pymilvus import MilvusClient

client = MilvusClient("milvus_demo.db")

res = client.query(
    collection_name="demo_collection",
    limit=100,
    output_fields=["text", "subject"],
)

print('All entities:')
print(res)