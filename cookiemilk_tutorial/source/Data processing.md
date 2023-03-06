# Data processing

## pathfinder_network()

`pathfinder_network(G, max, min, r=np.inf)`
    
### Description    
Calculate the PFNet of a given graph. Note: This function is called by cmap2graph() and text2graph().


## Calc_surface_matching()

`calc_surface_matching(graph1, graph2)`
    
### Description    
Calculate surface matching index between df_graphs.

Please see:
Kopainsky, B., Pirnay-Dummer, P., & Alessi, S. M. (2012). Automated assessment of learners' understanding in complex dynamic systems: Automated Assessment of Understanding. System Dynamics Review, 28(2), 131-156.

### Arguments
`graph1`: a NetworkX df_graphs.

`graph2`: another Networkx df_graphs.

### Value
A number of surface matching.

### Examples

```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(file=my_cmap1, data_type='pair', read_from_file=False)

# import another graph
my_cmap2 = [['A', 'D'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data2 = cookiemilk.cmap2graph(file=my_cmap2, data_type='pair', read_from_file=False)

# calculation
my_result = cookiemilk.calc_surface_matching(my_data1, my_data2)
print(my_result)
```

The result is 0.75.

## calc_graphical_matching()

`calc_graphical_matching(graph1, graph2)`

### Description    
Calculate graphical matching index between df_graphs.

Please see:
Kopainsky, B., Pirnay-Dummer, P., & Alessi, S. M. (2012). Automated assessment of learners' understanding in complex dynamic systems: Automated Assessment of Understanding. System Dynamics Review, 28(2), 131-156.

### Arguments
``graph1``: a NetworkX df_graphs.

``graph2``: another Networkx df_graphs.

### Value
A number of graphical matching.

### Examples
```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(file=my_cmap1, data_type='pair', read_from_file=False)

# import another graph
my_cmap2 = [['A', 'D'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data2 = cookiemilk.cmap2graph(file=my_cmap2, data_type='pair', read_from_file=False)

# calculation
my_result = cookiemilk.calc_graphical_matching(my_data1, my_data2)
print(my_result)
```

The result is 0.67.

## calc_gcent()
`calc_gcent(G, detailed=False)`

### Description  
Calculate the Graph Centrality (gcent) of a df_graphs.

Please see:
Clariana, R. B., Rysavy, M. D., & Taricani, E. (2015). Text signals influence team artifacts. Educational Technology Research and Development, 63(1), 35-52.

### Arguments
``G``: a NeyworkX df_graphs.

``detailed``: show detailed information of calculation or not. Default is False.

### Value
A number of gcent. And if you set `detailed=True`, additional information will be shown in the console.

### Examples
```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(file=my_cmap1, data_type='pair', read_from_file=False)

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

## numerical_sim()
`numerical_sim(value1, value2)`
    
### Description    
Calculate numerical similarity, see "calc_tversky".

### Arguments
``value1``: a value.

``value2``: another value.

### Value
A number of similarity.

### Examples
```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(file=my_cmap1, data_type='pair', read_from_file=False)

# import another graph
my_cmap2 = [['A', 'D'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data2 = cookiemilk.cmap2graph(file=my_cmap2, data_type='pair', read_from_file=False)

# calculate gcent
my_result1 = cookiemilk.calc_gcent(my_data1)
my_result2 = cookiemilk.calc_gcent(my_data2)

# calculate gcent similarity
print(cookiemilk.numerical_sim(my_result1, my_result2))
```

The result is 0.50.

## calc_tversky()
`calc_tversky(graph1, graph2, comparison, alpha=0.5, detailed=False)`

### Description  
Calculate Tversky's similarity between df_graphs.

There are three types of similarities, please see:
Kopainsky, B., Pirnay-Dummer, P., & Alessi, S. M. (2012). Automated assessment of learners' understanding in complex dynamic systems: Automated Assessment of Understanding. System Dynamics Review, 28(2), 131-156.
    
Pirnay-Dummer P., Ifenthaler D. (2010) Automated Knowledge Visualization and Assessment. In: Ifenthaler D., Pirnay-Dummer P., Seel N. (eds) Computer-Based Diagnostics and Systematic Analysis of Knowledge. Springer, Boston, MA.

Noted that the "Network overlap" described in Clariana's researches equals to the propositional similarity (when alpha=beta=0.5), please see:
Clariana, R. B., Wallace, P. E., & Godshalk, V. M. (2009). Deriving and measuring group knowledge structure from essays: The effects of anaphoric reference. Educational Technology Research and Development, 57(6), 725-737.

### Arguments
`graph1`: a NetworkX df_graphs.

`graph2`: another Networkx df_graphs.

`comparison`: a string from ['concept', 'propositional', 'semantic'] specifying which types of similarities to calculate.

`alpha`: the parameter "alpha" in the Tversky's similarity.

`detailed`: show detailed information of calculation or not. Default is False.

### Value
A number of Tversky's similarity.

### Examples
```
import cookiemilk

# import a graph
my_cmap1 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data1 = cookiemilk.cmap2graph(file=my_cmap1, data_type='pair', read_from_file=False)

# import another graph
my_cmap2 = [['A', 'D'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
my_data2 = cookiemilk.cmap2graph(file=my_cmap2, data_type='pair', read_from_file=False)

# calculate conceptual similarity
print(cookiemilk.calc_tversky(my_data1, my_data2, comparison='concept'))

# calculate propositional similarity
print(cookiemilk.calc_tversky(my_data1, my_data2, comparison='propositional'))

# calculate semantic similarity
print(cookiemilk.calc_tversky(my_data1, my_data2, comparison='semantic'))
```

The similarity is 1.0, 0.57 and 0.57, respectively.
