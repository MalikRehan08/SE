

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
password = quote_plus('USERNAME@123')
uri = "mongodb+srv://USERNAME:" + password + "@cluster0.n4i3ipr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['LibrarySearch']
# Send a ping to confirm a successful connection
try:
    # db.command('ping')
    # db.create_collection("booksCollection")
    # db.booksCollection.insert_many(
    #     [
    #         {'title': 'The Catcher in the Rye', 'ISBN': '978-0-316-76948-0', 'author': 'J.D. Salinger', 'genre': 'Fiction', 'type': 'Books'},
    #         {'title': 'To Kill a Mockingbird', 'ISBN': '978-0-06-112008-4', 'author': 'Harper Lee', 'genre': 'Fiction', 'type': 'Books'},
    #         {'title': 'The Hobbit', 'ISBN': '978-0-261-10235-4', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'type': 'Books'},
    #         {'title': '1984', 'ISBN': '973-0-452-28423-4', 'author': 'George Orwell', 'genre': 'Science Fiction', 'type': 'Books'},
    #         {'title': '1984', 'ISBN': '973-0-452-28423-4', 'author': 'George Orwell', 'genre': 'Science Fiction', 'type': 'Books'},
    #         {'title': 'The Great Gatsby', 'ISBN': '971-3-16-148410-0', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction', 'type': 'Books'},

    #         # CDs
    #         {'title': 'Greatest Hits', 'ISBN': '123-4-567890-1', 'author': 'Various Artists', 'genre': 'Pop', 'type': 'CDs'},
    #         {'title': 'Jazz Classics', 'ISBN': '234-5-678901-2', 'author': 'Jazz Ensemble', 'genre': 'Jazz', 'type': 'CDs'},
    #         {'title': 'Rock Anthems', 'ISBN': '345-6-789012-3', 'author': 'Rock Band', 'genre': 'Rock', 'type': 'CDs'},
    #         {'title': 'Hip Hop Collection', 'ISBN': '456-7-890123-4', 'author': 'Hip Hop Artists', 'genre': 'Hip Hop', 'type': 'CDs'},
    #         {'title': 'Pop Hits 2023', 'ISBN': '567-8-901234-5', 'author': 'Top Pop Artists', 'genre': 'Pop', 'type': 'CDs'},

    #         # Magazines
    #         {'title': 'National Geographic', 'ISBN': '987-6-543210-1', 'author': 'National Geographic Society', 'genre': 'Science', 'type': 'Magazines'},
    #         {'title': 'Fashion Trends', 'ISBN': '876-5-432109-8', 'author': 'Fashion Editors', 'genre': 'Fashion', 'type': 'Magazines'},
    #         {'title': 'Tech Today', 'ISBN': '765-4-321098-7', 'author': 'Tech Experts', 'genre': 'Technology', 'type': 'Magazines'},
    #         {'title': 'Lifestyle Living', 'ISBN': '654-3-210987-6', 'author': 'Lifestyle Gurus', 'genre': 'Lifestyle', 'type': 'Magazines'},
    #         {'title': 'Business W
    # eekly', 'ISBN': '543-2-109876-5', 'author': 'Business Journalists', 'genre': 'Business', 'type': 'Magazines'},

    #         # Videos
    #         {'title': 'Action Movie Marathon', 'ISBN': '876-5-432109-8', 'author': 'Action Directors', 'genre': 'Action', 'type': 'Videos'},
    #         {'title': 'Comedy Central', 'ISBN': '765-4-321098-7', 'author': 'Comedy Writers', 'genre': 'Comedy', 'type': 'Videos'},
    #         {'title': 'Documentary Series', 'ISBN': '654-3-210987-6', 'author': 'Documentary Filmmakers', 'genre': 'Documentary', 'type': 'Videos'},
    #         {'title': 'Drama Showcase', 'ISBN': '543-2-109876-5', 'author': 'Drama Directors', 'genre': 'Drama', 'type': 'Videos'},
    #         {'title': 'Family Movie Night', 'ISBN': '432-1-098765-4', 'author': 'Family Film Producers', 'genre': 'Family', 'type': 'Videos'},

    #         # Software
    #         {'title': 'Productivity Suite', 'ISBN': '876-5-432109-8', 'author': 'Software Company', 'genre': 'Productivity', 'type': 'Software'},
    #         {'title': 'Security Essentials', 'ISBN': '765-4-321098-7', 'author': 'Security Software Inc.', 'genre': 'Security', 'type': 'Software'},
    #         {'title': 'Graphic Design Pro', 'ISBN': '654-3-210987-6', 'author': 'Design Software Co.', 'genre': 'Graphic Design', 'type': 'Software'},
    #         {'title': 'Video Editing Master', 'ISBN': '543-2-109876-5', 'author': 'Video Editing Solutions', 'genre': 'Video Editing', 'type': 'Software'},
    #         {'title': 'Gaming Paradise', 'ISBN': '432-1-098765-4', 'author': 'Gaming Software Corp.', 'genre': 'Gaming', 'type': 'Software'},

    #         # Add more dummy books as needed
    #     ]

    # )
#     db.profileCollection.insert_many([
#     {'name': 'Michael', 'age': 28, 'gender': 'Male', 'contact no': 2345678901, 'address': 'Town1'},
#     {'name': 'Emily', 'age': 35, 'gender': 'Female', 'contact no': 8765432109, 'address': 'Town2'},
#     {'name': 'Daniel', 'age': 22, 'gender': 'Male', 'contact no': 3456789012, 'address': 'City3'},
#     {'name': 'Sophia', 'age': 29, 'gender': 'Female', 'contact no': 7654321098, 'address': 'City4'},
#     {'name': 'Ethan', 'age': 31, 'gender': 'Male', 'contact no': 4567890123, 'address': 'Village1'},
#     {'name': 'Olivia', 'age': 27, 'gender': 'Female', 'contact no': 6543210987, 'address': 'Village2'},
#     {'name': 'Alexander', 'age': 26, 'gender': 'Male', 'contact no': 5678901234, 'address': 'Town5'},
#     {'name': 'Ava', 'age': 33, 'gender': 'Female', 'contact no': 8901234567, 'address': 'City6'},
#     {'name': 'William', 'age': 24, 'gender': 'Male', 'contact no': 6789012345, 'address': 'Village3'},
#     {'name': 'Isabella', 'age': 32, 'gender': 'Female', 'contact no': 9012345678, 'address': 'Village4'}
# ])

    response = db.booksCollection.find()
    for data in response:
        print(data)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)