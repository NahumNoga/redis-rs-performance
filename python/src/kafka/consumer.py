import time
from datetime import datetime
import json 
from kafka import KafkaConsumer

def start() -> None:
    consumer = KafkaConsumer(
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest'
    )
    consumer.subscribe(['my_large_data_stream'])
    for message in consumer:
        print(f"size data = {len(message.value)}")

    # large_data = bytearray(4)
    # large_data_bytes = bytes(large_data)
    # start = time.time()
    # producer.send('my_large_data_stream', large_data_bytes)
    # print(f"Send my_large_data_stream to kafka, that took {(time.time() - start) * 1000}ms")



# import time 
# import json 
# import random 
# from datetime import datetime
# from data_generator import generate_message









# if __name__ == '__main__':
#     # Infinite loop - runs until you kill the program
#     while True:
#         # Generate a message
#         dummy_message = generate_message()
        
#         # Send it to our 'messages' topic
#         print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
#         producer.send('messages', dummy_message)
        
#         # Sleep for a random number of seconds
#         time_to_sleep = random.randint(1, 11)
#         time.sleep(time_to_sleep)
