class Movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating
    
    def info(self):
        print(f"Title: {self.title} | Rating: {self.rating}")


m1 = Movie("Leo" , 7.9)
m2 = Movie("Interstellar", 8.7)
m3 = Movie("12th Fail", 8.9)


movies_list = [m1,m2,m3]

print("Movies with rating > 8: ")
for movie in movies_list:
    if movie.rating > 8:
        movie.info()