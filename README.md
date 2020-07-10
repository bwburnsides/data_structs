# data_structs
Pythonic implementations of classical data structures

## bst.py

Includes an implementation of a binary search tree that heavily relies on recursion.
The basic insert, access, and deletion operations are supported. Special methods are
implemented to provide a Python interface:

            >>> # initialize with any number of elements (even 0)
            >>> tree = BST(12, 10, 15, 13, 16, 19, 20)
            >>> tree.insert(14)
            >>> 13 in tree  # 'contains' syntax
            True
            >>> tree[13]  # 'subscript' syntax
            Node
            Val: 13
            Left: None
            Right: 14
            >>> len(tree)  # 'len' syntax for num of elements
            8
            >>> del tree[10] # 'delitem' syntax for node deletion