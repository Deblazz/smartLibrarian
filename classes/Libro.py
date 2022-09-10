class LIBRO:

    def __init__(self, _id, title, author, genre, borrower):
        self._id = _id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrower = borrower

    def __init__(self, title, author, genre, borrower):
        self.title = title
        self.author = author
        self.genre = genre
        self.borrower = borrower

    def toJson(self):
        return {"title": self.title, "author": self.author, "genre": self.genre, "borrower":self.borrower}