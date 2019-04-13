import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.google.no/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0ahUKEwiAg4_LsZrUAhVDD5oKHSddDWMQtwIILjAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D4KPTXpQehio&usg=AFQjCNEMhDRSvsuiQ7FF7sfh27xPQmiQpQ")
#print (toy_story.movie_storyline)

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://youtu.be/cRdxXPV9GNQ")

#avatar.show_trailer()

oceans_11 = media.Movie("Oceans 11",
	"Danny Ocean wants to score the biggest heist in history. He combines an eleven member team",
	"https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
	"https://youtu.be/u7VTkceSsEw")

#oceans_11.show_trailer()

notting_hill = media.Movie ("Notting Hill",
	"The life of a simple bookshop owner changes when he meets the most famous film star in the world.",
	"https://upload.wikimedia.org/wikipedia/en/3/38/NottingHillRobertsGrant.jpg",
	"https://youtu.be/BN-REWY4vc4")

love_actually = media.Movie ("Love Actually",
	"Follows the lives of eight very different couples in dealing with their love lives in various loosely interrelated tales all set during a frantic month before Christmas in London, England.",
	"https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg",
	"https://youtu.be/BN-REWY4vc4")

short_circuit = media.Movie ("Short Circuit",
	"Number 5 of a group of experimental robots in a lab is electrocuted, suddenly becomes intelligent, and escapes.",
	"https://upload.wikimedia.org/wikipedia/en/b/b8/Short_Circuit_%281986_film_poster%29.jpg",
	"https://youtu.be/9rlI3Xg9g_A")

movies = [toy_story, avatar, oceans_11, notting_hill, love_actually,short_circuit]
fresh_tomatoes.open_movies_page(movies)