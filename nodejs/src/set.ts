import { createClient, commandOptions } from "redis";

const start = async () => {
  const redisUrl = "redis://localhost:6379/0";

  const client = createClient({ url: redisUrl });
  await client.connect();

  const start = Date.now();
  let large_data = Array.from({ length: 20000 }, () =>
    Math.floor(Math.random() * 20000)
  );
  console.log(large_data[2000]);
  large_data[2000] = 11.564654;
  console.log(large_data[2000]);
  const int32 = new Float32Array(large_data);
  const int8 = new Int8Array(int32.buffer);

  const bytes = Buffer.from(int32.buffer);

  client.set("my_large_data", bytes);
  console.log(
    `Successfully got \"my_large_data\" of size ${
      large_data.length
    }, that took ${Date.now() - start}ms`
  );
};

start();
