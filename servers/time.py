import json
from concurrent import futures

import grpc
import time_pb2
import time_pb2_grpc
from settings import TIMEPORT


class ShowTimeServicer(time_pb2_grpc.TimeServiceServicer):
  def __init__(self):
    with open('{}/databases/times.json'.format("."), "r") as jsf:
      self.db = json.load(jsf)["schedule"]

  def populate_showTime(self, st):
    return time_pb2.ShowTime(st["date"], st["movies"])

  def GetAllShowTimes(self, request, context):
    return map(self.populate_showTime, self.db)

  def GetShowTimesByDate(self, request, context):
    for line in self.db:
      if line["date"] == request.date:
        return self.populate_showTime(line)

  def passe():
    pass


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  time_pb2_grpc.add_TimeServiceServicer_to_server(ShowTimeServicer(),
                                                      server)
  server.add_insecure_port('[::]:' + TIMEPORT)
  server.start()
  server.wait_for_termination()


if __name__ == '__main__':
  serve()
