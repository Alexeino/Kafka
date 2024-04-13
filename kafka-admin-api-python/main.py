import os
from dotenv import load_dotenv
from fastapi import FastAPI
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError
from contextlib import asynccontextmanager
import logging


load_dotenv(verbose=True)
logger=logging.getLogger()

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Starting application setup...")

    try:
        import pdb; pdb.set_trace()
        client = KafkaAdminClient(
            bootstrap_servers=os.environ.get("BOOTSTRAP_SERVERS")
        )
        
        name=os.environ.get("TOPICS_PEOPLE_BASIC_NAME")
        num_partitions=int(os.environ.get("TOPICS_PEOPLE_BASIC_PARTITION"))
        replication_factor=int(os.environ.get("TOPICS_PEOPLE_BASIC_REPLICAS"))
        
        topic = NewTopic(
            name,num_partitions,replication_factor
        )

        client.create_topics([topic])
        yield
    except TopicAlreadyExistsError:
        print("Topic already exists!")
        yield
    finally:
        print("Closing Kafka Admin client! ")
        client.close()
    

app = FastAPI(title="Kafka Admin Demo",lifespan=lifespan)
    
@app.get("/hello")
async def hello():
    return {
        "message": "Hello All!"
    }
    
