# Import the necessary modules
from flask import Flask, render_template, request, send_file  # Flask modules for web app
from graphviz import Digraph  # To generate graphs
import json  # To parse JSON
import networkx as nx  # For graph operations
import io  # Input/output operations
from base64 import b64encode;  # this is to allow the image to appear under the input area

from data import *  # Importing data

# Convert the JSON data into a Python object
data = json.loads(raw)

# Function to plot a graph from a given graph object
def plot_graph(g):
    plot = Digraph("course_prereqs1", format='png')  # Create a Digraph object
    for v in g.nodes:  # For each node in the graph
        # Add the node to the plot with a tooltip if data is available
        plot.node(v, tooltip=data[v]["title"] if v in data else "")
    for u, v in g.edges():  # For each edge in the graph
        # Add the edge to the plot
        plot.edge(u, v)
    plot_data = plot.pipe(format='png')  # Generate PNG data from the plot
    return io.BytesIO(plot_data)  # Return the PNG data as a bytes object

# Create a new directed graph
G = nx.DiGraph()

# Populate the graph with data
for code, vals in data.items():  # For each item in the data
    for vi in vals["first"]:  # For each item in the "first" value of the data item
        # Add an edge to the graph
        G.add_edge(vi, code)

# Create a new Flask web application
app = Flask(__name__)

# Define a route for the web app (the main and only page)
@app.route('/', methods=['GET', 'POST'])  # This route will accept both GET and POST requests
def serve_image():
    # If the request is a POST request (i.e., the form was submitted)
    if request.method == 'POST':
        # Get the course code from the form
        course_code = request.form['course']
        # If the course code is not in the graph, return an error message
        if course_code not in G.nodes:
            return "Invalid course code entered"

        # Generate the subgraph based on the entered course code
        connected_nodes = list(nx.bfs_tree(G, source=course_code))
        subgraph = G.subgraph(connected_nodes)
        # Generate the image from the subgraph
        img_io = plot_graph(subgraph)

        # convert eh BytesIO object to a base64 string
        img_b64 = b64encode(img_io.getvalue()).decode()

        # pass the base 64 string to the template
        return render_template('index.html', img_data=img_b64)

        # # Return the image as a response
        # return send_file(img_io, mimetype='image/png')
    else:
        # If the request is a GET request (i.e., the page was accessed normally)
        # Render and return the form page
        return render_template('index.html')

# If the file is being run directly (not being imported)
if __name__ == '__main__':
    # Run the Flask web application on port 8000
    app.run(port=8000)
