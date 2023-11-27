# test_library_search_ui.py

import pytest
from main import LibrarySearchUI
import logging
import tkinter as tk  # Add this line to import the tk module
#from library_search_ui import SearchSystem
from pprint import pprint

# Configure logging
logging.basicConfig(level=logging.INFO)


@pytest.fixture
def library_search_ui():
    root = tk.Tk()
    return LibrarySearchUI(root)

def test_user_choice(library_search_ui):
    # Define the switch_dict before using it
    switch_dict = {
        1: test_search_by_author,
        2: test_search_by_ISBN,
        3: test_search_by_title,
        # Add other cases as needed
    }

    # Get user input to determine which case to execute
    choice = int(input("Enter your choice (1 for title, 2 for ISBN, 3 for author): "))

    # Execute the chosen case
    if choice in switch_dict:
        switch_dict[choice]
    else:
        print("Invalid choice")


def test_search_by_title(library_search_ui):
    query = input("Enter book name:")
    criteria = "Title"
    item_type = "All"
    result1 = library_search_ui.library_search_function(query, criteria,item_type)
    assert len(result1) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result1)
    print()

    

def test_search_by_ISBN(library_search_ui):
    query = input("Enter ISBN :")
    criteria = "ISBN"
    item_type = "All"
    result = library_search_ui.library_search_function(query, criteria,item_type)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result)
    print()



def test_search_by_author(library_search_ui):
    query = input("Enter Author :")
    criteria = "Author"
    item_type = "All"
    result = library_search_ui.library_search_function(query, criteria,item_type)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result)
    print()


def test_test_search_by_genre(library_search_ui):
    query = input("Enter genere :")
    criteria = "Genre"
    item_type = "All"
    result = library_search_ui.library_search_function(query, criteria,item_type)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result)
    print()


def test_search_all_criteria(library_search_ui):
    query = "The Great Gatsby"
    criteria = "All"
    item_type = "All"
    result = library_search_ui.library_search_function(query, criteria,item_type)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    #pprint(result)

def test_search_by_Type(library_search_ui):
    query = "The Great Gatsby"
    criteria = "Type"
    item_type =input("Enter categories (Books,CDs,Magazines,Videos,Software) ")
    result = library_search_ui.library_search_function(query, criteria,item_type)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria}, Type: {item_type})"
    pprint(result)
    print()


