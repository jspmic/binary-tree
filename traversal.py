from trees import Node, definition

NODE = definition() # Tree used as an example


# For depth-first traversal
def inorder_trav(node: Node) -> list[int]:
    if node is None:
        return []
    return inorder_trav(node.left) + [node.value] + inorder_trav(node.right)

def preorder_trav(node: Node) -> list[int]:
    if node is None:
        return []

    return [node.value] + preorder_trav(node.left) + preorder_trav(node.right)

def postorder_trav(node: Node) -> list[int]:
    if node is None:
        return []

    return postorder_trav(node.left) + postorder_trav(node.right) + [node.value]

# For the breadth-first traversal
def level_trav(node: Node) -> list[int]:
    queue = []
    trav = [] # Array to store the traversal result
    queue.append(node)
    while queue:
        actual_node = queue.pop(0)
        if actual_node is not None:
            trav.append(actual_node.value)
            queue.append(actual_node.left)
            queue.append(actual_node.right)

    return trav


if __name__ == "__main__":
    print("For the Depth-first traversal\n----------------")
    print("In-order traversal: ", inorder_trav(NODE))
    print("Pre-order traversal: ", preorder_trav(NODE))
    print("Post-order traversal: ", postorder_trav(NODE))
    
    print("\nFor the Breadth-first traversal\n-----------------")
    print("Breadth-first traversal: ", level_trav(NODE))
    exit(0)
