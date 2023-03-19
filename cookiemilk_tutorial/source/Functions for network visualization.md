# Functions for network visualization

## draw()

`draw(graph, show=True, save=False, filename='filename', encoding='utf-8', canvas_size=(500, 500), node_font='sans-serif', node_fontsize=12, node_fontcolor='crimson', node_fillcolor='#ffebcd', node_size=12, edge_color='#7ab8cc', edge_size=2, edge_distance=100, charge=-300, detailed=False)`
    
### Description    
Show and/or save a df_graphs.

Based on d3.js (https://d3js.org/) and pywebview (https://github.com/r0x0r/pywebview).

### Arguments

`graph`: a NetworkX df_graphs.

`show`: show df_graphs immediately if show=True, or do not show until a draw_html(...show=True) is running. The df_graphs is drawing using d3.js (version 3, i.e., d3v3) and is interactive. You can also modify the style of df_graphs by adding other parameters.

`save`: save the output as an HTML file. The df_graphs being saved is an SVG object in the HTML file. Scalable vector graphic (SVG) is a type of image format that can be opened by browser software such as Chrome, Edge and Firefox, and can be edited by using Adobe Illustrator. Currently, `cookiemilk` can not save a graph as an SVG file directly, but you can extract it from the HTML file.

`filename`: filename of the output HTML file. The default is "filename".

`encoding`: encoding of the output HTML file. The default is "utf-8".

`canvas_size`: a list or tuple specifying the size of the canvas. The default is (500, 500), which means 500*500 pixels.

`node_font`: a string specifying the font of nodes in the graph. The default is "sans-serif".

`node_fontsize`: a number specifying the size of labels in df_nodes. The default is 12.

`node_fontcolor`: a string specifying the colour of labels in nodes. The string can be written in HEX format or just a colour name (as long as d3.js know it). The default is "crimson".

`node_fillcolor`: a string specifying the colour of nodes. The default is "#ffebcd".

`node_size`: a number specifying the size of nodes in the graphs. The default is 12.

`edge_color`: a string specifying the colour of edges. The default is "#7ab8cc".

`edge_size`: a number specifying the width of edges in the graphs. The default is 2.

`edge_distance`: a number specifying the distance among nodes. The default is 100.

`charge`: a number specifying the charge in the df_graphs. The default is -300.

`detailed`: show HTML contents or not. The default is False.

### Value
A list object of edges.

### Examples
```
import cookiemilk

# import data
my_cmap = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data = cookiemilk.cmap2graph(file=my_cmap, data_type='pair', read_from_file=False)

# visualization
cookiemilk.draw(my_data)
```

Result:
![img1](/img/graph.png)

## average_graph()

`average_graph(data, keyterms, pfnet=True, max=1, min=0.1, r=np.inf, n_core=None)`

### Description    
Generate an average graph.

### Arguments

`data`: a list object containing multiple Networkx graph objects.

`keyterms`: A list object containing some string variables, each string is one key-term.

`pfnet`: Whether the data should be converted into an undirected PFNet. The default value is False.

`max`: A parameter used to convert the similarity matrix into the dissimilarity matrix if necessary. for example, if each value of the original matrix ranges from 0 to 1, then "max" will be 1 and "min" will be 0.1. If values of both "max" and "min" are None (which is the default value), then the original matrix will be used.

`min`: See "max".

`r`: A parameter of the pathfinder algorithm. Considering that the mental perception of concept relation is the ordinal scale, we set "r" as infinity, see "Schvaneveldt, R. W., Durso, F. T., & Dearhold, D. W. (1989). Network structures in proximity data. Psychology of Learning and Motivation, 24, 249-284".

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

