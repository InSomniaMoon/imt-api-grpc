import grpc
import booking_pb2
import booking_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:3001') as channel :
        stub = booking_pb2_grpc.UserStub(channel)


def get_booking(stub):
    bookings = stub.GetAllBookings(booking_pb2.Empty())
    for booking in bookings:
        print(booking)

def get_booking_by_id(stub,id):
    user = stub.GetBookingByUserId(stub,id)
    print(user)
    
def create_booking(stub, booking):
    stub.CreateBooking(booking)


if __name__ == "__main__":
    run()
