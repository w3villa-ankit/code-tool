import requests

# Define the base url of the Google Books API
base_url = "https://www.googleapis.com/books/v1/volumes?q="

# Function to fetch books from the Google Books API
def fetch_books(query):
    # Send a request to the Google Books API and fetch the book data
    response = requests.get(base_url + query)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Parse the JSON data from the API response
    data = response.json()

    return data['items']

# Function to extract the necessary information from the book data
def process_book_data(data):
    book_list = []

    for item in data:
        volume_info = item['volumeInfo']
        title = volume_info.get('title', 'Unknown')
        authors = volume_info.get('authors', ['Unknown'])
        print('Title:', title)
        print('Author:', ', '.join(authors))
        print('----------')

# Function to send a query to Google Books and print the list of books returned
def get_books(query):
    # Fetch the books from the Google Books API
    data = fetch_books(query)

    # Process the book data and print the list of books
    process_book_data(data)

# Test the function
get_books('science fiction')