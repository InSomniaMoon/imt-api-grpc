import grpc
import json
import booking_pb2 
import booking_pb2_grpc

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