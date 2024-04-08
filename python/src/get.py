import redis
import time
import numpy as np

def get() -> None:
    redis_url = "redis://localhost:6379/0"
    conn = redis.Redis.from_url(redis_url)

    start_get = time.time()
    large_data_bytes = conn.get("my_large_data")
    print(large_data_bytes[2000])
    large_data = np.frombuffer(large_data_bytes, dtype='float32')
    print(large_data[2000])
    assert large_data[2000] == 8.0
    print(f"Successfully got \"my_large_data\" of size {len(large_data)}, that took {(time.time() - start_get) * 1000}ms")
