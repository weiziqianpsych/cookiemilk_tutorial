# Functions

## Functions for data conversion

### cmap2graph()

`cmap2graph(data, data_type, keyterms=None, read_from_file=True, encoding='utf-8', read_from=0, pfnet=False, max=None, min=None, r=np.inf)`
    
#### Description    
Convert a concept map (or a proximity/adjacency matrix) into a NetworkX graph using the analysis of lexical aggregates (ALA).

Please see:

Clariana, R. B., Wallace, P. E., & Godshalk, V. M. (2009). Deriving and measuring group knowledge structure from essays: The effects of anaphoric reference. *Educational Technology Research and Development*, *57*(6), 725-737.

#### Arguments
``data``: A list (see the data type below), or a file path of a .txt document. Theoretically, contents can be written in any language, as long as Python and your computer support it. If you try to open a file, then you might have to set a suitable encoding form, for example, if contents is written in Chinese, the .txt file better save as utf-8 encoding, and should be open as the same encoding too.

``data_type``: A string named "pair" or "array". For the data type "pair", "file" should be a list contained every propositions/edges/links/lines from a concept map, e.g., file = [['concept A', 'concept B'], ['concept A', 'concept C'], ...]. For the data type  "array", "file" should be a n*n proximity/adjacency matrix, n = number of key-terms, both row and column represent key-terms and value(i, j) represents the relationship of concept(i) and concept(j). Both rectangle and triangle matrix are acceptable. 

``key_terms``: A list contained some string variables, each string is one key-term. All key-terms should be written in lower case, but upper case is also acceptable, as long as value of the parameter "as_lower" have been set as False.

``read_from_file``: if True, then manipulate the "file" parameter as a string, if False, then manipulate the "file" parameter as a file path. 

``encoding``: default is "utf-8", which supports most languages, such as English, Chinese, Korean, Arabic, etc. 

``read_from``: From which row (line) to read when opening data from a file. Noted that the index of the first row (line) is 0.

``pfnet``: Whether the data should be converted into a undirected PFNet. The default vale is False.

``max``: A parameter used to convert the similarity matrix into the dissimilarity matrix if necessary. for example, if each value of the origin matrix ranges from 0 to 1, then "max" will be 1 and "min" will be 0.1. If values of both "max" and "min" are None (which is the default value), then the origin matrix will be used.

``min*``: See "max".

``r``: A parameter of pathfinder algorithm. Considering that the mental perception of concept relation is the ordinal scale, we set "r" as infinity, see "Schvaneveldt, R. W., Durso, F. T., & Dearhold, D. W. (1989). Network structures in proximity data. Psychology of Learning and Motivation, 24, 249-284".
    

#### Value

A NetworkX graph represented the Knowledge Structure.

#### Examples

```
import cookiemilk

# import data
my_cmap = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data = cookiemilk.cmap2graph(data=my_cmap, data_type='pair', read_from_file=False)

# visualization
cookiemilk.draw(my_data)
```

Result:
![img1](/img/graph.png)

### text2graph()

`text2graph(data, key_terms, synonym=None, read_from_file=True, name=None, encoding='utf-8', as_lower=True, pfnet=False, max=None, min=None, r=np.inf)`

#### Description 
Convert a text into a NetworkX graph using the analysis of lexical aggregates (ALA).

Please see:

Clariana, R. B., Wallace, P. E., & Godshalk, V. M. (2009). Deriving and measuring group knowledge structure from essays: The effects of anaphoric reference. *Educational Technology Research and Development*, *57*(6), 725-737.

#### Arguments
``data``: a string or a file path of a .txt document. Theoretically, contents can be written in any language, as long as Python and your computer support it. If you try to open a file, then you might have to set a suitable encoding form, for example, if contents is written in Chinese, the .txt file better save as utf-8 encoding, and should be open as the same encoding too.

``key_terms``: a list contained some string variables, each string is one key-term. All key-terms should be written in lower case, but upper case is also acceptable, as long as value of the parameter "as_lower" have been set as False.

``synonym``: a dictionary object. Each key is a term form `keyterms`, and value can be a list containing synonym(s), e.g., synonym={'a':['a1', 'a2'], 'b':['b1', 'b2']}.

``read_from_file``: if True, then manipulate the "text" parameter as a string, if False, then manipulate the "text" parameter as a file path.

``encoding``: default is "utf-8", which supports most languages, such as English, Chinese, Korean, Arabic, etc.

``name``: name of Graph.

``as_lower``: whether to convert every character in the text to lower case. The default value is 'False'.

``pfnet``: converts the output into a undirected PFNet if set as True.

``max``: a parameter used to convert the similarity matrix into the dissimilarity matrix if necessary. for example, if each value of the origin matrix ranges from 0 to 1, then "max" will be 1 and "min" will be 0.1. If values of both "max" and "min" are None (which is the default value), then the origin matrix will be used.

``min``: see "max".

