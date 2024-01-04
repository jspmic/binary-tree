class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(node: Node) -> int:
    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


def size(node: Node) -> int:
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


# Non-optimal definition of a tree
def definition() -> Node:
    n1 = Node(5)
    n2 = Node(6)
    n3 = Node(4)
    n4 = Node(11)
    n5 = Node(15)
    n6 = Node(29)
    n7 = Node(13)

    n1.left = n2
    n1.right = n3

    n2.left = n4
    n2.right = n5

    n3.left = n6
    n3.right = n7

    return n1


if __name__ == "__main__":
    print(f"Height: {height(n1)}")
    print(f"Size: {size(n1)}")
    exit(0)
