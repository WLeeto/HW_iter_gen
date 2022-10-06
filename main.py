nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, data_list):
        self.data = data_list
        self.len = len(data_list)

    def __iter__(self):
        self.cursor = -1
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i == len(self.data[self.cursor]):
            # if self.i == len(self.data[self.cursor]):
            self.cursor += 1
            self.i = -1
            if self.cursor == self.len:
                raise StopIteration

        return self.data[self.cursor][self.i]


def flat_generator(nested_list):
    for i in nested_list:
        for j in i:
            yield j


if __name__ == "__main__":
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)

