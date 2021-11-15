import grpc

import time_pb2_grpc
import time_pb2
import grpc


def get_all_show_times(stub: time_pb2_grpc.TimeStub):
  times = stub.GetAllShowTimes(time_pb2.Empty())
  print(times)


def get_st_by_date(stub: time_pb2_grpc.TimeStub, d: str):
  times = stub.GetShowTimeByDate(time_pb2.Date(date=d))
  print(times)

def run():

  print("runing to host " + "localhost" + ':' + "3003")
  with grpc.insecure_channel('localhost' + ':' + "3003") as channel:
    stub = time_pb2_grpc.TimeStub(channel)

    print("-------------- GetAllShowTimes --------------")
    #get_all_show_times(stub)

    print("-------------- GetShowtimesByDate --------------")
    get_st_by_date(stub, "20151201")


if __name__ == '__main__':
  run()
