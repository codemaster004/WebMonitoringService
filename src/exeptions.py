
class UnsupportedSelectorsFormat(Exception):
    def __init__(self):
        self.message = "Provided css selector do not match the currently supported standard."
        super().__init__(self.message)

