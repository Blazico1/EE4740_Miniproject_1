from graphviz import Digraph

# Function to generate DOT representation of the tree
def generate_dot(node):
    print("Generating DOT representation of the tree...")
    dot = Digraph()
    dot.attr(rankdir='LR')
    def add_nodes_edges(node, dot):
        if dot is None:
            dot = Digraph()

        if node.left is None and node.right is None:
            # This is a leaf node
            dot.node(name=str(id(node)), label=f"{node.symbol}\n{node.frequency}", shape='box')
        else:
            # This is an internal node
            dot.node(name=str(id(node)), label="", width="0.1", height="0.1")

        if node.left:
            dot.edge(str(id(node)), str(id(node.left)), label="0")
            add_nodes_edges(node.left, dot)

        if node.right:
            dot.edge(str(id(node)), str(id(node.right)), label="1")
            add_nodes_edges(node.right, dot)

        return dot

    dot = add_nodes_edges(node, dot)
    return dot
