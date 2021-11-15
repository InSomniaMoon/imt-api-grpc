from os import name
import grpc
import user_pb2
import user_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:3001') as channel :
        stub = user_pb2_grpc.UserStub(channel)
        user_id=user_pb2.UserId(id="chris_rivers")
        print(" id : chris_rivers ")
        get_user_by_id(stub,user_id)
        print("all users  : ")
        get_users(stub)
        user = user_pb2.UserBody(
            id="1",
            name="test",
            last_active="now"
        )
        create_user(stub,user)
        print("all user after create a new one")
        get_users(stub)
        print("all user after delete chris rivers")
        delete_user(stub,user_id)
        get_users(stub)


def get_users(stub):
    users = stub.GetAllUser(user_pb2.Empty())
    for user in users:
        print(user)

def get_user_by_id(stub,id):
    print(id)
    user = stub.GetUserById(id)
    print(user)
    
def create_user(stub, userbody):
    stub.CreateUser(userbody)

def delete_user(stub,userid):
        stub.DeleteUser(userid)

if __name__ == "__main__":
    run()
