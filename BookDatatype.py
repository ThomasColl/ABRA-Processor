from amzsear import AmzSear


class BookDatatype:
    def __init__(self, amazonBookId):
        self.bookID = amazonBookId
        self.bookName = AmzSear(amazonBookId)


