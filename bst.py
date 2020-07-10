from typing import Optional


class Node:
    """ A basic node element in a binary tree."""

    def __init__(self, value: int = None, parent: "Node" = None) -> None:
        self.value = value
        self.parent = parent
        self.left_child: Optional["Node"] = None
        self.right_child: Optional["Node"] = None

    def __repr__(self) -> str:
        left = self.left_child.value if self.left_child is not None else None
        right = self.right_child.value if self.right_child is not None else None
        return f"Val: {self.value}\nLeft: {left}\nRight: {right}"

    @property
    def child_count(self):
        count = 0
        if self.left_child:
            count += 1
        if self.right_child:
            count += 1
        return count


class BST:
    """ A wrapper for Nodes.

        Contains methods for constructing and operating on non-balancing binary search trees.
    """

    def __init__(self, *initial_values: int, root: Optional[Node] = None) -> None:
        self.root = root
        for value in initial_values:
            self.insert(value)

    def __len__(self) -> int:
        """ Length of the BST.

            Use recursion to determine the number of nodes in the BST.
        """
        if self.root is None:
            return 0
        node_paths = []
        if self.root.left_child is not None:
            node_paths.append(self.root.left_child)
        if self.root.right_child is not None:
            node_paths.append(self.root.right_child)

        return 1 + self._node_count(node_paths)

    def _node_count(self, node_paths) -> int:
        """ Finds all children of nodes in node_paths.

            Uses recursion to find all nested children of given nodes.
        """
        count = 0
        for path in node_paths:
            count += 1

            child_node_paths = []
            if path.left_child is not None:
                child_node_paths.append(path.left_child)
            if path.right_child is not None:
                child_node_paths.append(path.right_child)

            if len(child_node_paths):
                count += self._node_count(child_node_paths)

        return count

    def insert(self, value: int) -> None:
        """ Add an integer to the BST.

            If no root is present, a root node is created.
        """
        if self.root is not None:
            return self._insert(value=value, current_node=self.root)
        self.root = Node(value)

    def _insert(self, value: int, current_node: Node) -> None:
        """ Recursive insertion search.

            Places a value in the BST using recursion.
        """
        # Traverse down the right if value is greater than current node's
        if value > current_node.value:
            # If there is no right child, insert the value
            if current_node.right_child is None:
                current_node.right_child = Node(value, parent=current_node)
            # Otherwise traverse down from that child node.
            else:
                self._insert(value, current_node=current_node.right_child)
        # Traverse down the left if value is lesser than current node's
        elif value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value, parent=current_node)
            else:
                self._insert(value, current_node=current_node.left_child)
        return

    def __getitem__(self, value: int) -> Optional[Node]:
        """ Find a node in a BST.

            Find the node with the given value in the BST.
        """
        if self.root is not None:
            return self._find(value, current_node=self.root)
        return None

    def _find(self, value: int, current_node: Node) -> Node:
        """ Recursive Node lookup.

            Uses recursion to find the BST node with the given value.
        """
        # Check for current node matching the value.
        if value == current_node.value:
            return current_node
        # Traverse down the right if greater than current node
        elif value > current_node.value:
            # If there is a right child, search from it
            if current_node.right_child is not None:
                return self._find(value, current_node=current_node.right_child)
        # Traverse down the left if lesser than the current node
        elif value < current_node.value:
            if current_node.left_child is not None:
                return self._find(value, current_node=current_node.left_child)

    def __delitem__(self, value: int) -> None:
        """ Delete a value in the BST.

            Finds the node with the given value and removes it from the BST.
        """
        target_node = self[value]
        if target_node:
            self._delete(target_node)

    def _delete(self, node: Node) -> None:
        """ Remove a node from the BST.

            Uses recursion to delete a node from the BST.
        """

        def find_minimum_node(node: Node) -> Node:
            mininum_node = node
            while mininum_node.left_child is not None:
                mininum_node = mininum_node.left_child
            return mininum_node

        # Deletion Case 1: The node has no children.
        # Delete the node from its parent.
        if node.child_count == 0:
            if node is node.parent.left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None

        # Deletion Case 2: The node has one child. Replace the node
        # with its child.  Update the parent's children.
        # Update the child's parent.
        elif node.child_count == 1:
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            if node.parent:
                if node is node.parent.left_child:
                    node.parent.left_child = child
                else:
                    node.parent.right_child = child
            else:
                self.root = child

            child.parent = node.parent

        # Deletion Case 3: The node has two children. Find the minimum
        # value in the right subtree, and replace the target node with it.
        # Remove the copied node.
        elif node.child_count == 2:
            replacement_node = find_minimum_node(node.right_child)
            node.value = replacement_node.value
            self._delete(replacement_node)

    def __contains__(self, value: int) -> bool:
        """ 'in' support for BST.

        >>> 7 in BST(5, 4, 7)
        True
        >>> 3 in BST(5, 4, 7)
        False
        """
        return bool(self[value])
