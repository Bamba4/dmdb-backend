class EmailAlreadyExistException(Exception):
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f"Email {self.email} already exist"
