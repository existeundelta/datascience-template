class Wrapper(object):
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        return self.model.predict(data)
