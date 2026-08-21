class Test:
    def __new__(cls):
        return None

    def __init__(self):
        print("Init called")

t = Test()