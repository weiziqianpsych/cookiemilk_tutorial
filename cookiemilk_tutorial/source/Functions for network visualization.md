# Functions for network visualization

## draw()

`draw(graph, show=True, save=False, filename='filename', encoding='utf-8', canvas_size=(500, 500), node_font='sans-serif', node_fontsize=12, node_fontcolor='black', node_fillcolor='lightgrey', node_size=12, edge_color='#7ab8cc', edge_size=2, edge_distance=100, charge=-300, detailed=True)`

### Description    
Show and/or save a NetworkX Graph.

Based on d3.js (https://d3js.org/) and pywebview (https://github.com/r0x0r/pywebview).

### Arguments

`graph`: A NetworkX graph.

`show`: A Boolean value, the default value is True. If show=True, the visualized graph will be shown immediately in a pywebview window. If show=False, the visualized graph will not be shown until a draw(...show=True) is running. The graph is drawn using d3.js (version 3, i.e., d3v3) and is interactive. You can also modify the style of the graph by setting other parameters.

`save`: A Boolean, the default value is False. If save=True, the visualized graph will be saved in an HTML file. The visualized graph being saved is an SVG object in the HTML file. Scalable vector graphic (SVG) is a type of image format that can be opened by browser software such as Google Chrome, Microsoft Edge and Firefox, and can be further modified by figure drawing software such as Adobe Illustrator. Currently, `cookiemilk` can not save a graph as an SVG file directly, but you can extract it from the HTML file using some tools such as SVG Crowbar (please see: https://nytimes.github.io/svg-crowbar/).

`filename`: A string specifying the filename of the output HTML file. The default value is "filename", which will result in an HTML file called "filename.HTML".

`encoding`: A string specifying the encoding standard of the output HTML file. The default is "utf-8".

`canvas_size`: A list or tuple object specifying the size of the canvas. The default is (500, 500), which means 500×500 pixels and seems suitable for a graph containing 10-15 key-terms. If your graph is large (e.g., many nodes and edges), please try to set up a large canvas.

`node_font`: A string specifying the font of nodes in the graph. The default font is "sans-serif".

`node_fontsize`: A number specifying the size of node labels. The default value is 12.

`node_fontcolor`: A string specifying the colour of node labels. The string can be written in HEX format or just a colour name (as long as it is available in d3.js). The default value is "black".

`node_fillcolor`: A string specifying the colour of nodes. The default value is "lightgrey".

`node_size`: A number specifying the size of nodes in the graph. The default value is 12.

`edge_color`: A string specifying the colour of edges. The default value is "#7ab8cc".

`edge_size`: a number specifying the width of edges in the graphs. The default is 2.

`edge_distance`: a number specifying the distance among nodes. The default is 100.

`charge`: a number specifying the charge in the df_graphs. The default is -300.

`detailed`: A boolean, the default value is True. If detailed=True, there will be a printed message shown if the HTML file is saved successfully.

### Value
None.

### Examples
```
import cookiemilk

# import data
my_cmap = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data = cookiemilk.cmap2graph(file=my_cmap, data_type='pair', read_from_file=False)

# show the graph in a pywebview window
cookiemilk.draw(my_data)

# do not show the graph, but save it in an HTML file
cookiemilk.draw(my_data, show=False, save=True)
```

Result:
![img1](/img/graph.png)

## average_graph()

`average_graph(data, keyterms, pfnet=True, max=1, min=0.1, r=np.inf, n_core=None, detailed=True)`

### Description    
Generate an average graph based on several graphs.

### Arguments

`data`: A list object containing several NetworkX graphs.

`keyterms`: A list object containing some string variables, each string is a key-term used in a graph.

`pfnet`: A Boolean value specifying if the data should be converted into an undirected PFNet. The default value is True.

`max`: A number used to convert the similarity matrix into the dissimilarity matrix if necessary when calculating a PFNet. For example, if each value of the original matrix ranges from 0 to 1, you can set max=1 and min=0.1. If values of both "max" and "min" are None, the original matrix will be used. The default value is 1.

`min`: A number used when calculating a PFNet. Please see "max". The default value is 0.1.

`r`: A number used when calculating a PFNet. Considering that the mental perception of concept relation is in the ordinal scale, the default value of `r` is infinity (i.e., np.inf). Please see "Schvaneveldt, R. W., Durso, F. T., & Dearhold, D. W. (1989). Network structures in proximity data. Psychology of Learning and Motivation, 24, 249-284".

`n_core`: An integer specifying the number of nodes with the highest node centrality keep in the average graph. The default value is None, representing that all key-terms and links will be kept.

`detailed`: A boolean, the default value is True. If detailed=True, there will be a printed message shown an average graph is generated successfully.

### Value
A NetworkX graph of the average network.

### Examples
```
import cookiemilk

# example data
cmap_student1 = [['A', 'B'], ['B', 'C'], ['C', 'D']]
cmap_student2 = [['F', 'B'], ['F', 'C'], ['F', 'E']]
cmap_student3 = [['A', 'G'], ['G', 'C'], ['G', 'D']]

# convert to graph
student1 = cookiemilk.cmap2graph(cmap_student1, data_type='pair', read_from_file=False)
student2 = cookiemilk.cmap2graph(cmap_student2, data_type='pair', read_from_file=False)
student3 = cookiemilk.cmap2graph(cmap_student3, data_type='pair', read_from_file=False)

# arrange data
data = list([student1, student2, student3])

# keyterm
keyterms = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# approach 1: an average network containing all key-terms (setting n_core=False)
average1 = cookiemilk.average_graph(data=data, keyterms=keyterms, n_core=False, pfnet=True)

# approach 2: an average network containing only four core key-terms (setting n_core=4)
average2 = cookiemilk.average_graph(data=data, keyterms=keyterms, n_core=4, pfnet=True)
```
