# main_file.py

import tkinter as tk
from tkinter import ttk

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
password = quote_plus('USERNAME@123')
uri = "mongodb+srv://USERNAME:" + password + "@cluster0.n4i3ipr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['LibrarySearch']


def library_search_ui():
    root = tk.Tk()
    return LibrarySearchUI(root)
class LibrarySearchUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Search System")
        

        # Search Entry
        self.search_entry = tk.Entry(root, width=40)
        self.search_entry.grid(row=3, column=0, padx=1, pady=5)

        # Criteria Combobox
        self.criteria_label = tk.Label(root, text="Search by:")
        self.criteria_label.grid(row=2, column=1, padx=10, pady=10)
        self.criteria_combobox = ttk.Combobox(root, values=["All", "Title", "Author", "ISBN", "Genre"])
        self.criteria_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.criteria_combobox.set("All")

        # Type Combobox
        self.type_label = tk.Label(root, text="Filter by Type:")
        self.type_label.grid(row=2, column=2, padx=10, pady=10)
        self.type_combobox = ttk.Combobox(root, values=["All", "Books", "CDs", "Magazines", "Videos", "Software"])
        self.type_combobox.grid(row=3, column=2, padx=10, pady=10)
        self.type_combobox.set("All")

        # Search Button
        self.search_button = tk.Button(root, text="🔍 Search", command=self.perform_search)
        self.search_button.grid(row=3, column=3, padx=10, pady=10)
        self.root.bind("<Return>", lambda event: self.perform_search())

        # Search Results Table
        self.results_table = ttk.Treeview(root, columns=("Title", "Author", "ISBN", "Genre", "Type"))
        self.results_table.heading("Title", text="Title")
        self.results_table.heading("Author", text="Author")
        self.results_table.heading("ISBN", text="ISBN")
        self.results_table.heading("Genre", text="Genre")
        self.results_table.heading("Type", text="Type")
        self.results_table.grid(row=5, column=0, columnspan=4, padx=10, pady=50)

        # ... (Rest of the code for LibrarySearchUI)

        #fetch data
        bookList = []
        response = db.booksCollection.find()
        for data in response:
            bookList.append(data)
        self.dummy_data = bookList
        self.display_search_results(self.dummy_data)

    def perform_search(self):
        # Perform search based on the criteria and type selected
        search_query = self.search_entry.get()
        criteria = self.criteria_combobox.get()
        item_type = self.type_combobox.get()

        # For demonstration purposes, let's assume there's a library search function
        # that returns a list of items matching the search criteria
        search_results = self.library_search_function(search_query, criteria, item_type)
        filtered_results = []
        for result in search_results:
            if item_type == "All" or result['type'].lower() == item_type.lower():
                filtered_results.append(result)

        # Display the results in the table
        self.display_search_results(filtered_results)

    def library_search_function(self, query, criteria, item_type):
        # Implement your library search function here
        # For the sake of example, returning dummy data
        if criteria == "Title":
            # Search for a specific book by title
            return [item for item in self.dummy_data if item['title'].lower() == query.lower() and (item_type == "All" or item['type'].lower() == item_type.lower())]
        elif criteria == "Author":
            # Search for books by author
            return [item for item in self.dummy_data if item['author'].lower() == query.lower() and (item_type == "All" or item['type'].lower() == item_type.lower())]
        elif criteria == "ISBN":
            # Search for books by ISBN
            return [item for item in self.dummy_data if item['ISBN'].lower() == query.lower() and (item_type == "All" or item['type'].lower() == item_type.lower())]
        elif criteria == "Genre":
            # Search for books by genre
            return [item for item in self.dummy_data if item['genre'].lower() == query.lower() and (item_type == "All" or item['type'].lower() == item_type.lower())]
        elif criteria == "Type":
            # Filter by book type
            return [item for item in self.dummy_data if item_type == "All" or item['type'].lower() == item_type.lower()]
        else:
            # If criteria is not recognized, return the entire collection
            return self.dummy_data

    def display_search_results(self, results):
        # Clear existing results
        # (You'll need to adapt this part based on your actual Treeview setup)
        for row in self.results_table.get_children():
            self.results_table.delete(row)

        # Insert new results
        # (You'll need to adapt this part based on your actual Treeview setup)
        for index, result in enumerate(results, start=1):
            self.results_table.insert("", "end", values=(result['title'], result['author'], result['ISBN'], result['genre'], result['type']))


