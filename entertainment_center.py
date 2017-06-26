from media import Movie
import fresh_tomatoes

# reads from csv file with movie information and generates a list of Movie objects
# each line in csv should correspond to each movie in this order:
# 		movie title, movie poster url, movie youtube trailer link
def gen_movies_list(movie_info_file_path):

	movies = []

	with open(movie_info_file_path, 'r') as conn:

		text = conn.read()

		movie_lines = text.split('\n') # assumes new line is '\n'

		for single_movie_line in movie_lines:

			single_movie = single_movie_line.split(',') # each line corresponds to a movie

			single_movie = [x.strip() for x in single_movie] # remove white space 

			single_movie_object = Movie(movie_title = single_movie[0],
										movie_poster_url = single_movie[1],
										movie_trailer_url = single_movie[2])

			movies.append(single_movie_object)

	return movies


if __name__ == '__main__':

	movie_data_loc = './movies_info.csv'

	movies = gen_movies_list(movie_data_loc)

	fresh_tomatoes.open_movies_page(movies)
