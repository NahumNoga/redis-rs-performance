import redis
import time
import numpy as np

def set() -> None:
    redis_url = "redis://localhost:6379/0"
    conn = redis.Redis.from_url(redis_url)

    large_data = np.random.rand(20000)
    print(large_data[2000])
    large_data[2000] = 5
    print(large_data[2000])
    large_data_bytes = bytes(large_data.tobytes())
    start_set = time.time()
    conn.set("my_large_data", large_data_bytes)
    print(f"Successfully set \"my_large_data\" of size {len(large_data)}, that took {(time.time() - start_set) * 1000}ms")
