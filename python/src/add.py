import redis
import time

def start() -> None:
    redis_url = "redis://localhost:6380/0"
    conn = redis.Redis.from_url(redis_url)

    large_data = bytearray(49152000)
    large_data_bytes = bytes(large_data)
    start = time.time()
    for i in range(4):
        conn.xadd(name="my_large_data_stream", id=str(i+1), fields={f"data_{i}": large_data_bytes})

        print(f"Add my_large_data_stream_{i} to stream, that took {(time.time() - start) * 1000}ms")
