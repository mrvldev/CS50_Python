from hello import hello

def test_default():
    assert hello("Alice") == "hello, Alice"

def test_argument():
    assert hello() == "hello, world"