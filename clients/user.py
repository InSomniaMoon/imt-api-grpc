import grpc
import user_pb2
import user_pb2_grpc
from settings import USERPORT

def run():
    with grpc.insecure_channel('localhost:' + USERPORT) as channel :
        stub = user_pb2_grpc.UserStub(channel)
        print("hello")
        user_id=user_pb2.UserId(id="chris_rivers")
        get_user_by_id(stub,user_id)


def get_users(stub):
    users = stub.GetAllUser(user_pb2.Empty())
    for user in users:
        print(user)

def get_user_by_id(stub,id):
    user = stub.GetUserById(stub,id)
    print(user)
    
def create_user(stub, userbody):
    stub.CreateUser(userbody)

def delete_user(stub,userid):
        stub.DeleteUser(userid)

if __name__ == "__main__":
    run()