class DummyData:
    profiles = []
    response = db.profileCollection.find()
    for data in response:
        profiles.append(data)
    dummy_profiles = profiles

    def profile_search_ui():
        root = tk.Tk()
        return ProfileSearchUI(root)
class ProfileSearchUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Profile Search")

        # ... (Rest of the code for ProfileSearchUI)
        self.search_entry = tk.Entry(root, width=40)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10)

        # Criteria Combobox
        self.criteria_label = tk.Label(root, text="Search by:")
        self.criteria_label.grid(row=0, column=1, padx=10, pady=10)
        self.criteria_combobox = ttk.Combobox(root, values=["All", "Name", "Age", "Gender", "Contact no", "Address"])
        self.criteria_combobox.grid(row=0, column=2, padx=10, pady=10)
        self.criteria_combobox.set("All")

        # Search Button
        self.search_button = tk.Button(root, text="🔍 Search", command=self.profile_search)
        self.search_button.grid(row=0, column=3, padx=10, pady=10)
        self.root.bind("<Return>", lambda event: self.profile_search())

        # Results Table
        self.results_table = ttk.Treeview(root, columns=("Name", "Age", "Gender", "Contact no", "Address"))
        self.results_table.heading("Name", text="Name")
        self.results_table.heading("Age", text="Age")
        self.results_table.heading("Gender", text="Gender")
        self.results_table.heading("Contact no", text="Contact no")
        self.results_table.heading("Address", text="Address")
        self.results_table.grid(row=1, column=0, columnspan=4, padx=10, pady=50)

    
        # Dummy data
        self.dummy_data = DummyData.dummy_profiles
        # Display initial dummy data
        self.display_profile_search_results(self.dummy_data)

    def profile_search(self):
        # Perform search based on the criteria selected
        search_query = self.search_entry.get()
        criteria = self.criteria_combobox.get()

        # Filter profiles based on the search criteria
        search_results = self.profile_search_function(search_query, criteria)
        filtered_results = []
        for result in search_results:
            filtered_results.append(result)
        self.display_profile_search_results(filtered_results)
        

    def profile_search_function(self, query, criteria):
        # Implement your profile search function here
        # For the sake of example, returning dummy data
        if criteria == "Name":
            # Search for profiles by name
            return [profile for profile in self.dummy_data if profile['name'].lower() == query.lower()]
        elif criteria == "Age":
            # Search for profiles by age
            return [profile for profile in self.dummy_data if str(profile['age']) == query]
        elif criteria == "Gender":
            # Search for profiles by gender
            return [profile for profile in self.dummy_data if profile['gender'].lower() == query.lower()]
        elif criteria == "Contact no":
            # Search for profiles by contact number
            return [profile for profile in self.dummy_data if str(profile['contact no']) == query]
        elif criteria == "Address":
            # Search for profiles by address
            return [profile for profile in self.dummy_data if profile['address'].lower() == query.lower()]
        elif criteria == "All":
            # Return all profiles
            return self.dummy_data
        else:
            # If criteria is not recognized, return an empty list
            return []

    def display_profile_search_results(self, results):
        # Clear existing results
        # (You'll need to adapt this part based on your actual Treeview setup)
        for row in self.results_table.get_children():
            self.results_table.delete(row)

        # Insert new results
        # (You'll need to adapt this part based on your actual Treeview setup)
        for index, result in enumerate(results, start=1):
            self.results_table.insert("", "end", values=(result['name'], result['age'], result['gender'], result['contact no'], result['address']))

if __name__ == "__main__":
    root = tk.Tk()

    # Create an instance of the LibrarySearchUI class
    library_search_ui_instance = LibrarySearchUI(root)

    # Create an instance of the ProfileSearchUI class
    profile_search_ui_instance = ProfileSearchUI(root)

    # Additional logic or interactions between the UIs can be added here

    root.mainloop()
