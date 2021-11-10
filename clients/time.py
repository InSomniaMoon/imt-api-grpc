import grpc
import time_pb2_grpc
import time_pb2
import grpc


def get_all_shot_times(stub: time_pb2_grpc.TimeServiceStub):
  times = stub.GetAllShowTimes(time_pb2.Empty())
  print(times)

def run():
  with grpc.insecure_channel('localhost:3001') as channel:
    stub = time_pb2_grpc.TimeServiceStub(channel)

    print("-------------- GetMovieByID --------------")
    get_all_shot_times(stub)


if __name__ == '__main__':
  run()
