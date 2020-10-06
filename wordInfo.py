class wordInformation(object):
    def __init__(self, word):
        self.word = word
        self.count = {}

    def increaseCount(self, file_name):
        if file_name not in self.count.keys():
            self.count[file_name] = 0

        self.count[file_name] += 1