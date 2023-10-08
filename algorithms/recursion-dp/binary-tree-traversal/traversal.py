# Recursive traversal of binary tree
def tree_traversal(root):
    print(root.value)
    if root.left:
        tree_traversal(root.left)
    if root.right:
        tree_traversal(root.right)

# Parallellized traversal of binary tree
def parallel_tree_traversal(root, rank, size):
    if size == 1:
        tree_traversal(root)

    if size == 2:
        if rank == 0:
            print(root.value)
            tree_traversal(root.left)
        if root.right and rank == 1:
            tree_traversal(root.right)
    
    if size == 3:
        if rank == 0:
            print(root.value)
            print(root.left.value)
            tree_traversal(root.left.left)
        if rank == 1:
            tree_traversal(root.left.right)
        if rank == 2:
            tree_traversal(root.right)
    
    if size == 4:
        if rank == 0:
            print(root.value)
            print(root.left.value)
            print(root.right.value)
            tree_traversal(root.left.left)
        if rank == 1:
            tree_traversal(root.left.right)
        if rank == 2:
            tree_traversal(root.right.left)
        if rank == 3:
            tree_traversal(root.right.right)

    if size == 5:
        if rank == 0:
            print(root.value)
            print(root.left.value)
            print(root.right.value)
            print(root.left.left.value)
            tree_traversal(root.left.left.left)
        if rank == 1:
            tree_traversal(root.left.left.right)
        if rank == 2:
            tree_traversal(root.left.right)
        if rank == 3:
            tree_traversal(root.right.left)
        if rank == 4:
            tree_traversal(root.right.right)

    if size == 6:
        if rank == 0:
            print(root.value)
            print(root.left.value)
            print(root.right.value)
            print(root.left.left.value)
            print(root.left.right.value)
            tree_traversal(root.left.left.left)
        if rank == 1:
            tree_traversal(root.left.left.right)
        if rank == 2:
            tree_traversal(root.left.right.left)
        if rank == 3:
            tree_traversal(root.left.right.right)
        if rank == 4:
            tree_traversal(root.right.left)
        if rank == 5:
            tree_traversal(root.right.right)
    
    if size == 7:
        if rank == 0:
            print(root.value)
            print(root.left.value)
            print(root.right.value)
            print(root.left.left.value)
            print(root.left.right.value)
            print(root.right.left.value)
            tree_traversal(root.left.left.left)
        if rank == 1:
            tree_traversal(root.left.left.right)
        if rank == 2:
            tree_traversal(root.left.right.left)
        if rank == 3:
            tree_traversal(root.left.right.right)
        if rank == 4:
            tree_traversal(root.right.left.left)
        if rank == 5:
            tree_traversal(root.right.left.right)
        if rank == 6:
            tree_traversal(root.right.right)

    if size == 8:
        if rank == 0:
            print(root.value)
            print(root.left.value)
            print(root.right.value)
            print(root.left.left.value)
            print(root.left.right.value)
            print(root.right.left.value)
            print(root.right.right.value)
            tree_traversal(root.left.left.left)
        if rank == 1:
            tree_traversal(root.left.left.right)
        if rank == 2:
            tree_traversal(root.left.right.left)
        if rank == 3:
            tree_traversal(root.left.right.right)
        if rank == 4:
            tree_traversal(root.right.left.left)
        if rank == 5:
            tree_traversal(root.right.left.right)
        if rank == 6:
            tree_traversal(root.right.right.left)
        if rank == 7:
            tree_traversal(root.right.right.right)