# Recursive search of binary tree
def tree_search(root, val, rank):
    if not root:
        return
    if root.value == val:
        print(f'Found {val} in rank {rank}'); return
    else:
        if root.left:
            tree_search(root.left, val, rank)
        if root.right:
            tree_search(root.right, val, rank)

# Parallellized recursive search of binary tree
def parallel_tree_search(root, val, rank, size):
    if size == 1:
        tree_search(root, val, rank)

    elif size == 2:
        if rank == 0:
            if root.value == val: print(f'Found {val} in rank {rank}'); return
            tree_search(root.left, val, rank)
        if rank == 1:
            tree_search(root.right, val, rank)
    
    elif size == 3:
        if rank == 0:
            if root.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.value == val: print(f'Found {val} in rank {rank}'); return
            tree_search(root.left.left, val, rank)
        if rank == 1:
            tree_search(root.left.right, val, rank)
        if rank == 2:
            tree_search(root.right, val, rank)
    
    elif size == 4:
        if rank == 0:
            if root.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.right.value == val: print(f'Found {val} in rank {rank}'); return
            tree_search(root.left.left, val, rank)
        if rank == 1:
            tree_search(root.left.right, val, rank)
        if rank == 2:
            tree_search(root.right.left, val, rank)
        if rank == 3:
            tree_search(root.right.right, val, rank)
        
    elif size == 5:
        if rank == 0:
            if root.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.right.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.left.value == val: print(f'Found {val} in rank {rank}'); return
            tree_search(root.left.left.left, val, rank)
        if rank == 1:
            tree_search(root.left.left.right, val, rank)
        if rank == 2:
            tree_search(root.left.right, val, rank)
        if rank == 3:
            tree_search(root.right.left, val, rank)
        if rank == 4:
            tree_search(root.right.right, val, rank)

    elif size == 6:
        if rank == 0:
            if root.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.right.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.right.value == val: print(f'Found {val} in rank {rank}'); return; return
            tree_search(root.left.left.left, val, rank)
        if rank == 1:
            tree_search(root.left.left.right, val, rank)
        if rank == 2:
            tree_search(root.left.right.left, val, rank)
        if rank == 3:
            tree_search(root.left.right.right, val, rank)
        if rank == 4:
            tree_search(root.right.left.left, val, rank)
        if rank == 5:
            tree_search(root.right.left.right, val, rank)
    
    elif size == 7:
        if rank == 0:
            if root.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.right.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.right.value == val: print(f'Found {val} in rank {rank}'); return
            if root.right.left.value == val: print(f'Found {val} in rank {rank}'); return
            tree_search(root.left.left.left, val, rank)
        if rank == 1:
            tree_search(root.left.left.right, val, rank)
        if rank == 2:
            tree_search(root.left.right.left, val, rank)
        if rank == 3:
            tree_search(root.left.right.right, val, rank)
        if rank == 4:
            tree_search(root.right.left.left, val, rank)
        if rank == 5:
            tree_search(root.right.left.right, val, rank)
        if rank == 6:
            tree_search(root.right.right.left, val, rank)

    elif size == 8:
        if rank == 0:
            if root.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.right.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.left.right.value == val: print(f'Found {val} in rank {rank}'); return
            if root.right.left.value == val: print(f'Found {val} in rank {rank}'); return
            if root.right.right.value == val: print(f'Found {val} in rank {rank}'); return
            tree_search(root.left.left.left, val, rank)
        if rank == 1:
            tree_search(root.left.left.right, val, rank)
        if rank == 2:
            tree_search(root.left.right.left, val, rank)
        if rank == 3:
            tree_search(root.left.right.right, val, rank)
        if rank == 4:
            tree_search(root.right.left.left, val, rank)
        if rank == 5:
            tree_search(root.right.left.right, val, rank)
        if rank == 6:
            tree_search(root.right.right.left, val, rank)
        if rank == 7:
            tree_search(root.right.right.right, val, rank)