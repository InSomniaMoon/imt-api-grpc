import concurrent
import grpc
import json
import booking_pb2 
import booking_pb2_grpc
from settings import BOOKINGPORT

class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open('{}/databases/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def GetAllBookings(self,request,context):
        for booking in self.db:
            yield booking_pb2.BookingMessage(date=booking['dates'],userid=booking['userid'])

    def GetBookingByUserId(self, request, context):
        for booking in self.db:
            if booking["id"] == request.id:
                return booking_pb2.BookingMessage(
                    userid=booking["userid"],
                    date=booking["dates"]
                )

    def CreateBooking(self, request, context):
        self.db.append({
            "userid":request.userid,
            "date":request.date
        })
    

def serve():
  server = grpc.server(concurrent.Future.ThreadPoolExecutor(max_workers=10))
  booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(),
                                                      server)
  server.add_insecure_port('[::]:' + BOOKINGPORT)
  server.start()
  server.wait_for_termination()


if __name__ == '__main__':
  serve()
