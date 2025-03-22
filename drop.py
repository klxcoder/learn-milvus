from pymilvus import MilvusClient

client = MilvusClient("milvus_demo.db")

client.drop_collection(collection_name="demo_collection")
