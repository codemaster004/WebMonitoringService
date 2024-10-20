
class UnsupportedSelectorsFormat(Exception):
    def __init__(self, message):
        self.message = f"Provided CSS selector do not match the currently supported standard. {message}"
        super().__init__(self.message)

