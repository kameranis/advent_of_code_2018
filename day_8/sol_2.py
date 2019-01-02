data = [int(i) for i in input().split()]

class Node:
    def __init__(self, data, i):
        self.children = []
        self.metadata = []
        self.children_count = data[i]
        i += 1
        self.metadata_count = data[i]
        i += 1
        for _ in range(self.children_count):
            self.children.append(Node(data, i))
            i = self.children[-1].last_index
        for _ in range(self.metadata_count):
            self.metadata.append(data[i])
            i += 1
        self.last_index = i
        self.score = None

    def get_score(self):
        if self.score is not None:
            return self.score
        if len(self.children) == 0:
            return sum(self.metadata)
        score = 0
        for child in self.metadata:
            if child > len(self.children):
                continue
            score += self.children[child - 1].get_score()
        return score


root = Node(data, 0)
print(root.get_score())

