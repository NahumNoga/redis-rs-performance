import redis
import time

def get() -> None:
    redis_url = "redis://localhost:6380/0"
    conn = redis.Redis.from_url(redis_url)

    start_get = time.time()
    large_data = conn.get("my_large_data")
    assert large_data[2000] == 5
    print(f"Successfully got \"my_large_data\" of size {len(large_data)}, that took {(time.time() - start_get) * 1000}ms")