``r``: a parameter of pathfinder algorithm. Considering that the mental perception of concept relation is the ordinal scale, we set "r" as infinity, see "Schvaneveldt, R. W., Durso, F. T., & Dearhold, D. W. (1989). Network structures in proximity data. Psychology of Learning and Motivation, 24, 249-284".

#### Value

A NetworkX graph represented the Knowledge Structure.

#### Examples

```
import cookiemilk

# import data
my_text = 'A is an alternate name for B, and it relates to C. While C relates to A, it also is an important reason for D.'
my_keyterms = ['A', 'B', 'C', 'D']
my_data = cookiemilk.text2graph(data=my_text, key_terms=my_keyterms, read_from_file=False, as_lower=False)

# visualization
cookiemilk.draw(my_data)
```

Result:
![img1](/img/graph.png)

## Functions for data processing

### pathfinder_network()

`pathfinder_network(G, max, min, r=np.inf)`
    
#### Description    
Calculate the PFNet of a given graph. Note: This function is called by cmap2graph() and text2graph().

### calc_surface_matching()

`calc_surface_matching(graph1, graph2)`
    
#### Description    
Calculate surface matching index between df_graphs.

Please see:
Kopainsky, B., Pirnay-Dummer, P., & Alessi, S. M. (2012). Automated assessment of learners' understanding in complex dynamic systems: Automated Assessment of Understanding. System Dynamics Review, 28(2), 131-156.

#### Arguments
`graph1`: a NetworkX df_graphs.

`graph2`: another Networkx df_graphs.

#### Value
A number of surface matching.

#### Examples

```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(data=my_cmap1, data_type='pair', read_from_file=False)

# import another graph
my_cmap2 = [['A', 'D'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data2 = cookiemilk.cmap2graph(data=my_cmap2, data_type='pair', read_from_file=False)

# calculation
my_result = cookiemilk.calc_surface_matching(my_data1, my_data2)
print(my_result)
```

The result is 0.75.

### calc_graphical_matching()

`calc_graphical_matching(graph1, graph2)`

#### Description    
Calculate graphical matching index between df_graphs.

Please see:
Kopainsky, B., Pirnay-Dummer, P., & Alessi, S. M. (2012). Automated assessment of learners' understanding in complex dynamic systems: Automated Assessment of Understanding. System Dynamics Review, 28(2), 131-156.

#### Arguments
``graph1``: a NetworkX df_graphs.

``graph2``: another Networkx df_graphs.

#### Value
A number of graphical matching.

#### Examples
```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(data=my_cmap1, data_type='pair', read_from_file=False)

# import another graph
my_cmap2 = [['A', 'D'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data2 = cookiemilk.cmap2graph(data=my_cmap2, data_type='pair', read_from_file=False)

# calculation
my_result = cookiemilk.calc_graphical_matching(my_data1, my_data2)
print(my_result)
```

The result is 0.67.

### calc_gcent()
`calc_gcent(G, detailed=False)`

#### Description  
Calculate the Graph Centrality (GC) of a graph.

Please see:

Clariana, R. B., Rysavy, M. D., & Taricani, E. (2015). Text signals influence team artifacts. *Educational Technology Research and Development*, *63*(1), 35-52.

#### Arguments
``G``: a NeyworkX df_graphs.

``detailed``: show detailed information of calculation or not. Default is False.

#### Value
A number of gcent. And if you set `detailed=True`, additional information will be shown in the console.

#### Examples
```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(data=my_cmap1, data_type='pair', read_from_file=False)

# calculation
my_result = cookiemilk.calc_gcent(my_data1, detailed=True)
```

The result shows that the gcent of this graph is 0.67.
```
adjacency matrix:
 [[0. 1. 1. 1.]
 [1. 0. 1. 0.]
 [1. 1. 0. 0.]
 [1. 0. 0. 0.]]
n: 4
node_degree: [3. 2. 2. 1.]
ncent: [1.         0.66666667 0.66666667 0.33333333]
gcent: 0.6666666666666667
```

### numerical_sim()
`numerical_sim(value1, value2)`
    
#### Description    
Calculate numerical similarity, see "calc_tversky".

#### Arguments
``value1``: a value.

``value2``: another value.

#### Value
A number of similarity.

#### Examples
```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(data=my_cmap1, data_type='pair', read_from_file=False)

# import another graph
my_cmap2 = [['A', 'D'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data2 = cookiemilk.cmap2graph(data=my_cmap2, data_type='pair', read_from_file=False)

# calculate gcent
my_result1 = cookiemilk.calc_gcent(my_data1)
my_result2 = cookiemilk.calc_gcent(my_data2)

# calculate gcent similarity
print(cookiemilk.numerical_sim(my_result1, my_result2))
```

The result is 0.50.

### calc_tversky()
`calc_tversky(graph1, graph2, comparison, alpha=0.5, detailed=False)`

#### Description  
Calculate Tversky's similarity between two graphs, including conceptual, propositional and semantic similarity.

There are three types of similarities, please see:

