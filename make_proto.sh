python3 -m grpc_tools.protoc -I=./protos --python_out=./servers/ --grpc_python_out=./servers/ $1.proto
python3 -m grpc_tools.protoc -I=./protos --python_out=./clients/ --grpc_python_out=./clients/ $1.proto