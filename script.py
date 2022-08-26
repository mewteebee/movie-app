movies = []
user_prompt = "Enter '1' to add a movie, '2' to see your movies, '3' to find a movie by title and '4' to quit: "

def add_new_movie():
    title = input("Enter title: ")
    year = input("Enter year: ")
    rating = input("Enter rating: ")

    movies.append({
        'title' : title, 
        'year' : year,
        'rating' : rating,
    })

def show():
    for movie in movies:
        show_movies(movie)

def show_movies(movie):
    print("")
    print(f"Title: {movie['title']}")
    print(f"Year: {movie['year']}")
    print(f"Rating: {movie['rating']}")

def find_movie():
    search = input("Enter movie title: ")

    for movie in movies: 
        if movie['title'] == search:
            show_movies(movie)

options = {
    '1': add_new_movie,
    '2': show,
    '3': find_movie
}            

def menu():
    selection = input(user_prompt)
    while selection != '4':
        if selection in options:
            selected_function = options[selection]
            selected_function()
        else: 
            print("Unknown command. Try again.")
        
        selection = input(user_prompt)

menu()