Kopainsky, B., Pirnay-Dummer, P., & Alessi, S. M. (2012). Automated assessment of learners' understanding in complex dynamic systems: Automated Assessment of Understanding. *System Dynamics Review*, *28*(2), 131-156.

Pirnay-Dummer P., Ifenthaler D. (2010) Automated Knowledge Visualization and Assessment. In: Ifenthaler D., Pirnay-Dummer P., Seel N. (eds) *Computer-Based Diagnostics and Systematic Analysis of Knowledge*. Springer, Boston, MA.

NOTE: the **Network Overlap** described in Clariana's studies equals to the propositional similarity (when `alpha=beta=0.5`, which is the default value of the function `calc_tversky`), please see:

Clariana, R. B., Wallace, P. E., & Godshalk, V. M. (2009). Deriving and measuring group knowledge structure from essays: The effects of anaphoric reference. *Educational Technology Research and Development*, *57*(6), 725-737.

#### Arguments
`graph1`: a NetworkX df_graphs.

`graph2`: another Networkx df_graphs.

`comparison`: a string from ['concept', 'propositional', 'semantic'] specifying which types of similarities to calculate.

`alpha`: the parameter "alpha" in the Tversky's similarity.

`detailed`: show detailed information of calculation or not. Default is False.

#### Value
A number of Tversky's similarity.

#### Examples
```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(data=my_cmap1, data_type='pair', read_from_file=False)

# import another graph
my_cmap2 = [['A', 'D'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data2 = cookiemilk.cmap2graph(data=my_cmap2, data_type='pair', read_from_file=False)

# calculate conceptual similarity
print(cookiemilk.calc_tversky(my_data1, my_data2, comparison='concept'))

# calculate propositional similarity
print(cookiemilk.calc_tversky(my_data1, my_data2, comparison='propositional'))

# calculate semantic similarity
print(cookiemilk.calc_tversky(my_data1, my_data2, comparison='semantic'))
```

The similarity is 1.0, 0.57 and 0.57, respectively.

## Functions for network visualization

### draw()

`draw(graph, show=True, save=False, filename='filename', encoding='utf-8', canvas_size=(500, 500), node_font='sans-serif', node_fontsize=12, node_fontcolor='black', node_fillcolor='lightgrey', node_size=12, edge_color='#7ab8cc', edge_size=2, edge_distance=100, charge=-300, detailed=True)`

#### Description    
Show and/or save a NetworkX Graph.

Based on d3.js (https://d3js.org/) and pywebview (https://github.com/r0x0r/pywebview).

#### Arguments

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

#### Value
None.

#### Examples
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

### average_graph()

`average_graph(data, keyterms, pfnet=True, max=1, min=0.1, r=np.inf, n_core=None, detailed=True)`

#### Description    
Generate an average graph based on several graphs.

#### Arguments

`data`: A list object containing several NetworkX graphs.

`keyterms`: A list object containing some string variables, each string is a key-term used in a graph.

`pfnet`: A Boolean value specifying if the data should be converted into an undirected PFNet. The default value is True.

`max`: A number used to convert the similarity matrix into the dissimilarity matrix if necessary when calculating a PFNet. For example, if each value of the original matrix ranges from 0 to 1, you can set max=1 and min=0.1. If values of both "max" and "min" are None, the original matrix will be used. The default value is 1.

`min`: A number used when calculating a PFNet. Please see "max". The default value is 0.1.

`r`: A number used when calculating a PFNet. Considering that the mental perception of concept relation is in the ordinal scale, the default value of `r` is infinity (i.e., np.inf). Please see "Schvaneveldt, R. W., Durso, F. T., & Dearhold, D. W. (1989). Network structures in proximity data. Psychology of Learning and Motivation, 24, 249-284".

`n_core`: An integer specifying the number of nodes with the highest node centrality keep in the average graph. The default value is None, representing that all key-terms and links will be kept.

`detailed`: A boolean, the default value is True. If detailed=True, there will be a printed message shown an average graph is generated successfully.

#### Value
A NetworkX graph of the average network.

#### Examples
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

## Quick_analysis

```
quick_analysis(
        folder,
        data_type,
        key_terms=None,
        synonym=None,
        as_lower=None,
        pfnet=False,
        max=None,
        min=None,
        r=np.inf,
        encoding=None,
        read_from=None,

        referent_type=None,
        r_key_terms=None,
        r_synonym=None,
        r_as_lower=None,
        r_pfnet=False,
        r_max=None,
        r_min=None,
        r_r=np.inf,
        r_encoding=None,
        r_read_from=None,

        calculation=None,
        alpha=0.5,

        save_figures=True,
        
        save_average_figures=False,
        n_core=None,

        canvas_size=(500, 500),
        node_font='sans-serif',
        node_fontsize=12,
        node_fontcolour='black',
        node_fillcolour='lightgrey',
        node_size=12,
        edge_colour='lightgrey',
        edge_size=2,
        edge_distance=100,
        charge=-300,
        window_size=(600, 600)
)
```
