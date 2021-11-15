import json
import os
from concurrent import futures

import time_pb2
import time_pb2_grpc
import grpc

os.environ['GRPC_VERBOSITY'] = "debug"
os.environ[
    'GRPC_TRACE'] = "call_error,connectivity_state,pick_first,round_robin,glb,http"


# populate showTime()
# @param: st:showTime dict
# @brief: méthode interne permettant de retourner un objet grpc showtime
def populate_showTime(st):
  print(st)
  return time_pb2.ShowTime(date=time_pb2.Date(date=st["date"]),
                           movies=list(st["movies"]))


class ShowTimeServicer(time_pb2_grpc.TimeServicer):
  def __init__(self):
    with open('{}/databases/times.json'.format("."), "r") as jsf:
      self.db = json.load(jsf)["schedule"]

  # get all show times
  # @brief: retourne la liste des showTimes
  def GetAllShowTimes(self, request, context):
    print("GetAllShowTimes called")
    # times = map(populate_showTime, self.db)
    times = time_pb2.ShowTime(date="25112021",
                              movies=list("edfklneekn", "zfkdfefk"))
    print(times)
    return times

  # get showTimes by date
  # @param: data:string
  # @brief: reoutrne les howtimes d'une date en particulier
  def GetShowTimeByDate(self, request, context):
    print("GetShowTimeByDate called")
    for line in self.db:
      if line["date"] == request.date:
        return populate_showTime(line)


# lance le serveur gRPC
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  print("serving on " + "localhost" + ':' + "3003")
  time_pb2_grpc.add_TimeServicer_to_server(ShowTimeServicer(), server)
  server.add_insecure_port('[::]:' + "3003")
  server.start()
  server.wait_for_termination()


if __name__ == '__main__':
  serve()
