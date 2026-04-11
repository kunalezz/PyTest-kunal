import pytest

# Normal markers
'''@pytest.mark.regression
def test_change():
    assert "hello" == "hello", 'Not Equal'
    assert  5==5, 'Not Equal'

@pytest.mark.regression
def test_comparision():
    assert 45 >= 33 , "Not greater than"
    # assert 22 >= 33 , "Not greater than"

@pytest.mark.regression
def test_membership():
    l = [1,2,3]
    assert  3 in l, 'Not in the list'''


'''# Inbuild markers
@pytest.mark.skip
def test_login():
    print("Logging in...")
    assert 'hello' == 'hello'
    assert 'world' == 'world'

@pytest.mark.smoke
def test_logout():
    print("Logging out...")
    ls = [1,2,3,4,5]
    2 in ls
    print( 2 in ls)

@pytest.mark.skipif(5==5, reason="Not working")
def test_register():
    print("Logging in...")
    ls = [1, 2, 3, 4, 5]
    assert (2 in ls) == True'''


# Parameterize marker ->
@pytest.mark.parametrize('a,b', [(1,2), (3,4), (5,6)])
def test_sum(a,b):
    print(a+b)

