from src.waitlist import Waitlist

def test_join_and_to_list_and_len():
    w = Waitlist()
    w.join("a"); w.join("b"); w.join("c")
    assert w.to_list() == ["a", "b", "c"]
    assert len(w) == 3

def test_find_and_cancel():
    w = Waitlist()
    for n in ["a", "b", "c", "b"]:
        w.join(n)
    assert w.find("c")
    assert w.cancel("b") is True
    assert w.to_list() == ["a", "c", "b"]
    assert w.cancel("x") is False
    assert w.to_list() == ["a", "c", "b"]

def test_bump():
    w = Waitlist()
    for n in ["a", "b", "c", "d"]:
        w.join(n)
    assert w.bump("c") is True
    assert w.to_list() == ["c", "a", "b", "d"]
    assert w.bump("z") is False