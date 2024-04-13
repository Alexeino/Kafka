# Apache Kafka

<!-- Notes -->
[Apache Kafka Notes Click Here](https://www.notion.so/Apache-Kafka-6f3508d341434beb80a00dd527777e75?pvs=4)

* Starting the Kafka using docker-compose.yml<br>
``` docker compose up -d ```

* Running kafka-topics commands
    * Exec into the cli-tools container using - ``` docker exec -it cli-tools bash ```

    * List Kafka Topics<br>
    ``` kafka-topics --list --bootstrap-server broker0:29092,broker1:29093,broker2:29094 ```
    * Create a Kafka Topic <br>
    ``` kafka-topics --bootstrap-server broker0:29092,broker1:29093,broker2:29094 --create --topic people --partitions 2 --replication-factor 2 ```
    * Describe a Kafka Topic<br>
    ``` kafka-topics --describe --topic people --bootstrap-server broker0:29092,broker1:29093,broker2:29094 ```
    * Deleting a Kafka Topic<br>
    ``` kafka-topics --delete --topic people --bootstrap-server broker0:29092,broker1:29093,broker2:29094 ```
    * Creating kafka topic with different retention period<br>
    ``` kafka-topics --create --topic people --config retention.ms=360000 --bootstrap-server broker0:29092 ```
    * Checking all the configuration settings of a Kafka Topic<br>
    ``` kafka-configs --describe --retention --bootstrap-server broker0:29092 --topic people ```
    * Changing the retention period of a topic<br>
    ``` kafka-configs --bootstrap-server broker0:29092 --alter --entity-type topics --entity-name people --add-config retention.ms=500000 ```
    * Creating a compact type kafka topic (tombstone functionality)<br>
    ``` kafka-topics --bootstrap-server broker0:29092 --create --topic people.latest --config cleanup.policy=compact ```


## KafkaAdminClientAPI (Python)
* Go into kafka-admin-api-python and start the FastAPI app using<br> ``` uvicorn app:main --reload ```
* The script should create a topics with name specified inside .env file.
* Check into the cli-tools by running<br>
``` kafka-topics --list --broker-url broker0:29092 ```