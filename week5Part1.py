class movie:
    def __init__(self, title, genre, length, streamingsite):
        #Attributes / instance variables
        self.title = title
        self.genre=genre
        self.length=length
        self.streamingsite=streamingsite
        self.ratings=[]

#Methods
    def add_rating(self, rating):
        if 0 <= rating <= 10:
            self.ratings.append(rating)
        else:
            print("Rating must be between 0 and 10")
    
    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Duration: {self.length} minutes")
        print(f"Streaming Site: {self.streamingsite}")
        print(f"Average Rating: {self.get_average_rating():.1f}/10")

#inherited class
class marvelunviverse(movie):
    def __init__(self, title, genre, length, streamingsite,phase, mainheros):
        super().__init__(title, genre, length, streamingsite)
        self.phase = phase
        self.mainheros = mainheros  
        self.post_credit_scenes=0
    
    def set_post_credit_scenes(self, count):
        self.post_credit_scenes = count
    
    def display_info(self):  # Overriding the parent method
        super().display_info()
        print(f"MCU Phase: {self.phase}")
        print(f"Main Heroes: {', '.join(self.mainheros)}")
        if self.post_credit_scenes > 0:
            print(f"Post-credit scenes: {self.post_credit_scenes} (stay till the end!)")

# Example 
if __name__ == "__main__":
    # Create a regular movie
    regular_movie = movie("Inception", "Sci-Fi",148,"Netflix")
    regular_movie.add_rating(8)
    regular_movie.add_rating(9)
    regular_movie.display_info()
    
    # Create a Marvel movie
    avengers = marvelunviverse(
        title="Avengers: Endgame",
        genre="Action",
        length=181,
        streamingsite="Disney plus",
        phase=3,
        mainheros=["Iron Man", "Captain America", "Thor", "Hulk"]
    )
    avengers.set_post_credit_scenes(1)
    avengers.add_rating(9)
    avengers.add_rating(10)
    avengers.add_rating(10)
    avengers.display_info()