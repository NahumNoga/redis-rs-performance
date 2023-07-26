import redis
import time

def add() -> None:
    redis_url = "redis://localhost:6380/0"
    conn = redis.Redis.from_url(redis_url)

    large_data = bytearray(49152000 * 4)
    large_data_bytes = bytes(large_data)
    for i in range(4):
        start_add = time.time()
        conn.xadd(name="my_large_data_stream", id=str(i+1), fields={f"data_{i}": large_data_bytes})

        print(f"Add my_large_data_stream_{i} to stream, that took {(time.time() - start_add) * 1000}ms")
