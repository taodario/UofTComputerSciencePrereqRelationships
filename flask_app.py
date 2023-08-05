# Import the necessary modules
import fontTools
from flask import Flask, render_template, request, \
    send_file  # Flask modules for web app
from graphviz import Digraph  # To generate graphs
import json  # To parse JSON
import networkx as nx  # For graph operations
import io  # Input/output operations
from base64 import \
    b64encode  # this is to allow the image to appear under the input area

from data import *  # Importing data

# Convert the JSON data into a Python object
data = json.loads(raw)


# Function to plot a graph from a given graph object
def plot_graph(g):
    plot = Digraph("course_prereqs1", format='png')  # Create a Digraph object

    # Set default font for the graph
    plot.attr('graph', fontname='Roboto')
    plot.attr('node', fontname='Roboto')
    plot.attr('edge', fontname='Roboto')

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
    for vi in vals[
        "first"]:  # For each item in the "first" value of the data item
        # Add an edge to the graph
        G.add_edge(vi, code)

# Create a new Flask web application
app = Flask(__name__)

# Define a route for the web app (the main and only page)
@app.route('/', methods=['GET',
                         'POST'])  # This route will accept both GET and POST requests
def serve_image():
    # If the request is a POST request (i.e., the form was submitted)
    if request.method == 'POST':
        # Get the course code from the form
        course_code = request.form['course']

        # Convert the course code to lower case and check only the first 6 characters
        course_prefix = course_code.lower()[:6]

        # Get list of course codes that match the prefix (also converted to lower case)
        matched_codes = [code for code in data if
                         code.lower().startswith(course_prefix)]

        # If the course code is not in the graph, return an error message
        if not matched_codes:
            return render_template('index.html',
                                   error="This course has no requisites, or you may have entered an invalid course code. Please try again")

        # if multiple matches, just choose the first one (modify as needed)
        course_code = matched_codes[0]

        # Generate the subgraph based on the entered course code
        connected_nodes = list(nx.bfs_tree(G, source=course_code))
        subgraph = G.subgraph(connected_nodes)
        # Generate the image from the subgraph
        img_io = plot_graph(subgraph)

        # convert eh BytesIO object to a base64 string
        img_b64 = b64encode(img_io.getvalue()).decode()

        # pass the base 64 string to the template
        return render_template('index.html', img_data=img_b64)

    else:
        # If the request is a GET request (i.e., the page was accessed normally)
        # Render and return the form page
        return render_template('index.html')


# If the file is being run directly (not being imported)
if __name__ == '__main__':
    # Run the Flask web application on port 8000
    app.run(port=8000)
