import grpc
import booking_pb2
import booking_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:3005') as channel :
        stub = booking_pb2_grpc.BookingStub(channel)
        print("all bookings -------------")
        get_booking(stub)
        print("booking by id ------------")
        id = booking_pb2.UserId(id="chris_rivers")
        get_booking_by_id(stub,id)

def get_booking(stub):
    bookings = stub.GetAllBookings(booking_pb2.Empty())
    for booking in bookings:
        print(booking)

def get_booking_by_id(stub,id):
    booking = stub.GetBookingByUserId(id)
    print(booking)

def create_booking(stub, booking):
    stub.CreateBooking(booking)


if __name__ == "__main__":
    run()
