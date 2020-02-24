# This will contain book titles, authors and price

# Create a fuction which displays all the books and their information
def display_all_books():
    for index in range(0, len(books)):
        print(index+1, books[index])

# Create a function which displays the menu
def display_menu():
    print("      Menu      ")
    print("1. Display all books")
    print("2. Add a book")
    print("3. Delete a book")
    print("4. Update a book")
    print("5. Quit program")    
# Create a list with the book titles, authors and price
books = [["New Recruit","Robert Muchamore", 20], ["Into the fire", "Greg Hurwitz", 27], ["Life as a Casketeer", "Francis Tipene", 28]]

# Menu will keep displaying so long as this stays true
show_menu = True

# Display menu until user quits 
while show_menu == True :
    display_menu()
    # Get selected menu option
    while True:
        # Check if value entered is a valid integer
        try:
            # Get Menu option
            menu_option = int(input("What menu option do you want to pick?: "))
            break
        # Check if value entered was a integer
        except:
            #display error message
            print("Error please enter a integer (number)")
            # Redisplay menu
            display_menu()
            
            # Display all books
            if menu_option == 1:
                display_all_books()
            
            # add a student 
            elif menu_option == 2:
                book_name = input("Enter the name of a book: ")
                author_name = input("Enter the name of the author: ")
                book_price = int(input("Enter the price of the book: "))
                
                new_book = [book_name, author_name, book_price]
                
                books.append(new_book)
