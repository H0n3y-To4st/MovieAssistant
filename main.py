import json

def load_movies_data():
  with open("movies.json", "r") as openedfile:
    movies = json.loads(openedfile.read())
    return movies

#Added error handling for user input
def get_user_genre_choice():
  print(get_unique_genres())
  genre_choice = input('Please pick a genre from the available options: ')
  unique_genres = get_unique_genres()
  while genre_choice not in unique_genres:
    genre_choice = input('Please pick a genre from the available options: ')
  return genre_choice
  
def get_unique_genres():
  unique_genres = set()
  movies = load_movies_data()

  for movie in movies:
    unique_genres.add(movie.get('genre'))
  return unique_genres

def get_movies_in_genre(genre):
  movies = load_movies_data()
  movies_in_genre = []
  for movie in movies:
    if movie.get('genre') == genre:
      movies_in_genre.append(movie)
  return movies_in_genre

def selected_genre(genre):
  movie_list = get_movies_in_genre(genre)
  for index, item in enumerate(movie_list):
    title = item.get('title')
    print("{} : {}".format(index + 1, title))

def get_movie_by_index():
    genre = get_user_genre_choice()
    movie_list = get_movies_in_genre(genre)
    for index, item in enumerate(movie_list):
      title = item.get('title')
      print("{} : {}".format(index + 1, title))

    selected_movie_index = int(input('Please select a movie by entering a number: '))
    selected_movie = movie_list[selected_movie_index - 1]

    for key, value in selected_movie.items():
        print("{}: {}".format(key,value))

if __name__ == "__main__":
  load_movies_data()
  get_movie_by_index()