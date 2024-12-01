import pytest
from library_item import LibraryItem

def test_library_item_initialization():
    item = LibraryItem("Shape of You", "Ed Sheeran", 5)
    assert item.song == "Shape of You"
    assert item.singer == "Ed Sheeran"
    assert item.rating == 5
    assert item.play_count == 0

def test_library_item_initialization_default_rating():
    item = LibraryItem("Perfect", "Ed Sheeran")
    assert item.rating == 0

def test_info_method():
    item = LibraryItem("Someone Like You", "Adele", 4)
    assert item.info() == "Someone Like You - Adele ****"
    item.rating = 0
    assert item.info() == "Someone Like You  - Adele "

def test_stars_method():
    item = LibraryItem("Shape of You", "Ed Sheeran")
    item.rating = 3
    assert item.stars() == "***"

    item.rating = 0
    assert item.stars() == ""
