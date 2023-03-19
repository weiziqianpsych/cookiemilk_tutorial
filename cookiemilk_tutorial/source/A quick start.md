# A quick start

## Step 1 Load data

First of all, import the package.
```
import cookiemilk
```

### Load a concept map from a file
For a concept map in the proposition format (i.e., the links/edge are unweighted, which means the values of the links/edges are 1 or 0), we can load it by using the function `cmap2graph` when setting the argument `data_type='pairs'`. To do this, the data should be arranged in a way like this:


beeswax &emsp; minerals \
bees &emsp; figure 8 \
nectar &emsp; bees \
water &emsp; beeswax \
figure 8 &emsp; sun \
fruit trees &emsp; nectar \
shake &emsp; distance \
minerals &emsp; nectar \
distance &emsp; abdomen \
evaporation &emsp; nectar \
hive &emsp; nectar \
hive &emsp; house bees \
figure 8 &emsp; shake \
water &emsp; evaporation \
dry &emsp; evaporation \
abdomen &emsp; figure 8 \
dry &emsp; house bees \
honey &emsp; house bees


You can save such kind of content in a .txt file, like this:
![img1](/img/cmap_file.png)

And we can use `cmap2graph` to load and convert it into a NetworkX graph.
```
bees_cmap = cookiemilk.cmap2graph(file='bees_student_cmap_en.txt', data_type='pairs')
```

### Load a concept map via codes

You can also load data by writing some codes. For example, the concept map data above can be loaded like this.

```
my_cmap = [['beeswax', 'minerals'],
           ['bees', 'figure 8'],
           ['nectar', 'bees'],
           ['water', 'beeswax'],
           ['figure 8', 'sun'],
           ['fruit trees', 'nectar'],
           ['shake', 'distance'],
           ['minerals', 'nectar'],
           ['distance', 'abdomen'],
           ['evaporation', 'nectar'],
           ['hive', 'nectar'],
           ['hive', 'house bees'],
           ['figure 8', 'shake'],
           ['water', 'evaporation'],
           ['dry', 'evaporation'],
           ['abdomen', 'figure 8'],
           ['dry', 'house bees'],
           ['honey', 'house bees']]

my_data = cookiemilk.cmap2graph(file=my_cmap, data_type='pairs', read_from_file=False)
```

### Load a matrix from a file
You can also load a matrix when setting the argument `data_type='array'` (this matrix can be seen as a weighted concept map linking each node together). For example, here is a matrix data that we want to load. This data was exported from the software JRateDrag, which was used in previous studies for conducting the sorting task.

![img1](/img/prx.png)

Let's take a look at the information of the data and then adjust the settings. **This is important because inappropriate settings will make your results wrong**. 

