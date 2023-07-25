import redis
import time

def start() -> None:
    redis_url = "redis://localhost:6380/0"
    conn = redis.Redis.from_url(redis_url)

    start = time.time()
    my_large_data_stream = conn.xread(streams={"my_large_data_stream": b'$'}, count=None, block=1000)
    read_time = time.time() - start
    if len(my_large_data_stream) > 0:
        [[stream, [[number, parts]]]] = my_large_data_stream
        x = { y.decode('utf-8'): parts.get(y).decode('utf-8') for y in parts.keys() }
        first_key = list(x.keys())[0]
        print(f"Successfully got \"my_large_data_stream\" \"{first_key}\" of size {len(list(x[first_key]))}, that took {read_time * 1000}ms")
    else:
        print(my_large_data_stream)
    start = time.time()
    my_large_data_stream = conn.xread(streams={"my_large_data_stream": b'1-0'}, count=None, block=1000)
    read_time = time.time() - start
    if len(my_large_data_stream) > 0:
        [[stream, [[number, parts]]]] = my_large_data_stream
        x = { y.decode('utf-8'): parts.get(y).decode('utf-8') for y in parts.keys() }
        first_key = list(x.keys())[0]
        print(f"Successfully got \"my_large_data_stream\" \"{first_key}\" of size {len(list(x[first_key]))}, that took {read_time * 1000}ms")
    else:
        print(my_large_data_stream)
    # my_large_data_stream = conn.xread(streams={"my_large_data_stream": '$'}, count=None, block=100)
    # print(f"Successfully got \"my_large_data_stream\" of {my_large_data_stream}, that took {(time.time() - start) * 1000}ms")
