# Part 3 Advanced tips

## 1 Process a large dataset

Editing...


## 2 Use latent semantic analysis to generate an expert model

Editing...

## 3 About Tversky similarity

Editing...

## 4 About graph centrality

In this part, I will show you how to calculate graph centrality by hand so that you can understand how the holistic structure of a graph is estimated. And then I will show you how to use the function `calc_gcent` to calculate graph centrality conveniently.

We will use an example network from Clariana and Koul's research (2004). Please see below. This network includes five nodes and five edges (i.e., links).

![img1](/img/example_pfnet.png)

### 4.1 Calculate graph centrality manually

The equations of graph centrality are shown below (Clariana, Rysavy, & Taricani, 2015).

Equation 1: CD(v) = deg(v) / (n – 1)

Equation 2: CD(G) = ∑vi=1 [max(CD(vi)) – CD(vi)] / (n – 2)	

First, we need to calculate the node degree of each node. In graph theory, the degree of a node is the number of edges (i.e., links) including the node. In this example, the node "dog" connects to three other nodes. Considering "dog" has three links (i.e., "dog-cat", "dog-pet", "dog-truck"), we can say deg("dog") = 3. Similar to this, other nodes' degrees can be calculated as follows.

deg("cat") = 3

deg("dog") = 3

deg("pet") = 2

deg("car") = 1

deg("truck") = 1

Second, we need to calculate node centrality for each node. Based on Equation 1, each node's centrality can be calculated as follows.

CD("cat") = deg("cat")/(n - 1) = 3/(5 - 1) = 0.75

CD("dog") = deg("dog")/(n - 1) = 3/(5 - 1) = 0.75

CD("pet") = deg("pet")/(n - 1) = 2/(5 - 1) = 0.50

CD("car") = deg("car")/(n - 1) = 1/(5 - 1) = 0.25

CD("truck") = deg("truck")/(n - 1) = 1/(5 - 1) = 0.25

Third, we then use Equation 2 to calculate the holistic centrality of the network (i.e., graph centrality) as follows. Note that the highest node centrality in this network is 0.75, so max(C~D~(v~i~)) = 0.75.

CD(G) = [(0.75 - 0.75) + (0.75 - 0.75) + (0.75 - 0.50) + (0.75 - 0.25) + (0.75 - 0.25)] / (5 - 2) = 0.4267

As result, C~D~(G) of this PFNet is 0.4267. I hope this example is useful for you to understand the calculation of graph centrality. 

### 4.2 Use `calc_gcent` to calculate graph centrality

Finally, let's try to use `calc_gcent` to calculate the graph centrality of this PFNet automatically.

```
import cookiemilk

# import the example PFNet
my_cmap1 = [['car', 'cat'], ['cat', 'pet'], ['cat', 'dog'], ['pet', 'dog'], ['dog', 'truck']]
my_data1 = cookiemilk.cmap2graph(file=my_cmap1, data_type='pair', read_from_file=False)

# calculation
my_result = cookiemilk.calc_gcent(my_data1, detailed=True)
```

And here is the result. We have set the argument `detailed=True`, which will enable us to check each step of the calculation. When analyzing data, you can set the argument `detailed=False` to avoid redundant outputs.

```
adjacency matrix:
 [[0. 1. 0. 0. 0.]
 [1. 0. 1. 1. 0.]
 [0. 1. 0. 1. 0.]
 [0. 1. 1. 0. 1.]
 [0. 0. 0. 1. 0.]]
n: 5
node_degree: [1. 3. 2. 3. 1.]
ncent: [0.25 0.75 0.5  0.75 0.25]
gcent: 0.41666666666666663
```

As the result is stored in the variable `my_result`, we can also print it to see the value of graph centrality.

```
print(my_result)
```

And the output is shown below.

```
0.41666666666666663
```

### 4.3 References
* Clariana, R. B., & Koul, R. (2004). A computer-based approach for translating text into concept map-like representations. In A. J. Canas, J. D. Novak, and F. M. Gonzales, Eds., *Concept maps: theory, methodology, technology*, vol. 2, in the Proceedings of the First International Conference on Concept Mapping, Pamplona, Spain, Sep 14-17, pp.131-134. 
* Clariana, R. B., Rysavy, M. D., & Taricani, E. (2015). Text signals influence team artifacts. *Educational Technology Research and Development*, *63*(1), 35-52.
