import json
import grpc
from concurrent import futures
import movie_pb2
import movie_pb2_grpc



class MovieServicer(movie_pb2_grpc.MovieServicer):
  def __init__(self):
    with open('{}/databases/movies.json'.format("."), "r") as jsf:
      self.db = json.load(jsf)["movies"]

  def GetMovieByID(self, request, context):
    for movie in self.db:
      if movie["id"] == request.id:
        print(movie)
        return movie_pb2.MovieData(title=movie['title'],
                                   rating=movie['rating'],
                                   director=movie['director'],
                                   id=movie['id'])

  def GetMovies(self, request, context):
    for movie in self.db:
      yield movie_pb2.MovieData(title=movie['title'],
                                rating=movie['rating'],
                                director=movie['director'],
                                id=movie['id'])

  def CreateMovie(self, request, context):
    self.db.append({
        "id": request.id,
        "title": request.title,
        "director": request.director,
        "rating": request.rating
    })
    return movie_pb2.Empty()

  def UpdateMovie(self, request, context):
    id = request.id

    for movie in self.db:
      if (str(movie["id"]) == str(id)):
        print(request.title)
        movie["title"] = request.title
        movie["director"] = request.director
        movie["rating"] = request.rating

    return movie_pb2.Empty()

  def DeleteMovie(self, request, context):
    id = request.id
    for movie in self.db:
      if (str(movie["id"]) == str(id)):
        self.db.remove(movie)
    return movie_pb2.Empty()
   

  def GetListMovies(self, request, context):
        for movie in self.db : 
            yield movie_pb2.MovieData(title=movie['title'], rating=movie['rating'],director=movie['director'], id=movie['id'])

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  movie_pb2_grpc.add_MovieServicer_to_server(MovieServicer(), server)
  server.add_insecure_port('[::]:3002')
  server.start()
  server.wait_for_termination()


if __name__ == '__main__':
  serve()