from lib.parrot import parrot

def test_parrot():
    result = parrot("Hello, World!")  # Pass a string argument to the parrot function
    assert result == "Hello, World!"
