import fresh_tomatoes
import media

# instances of my favorite movies
batman = media.Movie("Batman",
                     "A heroic genius who fights for justice. He's also rich.",
                     "https://upload.wikimedia.org/wikipedia"
                     "/en/a/af/Batman_Begins_Poster.jpg",
                     "https://www.youtube.com/watch?v=vak9ZLfhGnQ")
wonder_woman = media.Movie("Wonder Woman",
                           "The daughter of Zeus fights for justice and"
                           " helps mankind overcome evil.",
                           "https://upload.wikimedia.org/wikipedia/en/"
                           "e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")
lotr = media.Movie("Lord of the Rings",
                   "The adventure of conquering the inner & "
                   "outer evil by the smallest of figures.",
                   "https://upload.wikimedia.org/wikipedia/en/"
                   "9/9d/The_Lord_of_the_Rings_The_Fellowship_of_"
                   "the_Ring_%282001%29_theatrical_poster.jpg",
                   "https://www.youtube.com/watch?v=Pki6jbSbXIY")
o_brother_where_thou = media.Movie("O Brother Where Art Thou",
                                   "A group of guys hilarious "
                                   "discover more to life.",
                                   "https://upload.wikimedia.org/wikipedia/en"
                                   "/5/5b/O_brother_where_art_thou_ver1.jpg",
                                   "https://www.youtube.com/"
                                   "watch?v=eW9Xo2HtlJI")

superman = media.Movie("Man of Steel", "An alien comes to earth "
                                       "and saves the planet.",
                       "https://upload.wikimedia.org/wikipedia/en/8/85/"
                       "ManofSteelFinalPoster.jpg",
                       "https://www.youtube.com/watch?v=T6DJcgm3wNY")

x_men = media.Movie("X-MEN Apocalypse",
                    "A movies filled with racial and political undertones"
                    " where Mutants save the world",
                    "https://upload.wikimedia.org/wikipedia/en"
                    "/0/04/X-Men_-_Apocalypse.jpg",
                    "https://www.youtube.com/watch?v=COvnHv42T-A")
# end of movie instances

# List of movies saved as an array
movies = [batman, wonder_woman, lotr, o_brother_where_thou, superman, x_men]
fresh_tomatoes.open_movies_page(movies)
