# data_structs
Pythonic implementations of classical data structures.

## expr.py

Create and operate on binary expression trees that represent algebraic expressions. Inspired by a Computerphile video.

Includes abstract classes defining generic algebraic expressions, and concrete classes that include the abstract's implementation. Expressions include neatly formatted `repr()`s and can be evaluated.

This is my first time combining many topics such as Abstract Base Classes, Multiple Inheritance, and Inheritance into a single project.

The abstract base `Expression()` includes Python special methods for easily creating complex expressions using the built-in operators.

This project could form the basis for a graphical differentiation or integration program, where resultant expression is shown at each step of the solution.

            >>> Add(Constant(3), Variable("x"))
            (3 + x)
            >>> # or:
            >>> Constant(3) + Variable("x")
            (3 + x)
            >>> e = ((Constant(3) * Variable("y")) / (Constant(2) * Variable("x"))) * Factorial(Constant(3))
            >>> e.eval({"x": 3, "y": 2})
            6.0

## bst.py

Includes an implementation of a binary search tree that heavily relies on recursion.
The basic insert, access, and deletion operations are supported. Special methods are
implemented to provide a Python interface:

            >>> # initialize with any number of elements (even 0)
            >>> tree = BST(12, 10, 15, 13, 16, 19, 20)
            >>> tree.insert(14)  # proper insertion after the creation
            >>> 13 in tree  # 'contains' syntax
            True
            >>> tree[13]  # 'subscript' syntax
            Node
            Val: 13
            Left: None
            Right: 14
            >>> len(tree)  # 'len' syntax for num of elements in BST
            8
            >>> del tree[10] # 'delitem' syntax for node deletion