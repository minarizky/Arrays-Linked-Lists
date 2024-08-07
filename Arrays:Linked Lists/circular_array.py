class CircularArray:
    def __init__(self):
        self.array = []
        self.start = 0

    def addItem(self, item):
        self.array.append(item)

    def getByIndex(self, index):
        if not self.array:
            return None
        return self.array[(self.start + index) % len(self.array)]

    def rotate(self, rotation):
        if self.array:
            self.start = (self.start - rotation) % len(self.array)

    def printArray(self):
        for i in range(len(self.array)):
            print(self.getByIndex(i))
