class Bar:
    def __init__(self, message):
        self.message = message

    def say(self):
        print(self.message)

__all__ = ['Bar']
