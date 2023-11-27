# test_profile_search_ui.py
import pytest
from main import ProfileSearchUI
from pprint import pprint
import logging
import tkinter as tk
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def profile_search_ui():
    root = tk.Tk()
    return ProfileSearchUI(root)

def test_user_choice(profile_search_ui):
    # Define the switch_dict before using it
    switch_dict = {
        1: test_search_by_name,
        2: test_search_by_age,
        3: test_search_by_gender,
        # Add other cases as needed
    }

    # Get user input to determine which case to execute
    choice = int(input("Enter your choice (1 for name, 2 for age, 3 for gender): "))

    # Execute the chosen case
    if choice in switch_dict:
        switch_dict[choice]
    else:
        print("Invalid choice")

def test_search_by_name(profile_search_ui):
    query = input("Enter name:")
    criteria = "Name"
    result = profile_search_ui.profile_search_function(query, criteria)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result, width=1)
    print()

def test_search_by_age(profile_search_ui):
    query = input("Enter age:")
    criteria = "Age"
    result = profile_search_ui.profile_search_function(query, criteria)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result)
    print()


def test_search_by_gender(profile_search_ui):
    query = input("Enter gender:")
    criteria = "Gender"
    result = profile_search_ui.profile_search_function(query, criteria)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result)
    print()


def test_search_by_Contactno(profile_search_ui):
    query = input("Enter Contact no:")
    criteria = "Contact no"
    result = profile_search_ui.profile_search_function(query, criteria)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result)
    print()



def test_search_by_address(profile_search_ui):
    query = input("Enter address:")
    criteria = "Address"
    result = profile_search_ui.profile_search_function(query, criteria)
    assert len(result) > 0, f"No results found for '{query}' (Criteria: {criteria})"
    pprint(result)
    print()


