# Part 3 Advanced tips

## 3.1 Process a large dataset

Now you can use the function `quick_analysis` to process big data easily. This function can do the basic things, but if you want to conduct some advanced analyses (e.g., analyzing data from an experiment where students use different key-terms in their essays or concept maps), you will need to write the code by yourself (see Part 2 for details).

For example, we have four students' essays here. To use `quick_analysis`, We need to arrange these data in separate .txt files and put them in a folder called "data", while the expert essay (which will be used as the referent in some calculations) is saved as a file called "ref.txt" (NOTE: to use `quick_analysis`, you have to name the expert data as "ref.txt" exactly). Both the file "ref.txt" and the folder "data" should be included in a folder.

![img1](/img/quick_analysis1.png)

Then, you can use the following code to process the data.

```
import cookiemilk_project.cookiemilk as cookiemilk
import numpy as np


key_terms = ['longitudinal prediction',
             'literacy development',
             'cognitive skills',
             'language skills',
             'parental reports',
             'reading achievement']

my_data = cookiemilk.quick_analysis(

    # the file path of the data
    folder='/Users/weiziqian/Desktop/test/text',  # the folder containing ref.txt and students' data

    # about students' data
    data_type='text',  # data type, can be "proposition", "array" or "text"
    key_terms=key_terms,  # key-terms in ref.txt and students' data
    synonym=None,  # you can define synonyms here
    as_lower=True,  # whether convert all the words into lowercase
    pfnet=True,  # whether converting data into PFNets
    max=1.1,  # a parameter of the pathfinder algorithm
    min=0.1,  # a parameter of the pathfinder algorithm
    r=np.inf,  # a parameter of the pathfinder algorithm
    encoding='utf-8',  # the encoding format of data files
    read_from=0,  # which line should the content in data files be read from

    # about the expert data, the parameters are as same as the above
    referent_type='text',
    r_key_terms=key_terms,
    r_synonym=None,
    r_as_lower=True,
    r_pfnet=True,
    r_max=1.1,
    r_min=0.1,
    r_r=np.inf,
    r_encoding='utf-8',
    r_read_from=0,

    # which calculations do you want to conduct (all available features are listed below)
    calculation=[
        'density',
        'GC',
        's_density',
        's_GC',
        's_surface',
        's_concept',
        's_link',
        's_graphical',
        's_semantic'
    ],
    alpha=0.5,  # a parameter of Tversky's similarity

    # about the visualization
    save_figures=True,  # whether to save the visualized graphs
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
    window_size=(600, 600),

    # about the average graph
    save_average_figures=True,  # whether to generate the average graph
    n_core=None
)

```

After running the code, we can find a new folder called "networks", which containsing all visualized graphs and the average graph (if you chose to generate it), and a table file called "quick_analysis_20230710_145130.csv" (the numbers indicate the date and time). 

![img1](/img/quick_analysis2.png)

As shown below, the table file contains the results of the data.

![img1](/img/quick_analysis3.png)

## 3.2 Use latent semantic analysis to generate an expert model

Editing...

## 3.3 About Tversky similarity

Editing...

## 3.4 About graph centrality

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

Clariana, R. B., & Koul, R. (2004). A computer-based approach for translating text into concept map-like representations. In A. J. Canas, J. D. Novak, and F. M. Gonzales, Eds., *Concept maps: theory, methodology, technology*, vol. 2, in the Proceedings of the First International Conference on Concept Mapping, Pamplona, Spain, Sep 14-17, pp.131-134. 

Clariana, R. B., Rysavy, M. D., & Taricani, E. (2015). Text signals influence team artifacts. *Educational Technology Research and Development*, *63*(1), 35-52.
