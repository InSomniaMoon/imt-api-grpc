import grpc
import movie_pb2
import movie_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:3002') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)
        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)
        print("-------------- GetListMovies --------------")
        get_list_movies(stub)


        mvdata = movie_pb2.MovieData(title="test",rating=4.0,director="me",id="4")
        create_movie(stub, mvdata)
        get_list_movies(stub)
        mvu = movie_pb2.MovieData(title="update",rating=0,director="me",id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        update_movie(stub, mvu)
        print("-------------- GetListMovies --------------")
        get_list_movies(stub)
        delete_movie(stub,movieid)
        print("-------------- GetListMovies --------------")
        get_list_movies(stub)


def get_list_movies(stub):
    movies = stub.GetListMovies(movie_pb2.Empty())
    for movie in movies : 
        print("Movie called : " + movie.title)

def delete_movie(stub,id):
    stub.DeleteMovie(id)

def create_movie(stub, movie):
    stub.CreateMovie(movie)


def get_movie_by_id(stub, id):
    movie = stub.GetMovieByID(id)
    print(movie)

def update_movie(stub, moviedata):
    stub.UpdateMovie(moviedata)


if __name__ == "__main__":
    run()
