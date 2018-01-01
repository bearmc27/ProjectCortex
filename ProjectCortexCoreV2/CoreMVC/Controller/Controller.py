class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def print_something(self, msg):
        print(msg)
