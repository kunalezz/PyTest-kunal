# #without writing test before the function name PyTest will not test this function
# def test_register():
#     print('Registering...')
# def test_login():
#     print('Logging in...')
# def test_logout():
#     print('Logged out...')


class Test_Demo:
    test_pop = None
    # def __init__ (self):
    #     pass
    def test_register(self):
        print('Registering...')
    def test_login(self):
        print('Logging in...')
    def test_logout(self):
        print('Logged out...')


# def test_login():
#     print("Logging in...")
#
#
# def test_logout():
#     print("Logging out...")
#
#
# def test_register():
#     print("Registering...")
class TestDemo:
    def __init__(self):
        # print("TestDemo has started!!!!")
        pass
    def test_login(self):
        print("Logging in...")
    def test_logout(self):
        print("Logging out...")
    def test_register(self):
        print("Registering...")

# obj1=TestDemo

# PyTest is a unit testing framework. Test files should either start with test_ or end with _test.py. Test functions must always start with test_. When these naming conventions are followed, PyTest automatically discovers and executes the test files, functions, and classes without requiring explicit function calls.
# and without creating the object we can execute the class
# -v stands for verbosity it gives the detailed description of the code
# -s stands for scripting, it will print all the print statements
# if it doesnt start with test python wont recognise the functions
# in case of test classes we need not create the obj and call the functions, if we do so, execution will happen twice