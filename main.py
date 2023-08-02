# from graphviz import Digraph
# import json
# import networkx as nx
# from IPython.display import display  # Import the display function
#
# from data import *
#
# data = json.loads(raw)
#
#
# # displays everything I think... (from cs courses)
# def plot_graph(g):
#     plot = Digraph("course_prereqs1", format='png')  # previous format was svg. Changed to png.
#     for v in g.nodes:
#         plot.node(v, tooltip=data[v]["title"] if v in data else "")
#     for u, v in g.edges():
#         plot.edge(u, v)
#     # display(plot)
#     # plot.render()
#     plot.render('course_prereqs1', view=True)  # Save the graph to a file and open it
#
#
# G = nx.DiGraph()
#
# for code, vals in data.items():
#     for vi in vals["first"]:
#         G.add_edge(vi, code)
#
# # code below allows me to see everything starting with CSC108 only.
# # Select the subgraph with CSC108H1 and all its connected nodes
# connected_nodes = list(nx.bfs_tree(G, source='CSC209H1'))
# subgraph = G.subgraph(connected_nodes)
# # Plot the subgraph
#
# if __name__ == '__main__':
#     # print(data)  # prints the raw data I have. (json.loads(raw))
#     # plot_graph(G)
#
#     # Plot the subgraph
#     plot_graph(subgraph)
