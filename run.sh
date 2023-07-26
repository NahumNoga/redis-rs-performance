# echo @@@@@@@@@@@@ PYTHON SET @@@@@@@@@@@@@@
# (cd python && poetry run set)
# echo @@@@@@@@@@@@@ END OF SET @@@@@@@@@@@@@

# echo @@@@@@@ PYTHON  GET @@@@@@@@@@@@@@
# (cd python && poetry run get)
# echo @@@@@@@@@@@@@ END OF PYTHON GET @@@@@@@@@@@@@

# echo @@@@@ PYTHON ADD AND READ STREAM @@@@@@@@
# (cd python && (poetry run add & poetry run read))
# echo @@@@@@@@@@@@@ END OF PYTHON @@@@@@@@@@@@@

echo ############# SET PHASE #################
(cd python && poetry run add) & (cd rust-tokio && cargo run --bin read)
echo ############# END OF SET PHASE ##########

# echo ############# SET PHASE #################
# (cd rust-sync && cargo run --bin set)
# echo ############# END OF SET PHASE ##########

# echo ############# BENCHMARK #################
# echo @@@@@@@@@@@@@ NODEJS @@@@@@@@@@@@@@@@@@@@
# (cd nodejs && npm run build &>/dev/null && npm run start:release)
# echo @@@@@@@@@@@@@ END OF NODEJS @@@@@@@@@@@@@

# echo @@@@@@@@@@@@@ PYTHON @@@@@@@@@@@@@@@@@@@@
# (cd python && poetry run start)
# echo @@@@@@@@@@@@@ END OF PYTHON @@@@@@@@@@@@@

# echo @@@@@@@@@@@@@ RUST @@@@@@@@@@@@@@@@@@@@@@
# echo @@@@@@@@@@@@@ DEBUG_SYNC @@@@@@@@@@@@@@@@
# (cd rust-sync && cargo run)
# echo @@@@@@@@@@@@@ END OF DEBUG_SYNC @@@@@@@@@

# echo @@@@@@@@@@@@@ DEBUG_TOKIO @@@@@@@@@@@@@@@
# (cd rust-tokio && cargo run)
# echo @@@@@@@@@@@@@ END OF DEBUG_TOKIO @@@@@@@@

# echo @@@@@@@@@@@@@ RELEASE_SYNC @@@@@@@@@@@@@@
# (cd rust-sync && cargo build --release &>/dev/null && ./target/release/main)
# echo @@@@@@@@@@@@@ END OF RELEASE_SYNC @@@@@@@
# echo @@@@@@@@@@@@@ RELEASE_TOKIO @@@@@@@@@@@@@
# (cd rust-tokio && cargo build --release &>/dev/null && ./target/release/main)
# echo @@@@@@@@@@@@@ END OF RELEASE_TOKIO @@@@@@
# echo @@@@@@@@@@@@@ END OF RUST @@@@@@@@@@@@@@@
# echo ############# END OF BENCHMARK PHASE ####
