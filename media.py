import webbrowser


class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """ This class provides a way to store movie related information"""
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube


    def show_trailer(self):
        """ open movie trailer"""
        webbrowser.open(self.trailer_youtube)