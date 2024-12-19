import pytest
from main import hello_world, greet_person

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_greet_person():
    assert greet_person("Alice") == "Hello, Alice!"
