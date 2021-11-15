from concurrent import futures
import grpc
import json
import user_pb2 
import user_pb2_grpc
from settings import USERPORT


class UserServicer(user_pb2_grpc.UserServicer):
    def __init__(self):
        with open('{}/databases/users.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["users"]

    def GetAllUser(self,request,context):
        print(self.db)
        for user in self.db:
            yield user_pb2.UserBody(
                id=user["id"],
                name=user["name"],
                last_active=user["last_active"]
            )

    def GetUserById(self, request, context):
        for user in self.db:
            print(request.id)
            if(str(user["id"]) == str(request.id)):
                return user_pb2.UserBody(
                    id=user["id"],
                    name=user["name"],
                    last_active=user["last_active"]
                )
        return user_pb2.UserBody(
            id="",
            name="",
            last_active=""
        )
    def CreateUser(self, request, context):
        self.db.append({
            "id":request.id,
            "name":request.name,
            "last_active":request.last_active
        })
    
    def DeleteUser(self, request, context):
        id=request.id
        for user in self.db:
            if(str(user["id"] == str(id))):
                self.db.remove(user)
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:'+USERPORT)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
