from test770.lib import whats_my_name

def test_who_am_i():

    res = whats_my_name()

    assert "Djobet" in res.split()