First, this is distance data (which means the values in the matrix represent dissimilarities) rather than data containing 1 or 0 only, so we need to set the argument `pfnet=True` to use the pathfinder algorithm to convert it into a *PFNet* (i.e., an unweighted graph that only contains a few links/edges). When we conduct the pathfinder algorithm, the imported matrix should be a dissimilarities matrix, and this is what this data is, so we do not need to do the matrix transformation (i.e., we set the argument `max=None` and `mix=None`, which are the default settings. Another usage of the argument `max` and `min` in the software JPathfinder defines the range of the values in the matrix, but it's fine to ignore these two arguments because all values will be within the range in most of the situations). 

Second, we only need to load the matrix, so the information at the beginning of the file is unnecessary. Thus, we need to set the argument `read_from=7` to read the file from the 7th line, which is the start of the matrix. 

Third, do not forget to define a list with terms in an appropriate order (i.e., the variable `keyterms` below).

By the way, your data may be a full matrix or a triangle matrix (the example here is a triangle matrix), but you do not need to worry about that, because the function `cmap2graph` will do the matrix transformation automatically when it is necessary.

Now, here are the codes.

```
keyterms = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
            'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
            'bees', 'evaporation', 'dry', 'fruit trees']
            
triangle = cookiemilk.cmap2graph(file='/Users/weiziqian/jpf/triangle.prx', data_type='array', keyterms=terms,
                                 read_from=7, pfnet=True)
                                 
cookiemilk.draw(triangle)
```

And this is what we got.

![img1](/img/triangle_graph.png)

We can also take a look at what the PFNet looks like if we do the same thing via JPathfinder software. You can find that the graph is consistent.

![img1](/img/triangle_pfnet.png)

### Load a matrix via codes
It is possible, but I do not recommend it unless you want to debug or test something.

### Load a text from a file

If you have a file like this, you can load it via the function `text2graph`. Here we use a document derived from the PISA reading test, the title of this document is *Collecting Nectar*.

![img1](/img/bee_text.png)

To do so, you need to provide the key terms in the text by defining a list object in Python (see `keyterms` below). Here are the codes.

```
keyterms = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
            'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
            'bees', 'evaporation', 'dry', 'fruit trees']
            
my_data = cookiemilk.text2graph(text='bee_text.txt', keyterms=my_keyterms, as_lower=True)
```

**NOTE: if the text is written in English, I strongly recommend you to provide terms in lower case and set the argument `as_lower=True`.** When the argument `as_lower=True` (the default setting), it will convert all of the words in the text to lowercase, so that all key terms can be identified correctly. But, if there are key terms in upper case (e.g., abbreviations like 'GPS') and all of the corresponding terms in the text are also written in upper case, you can consider setting the argument `as_lower=False`.

**NOTE: if there are synonyms in the text, try to use the argument `synonym` in the function `text2graph`.** You can find more details about it on the page of this function.

### Load a text via codes
We can also load this text from a string object in Python directly.
```
text = "Bees make honey to survive. It is their only essential food. If there are 60,000 bees in a hive about one third of them will be involved in gathering nectar which is then made into honey by the house bees. A small number of bees work as foragers or searchers. They find a source of nectar, then return to the hive to tell the other bees where it is.  Foragers let the other bees know where the source of the nectar is by performing a dance which gives information about the direction and the distance the bees will need to fly. During this dance the bee shakes her abdomen from side to side while running in circles in the shape of a figure 8. The dance follows the pattern shown on the following diagram. The diagram shows a bee dancing inside the hive on the vertical face of the honeycomb. If the middle part of the figure 8 points straight up it means that bees can find the food if they fly straight towards the sun. If the middle part of the figure 8 points to the right, the food is to the right of the sun."
```

We can replace the synonyms via the codes below. This is an alternative way to process synonyms if you do not want to use the argument `synonym` in the function `text2graph`.
```
text = text.replace('honeycomb', 'hive')  # replace synonym: honeycomb --> hive
```

And we also need to list which key terms were used in the text.
```
keyterms = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
            'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
            'bees', 'evaporation', 'dry', 'fruit trees']
```

Now we can convert the text into a NetworkX graph by using `text2graph`.
```
bee_text = cookiemilk.text2graph(text, keyterms, read_from_file=False)
```

Here is another example, we do the same thing for a student's summary of the text.
```
text_student = 'Bees make honey to survive. It is their only essential food. If there are 60,000 bees in a hive about one third of them will be involved in gathering nectar which is then made into honey by the house bees. A small number of bees work as foragers or searchers. They find a source of nectar, then return to the hive to tell the other bees where it is. Foragers let the other bees know where the source of the nectar is by performing a dance which gives information about the direction and the distance the bees will need to fly. During this dance the bee shakes her abdomen from side to side while running in circles in the shape of a figure 8. . If the middle part of the figure 8 points straight up it means that bees can find the food if they fly straight towards the sun. If the middle part of the figure 8 points to the right, the food is to the right of the sun. The distance of the food from the hive is indicated by the length of time that the bee shakes her abdomen. If the food is quite near the bee shakes her abdomen for a short time. If it is a long way away she shakes her abdomen for a long time. When the bees arrive at the hive carrying nectar they give this to the house bees. The house bees move the nectar around with their mandibles, exposing it to the warm dry air of the hive. When it is first gathered the nectar contains sugar and minerals mixed with about 80% water. After ten to twenty minutes, when much of the excess water has evaporated, the house bees put the nectar in a cell in the honeycomb where evaporation continues. After three days, the honey in the cells contains about 20% water. At this stage, the bees cover the cells with lids which they make out of beeswax. At any one time the bees in a hive usually gather nectar from the same type of blossom and from the same area. Some of the main sources of nectar are fruit trees, clover and flowering trees. '

text = text.replace('honeycomb', 'hive')  # replace synonym: honeycomb --> hive

keyterms = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
            'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
            'bees', 'evaporation', 'dry', 'fruit trees']

bee_student = cookiemilk.text2graph(text_student, keyterms, read_from_file=False)
```

## Step 2 Do some calculations
For example, we can calculate the propositional similarity between `bee_text` and `bee_student` by using the function `calc_tversky`.
```
cookiemilk.calc_tversky(bee_text, bee_student, comparison='propositional', detailed=True)
```

And here is what we got.
```
Calculating Tversky's similarity in ratio scales
s = (set1 - set2)/[(set1 - set2) + alpha*(set1 - set2) + beta*(set2 - set1)]
alpha=0.5, beta=0.5
for more information, please see the references below:
Tversky, A. (1977). Features of similarity. Psychological Review, 84(4), 327–
352. https://doi.org/10.1037/0033-295X.84.4.327
 Pirnay-Dummer P., Ifenthaler D. (2010) Automated Knowledge Visualization and 
Assessment. In: Ifenthaler D., Pirnay-Dummer P., Seel N. (eds) Computer-Based 
Diagnostics and Systematic Analysis of Knowledge. Springer, Boston, MA. 
https://doi.org/10.1007/978-1-4419-5662-0_6
set1 & set2: [['honey', 'bees'], ['shake', 'abdomen'], ['hive', 'bees'], ['house bees', 'honey'], ['sun', 'bees'], ['figure 8', 'bees'], ['abdomen', 'figure 8'], ['nectar', 'distance'], ['nectar', 'honey'], ['nectar', 'hive'], ['sun', 'figure 8'], ['house bees', 'bees'], ['distance', 'bees'], ['nectar', 'bees'], ['shake', 'bees']]
value of set1 & set2: 15
set1 - set2: [['hive', 'figure 8']]
value of set1 - set2: 1
set2 - set1: [['beeswax', 'bees'], ['nectar', 'minerals'], ['water', 'bees'], ['nectar', 'fruit trees'], ['hive', 'shake'], ['distance', 'hive'], ['water', 'minerals'], ['water', 'honey'], ['nectar', 'house bees'], ['house bees', 'water'], ['sun', 'distance'], ['abdomen', 'bees'], ['honey', 'evaporation'], ['nectar', 'dry'], ['hive', 'dry']]
value of set2 - set1: 15
similarity = 15/(15 + 0.5*1 + 0.5*15)=0.6521739130434783
```

Well, the propositional similarity between these two graphs is 0.65.

## Step 3 Visualization
We can use the function `draw` to show a graph, it will draw the graph using `D3.js` and display it by `pywebview`. Let's take a look at `bee_cmap`.
```
cookiemilk.draw(bee_cmap)
```

Result:
![img1](/img/draw.png)

## Step 4 Average graph
If we are conducting a behavioural experiment, one of the possible analyses that we may want to do is to check how networks differ between groups. Such a descriptive analysis can be done by generating average networks at the group level vis the function `average_graph`.

Here is an example, I will show you how can we generate an average network based on data from three students. As shown below, different students used different key-terms in their concept maps. Student1 used the terms "A", "B", "C", and "D"; Student2 used the terms "B", "C", "E",  and "F"; Student3 used the term "A", "C", "D", and "G".

```
# example data
cmap_student1 = [['A', 'B'], ['B', 'C'], ['C', 'D']]
cmap_student2 = [['F', 'B'], ['F', 'C'], ['F', 'E']]
cmap_student3 = [['A', 'G'], ['G', 'C'], ['G', 'D']]

student1 = cookiemilk.cmap2graph(cmap_student1, data_type='pair', read_from_file=False)
student2 = cookiemilk.cmap2graph(cmap_student2, data_type='pair', read_from_file=False)
student3 = cookiemilk.cmap2graph(cmap_student3, data_type='pair', read_from_file=False)
```

To use the function `average_graph`, we need to include networks from three students in a list object. And we also need to provide all of the key-terms.

```
# arrange data
data = list([student1, student2, student3])

keyterms = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
```

In general, `average_graph` works as the following steps. First, each network will be represented as an n×n matrix (n = the number of key-terms). Each value in the matrix will be 1 or 0, with 1 = 'connected link' and 0 = 'unconnected'. Second, a mean matrix based on all matrices will be defined and converted to a NetworkX graph. Third, the average network will be converted to a PFNet if the argument `PFNet`=TRUE. Finally, if the argument `n_core` is an integer, for example, 4, an average network containing only the four most important key-terms and related links will be returned. If the argument `n_core` is None (i.e., the default value), an average network containing all key-terms and links will be returned.

Now, I will show you three approaches to generating average networks. NOTE: I only recommend the first and the second approach, and the third approach is just shown for explanations. The first approach (i.e., `average1`) generates an average PFNet containing all key-terms. The second approach (i.e., `average2`) generates an average PFNet **BUT** only containing the four most important key-terms and related links. The third approach (i.e., `average3`) generates an average non-PFNet graph with weighted edges.

```
# average
average1 = cookiemilk.average_graph(data=data, keyterms=keyterms, n_core=False, pfnet=True)
average2 = cookiemilk.average_graph(data=data, keyterms=keyterms, n_core=4, pfnet=True)
average3 = cookiemilk.average_graph(data=data, keyterms=keyterms, n_core=False, pfnet=False)

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(15, 5), dpi=100)

plt.subplot(231)
plt.title('Student1')
p1 = nx.draw(student1, with_labels=True)

plt.subplot(232)
plt.title('Student2')
nx.draw(student2, with_labels=True)

plt.subplot(233)
plt.title('Student3')
nx.draw(student3, with_labels=True)

plt.subplot(234)
plt.title('average PFNet')
nx.draw(average1, with_labels=True)

plt.subplot(235)
plt.title('average PFNet containing four most important terms')
nx.draw(average2, with_labels=True)

plt.subplot(236)
plt.title('weighted average graph')
pos = nx.spring_layout(average3, k=10)  # For better example looking
nx.draw(average3, pos, with_labels=True)
labels = {e: round(average3.edges[e]['weight'], 2) for e in average3.edges}
nx.draw_networkx_edge_labels(average3, pos, edge_labels=labels)

plt.show()
```

Result:
![img1](/img/example_average.png)

As shown in three students' networks (see the top in the above figure), the key-term "B" and "C" were the two most important key-terms in Student1's network, the key-term "F" was the most important in Student2's network, and the key-term "G" was the most important in Student3's network. 

The first average network contained all key-terms that appear in students' networks (i.e., from "A" to "G", see the bottom-left of the above figure). However, this approach might result in a large network if the dataset is large and different students used different key-terms. One of the possible solutions is to retain only the most important nodes and related links in the average network. For doing this, we needed to check the node centrality first.

```
nx.degree_centrality(average1)
```

Here were the results. 

```
{'B': 0.5, 'A': 0.3333333333333333, 'C': 0.6666666666666666, 'D': 0.3333333333333333, 'F': 0.5, 'E': 0.16666666666666666, 'G': 0.5}
```

We found that "B", "C", "F", and "G" show the highest node centrality, so we could consider retaining only four nodes in the average network. Four was also the number of key-terms in each student's network, so this number seems appropriate in this case. By setting the argument `n_core`=4, we obtained the second average network (see the bottom-middle of the above figure). Note that keeping the size of the average network is important in some cases because some indices such as graph centrality (GC) only can be used to compare networks when the networks are about the same size.

The third average network contained most of the information in the mean matrix (see the bottom-middle of the above figure), but it was less interpretable. This is why the argument `pfnet` and `n_core` are important for generating an average network.
