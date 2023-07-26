import redis
import time

def set() -> None:
    redis_url = "redis://localhost:6380/0"
    conn = redis.Redis.from_url(redis_url)

    large_data = bytearray(49152000 * 10)
    large_data_bytes = bytes(large_data)
    start_set = time.time()
    conn.set("my_large_data", large_data_bytes)
    print(f"Successfully set \"my_large_data\" of size {len(large_data)}, that took {(time.time() - start_set) * 1000}ms")
