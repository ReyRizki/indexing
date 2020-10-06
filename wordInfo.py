class wordInformation(object):
    def __init__(self, word):
        self.word = word
        self.indexes = {}

    def insertIndex(self, file_number, index):
        if file_number not in self.indexes.keys():
            self.indexes[file_number] = []

        self.indexes[file_number].append(index)