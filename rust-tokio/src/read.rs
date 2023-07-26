extern crate redis;
extern crate tokio;

use tokio::time::sleep;

use redis::{
    streams::{StreamReadOptions, StreamReadReply},
    AsyncCommands,
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let redis_url = "redis://localhost:6380/0";

    let mut conn = redis::Client::open(redis_url)
        .expect("Invalid connection URL")
        .get_multiplexed_async_connection()
        .await
        .expect("failed to connect to Redis");

    sleep(std::time::Duration::from_millis(1000)).await;
    let opts = StreamReadOptions::default().count(1).block(0);
    for i in 0..4 {
        let start = std::time::Instant::now();
        let large_data_stream: Option<StreamReadReply> = conn
            .xread_options(&["my_large_data_stream"], &[format!("{i}-0")], &opts)
            .await?;
        // assert_eq!(large_data[2000], 5u8);
        if let Some(reply) = large_data_stream {
            for stream_key in reply.keys {
                println!("->> xread block: {}", stream_key.key);
                for stream_id in stream_key.ids {
                    println!("  ->> StreamId: {:?}", stream_id.id);
                    // for (field, value) in stream_id.map {
                    //     // Check if the value is a ByteArray variant
                    //     // Decode the "string-data" into actual bytes
                    //     let byte_array = decode_byte_array(&value);
                    //     let byte_array_size = byte_array.len();
                    //     println!(
                    //         "  ->> Field: {:?}, Size: {}, Data: {:?}",
                    //         field, byte_array_size, byte_array
                    //     );
                    // }
                    for (field, value) in stream_id.map {
                        println!("  ->> field: {:?} ", field);
                    }
                }
            }
        }
        println!(
            "Successfully got \"my_large_data\", that took {:?}",
            start.elapsed(),
        );
    }

    Ok(())
}

// fn decode_byte_array(byte_str: &str) -> Vec<u8> {
//     // In this example, we assume the byte array is represented as a string
//     // in the format "'\xHH\xHH\xHH...'". We need to remove the surrounding single quotes and decode
//     // the hexadecimal characters into bytes.

//     let hex_chars = &byte_str[2..byte_str.len() - 1]; // Removing the surrounding single quotes.

//     let mut byte_array = Vec::new();
//     let mut chars_iter = hex_chars.chars();
//     while let Some(ch) = chars_iter.next() {
//         if ch == '\\' {
//             // Escaped character; we need to parse the hexadecimal value.
//             let hex_value = format!(
//                 "{}{}",
//                 chars_iter.next().unwrap(),
//                 chars_iter.next().unwrap()
//             );
//             if let Ok(byte) = u8::from_str_radix(&hex_value, 16) {
//                 byte_array.push(byte);
//             }
//         }
//     }

//     byte_array
// }

// // 5) Blocking xread
// tokio::spawn(async {
// 	let client = Client::open("redis://127.0.0.1/").unwrap();
// 	let mut con = client.get_tokio_connection().await.unwrap();
// 	loop {
// 		let opts = StreamReadOptions::default().count(1).block(0);
// 		let result: Option<StreamReadReply> = con.xread_options(&["my_stream"], &["$"], opts).await.unwrap();
// if let Some(reply) = result {
// 	for stream_key in reply.keys {
// 		println!("->> xread block: {}", stream_key.key);
// 		for stream_id in stream_key.ids {
// 			println!("  ->> StreamId: {:?}", stream_id);
// 		}
// 	}
// 	println!();
// }
// 	}
// });
