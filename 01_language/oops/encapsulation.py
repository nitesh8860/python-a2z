class Movie:
  def __init__(self):
    self.title = ""
    self.year = -1
    self.genre = ""

  def __init__(self, t, y, g):
    self.title = t
    self.year = y
    self.genre = g

  # getters setters
  def get_title(self):
    return self.title

  def set_title(self, t):
    self.title = t

  def get_year(self):
    return self.year

  def set_year(self, y):
    self.year = y

  def get_genre(self):
    return self.genre

  def set_genre(self, g):
    self.genre = g

  def print_details(self):
    print("Title: ", self.title)
    print("Year: ", self.year)
    print("Genre: ", self.genre)

def main(): 
  movie = Movie("The Lion King", 1994, "Adventure")
  movie.print_details()

  print("---")  
  movie.set_title("Forrest Gump")
  print("New title: ", movie.get_title())  

if __name__ == "__main__":
    main()