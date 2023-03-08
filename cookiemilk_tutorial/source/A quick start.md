# A quick start

## Step 1 Load data

First of all, import the package.
```
import cookiemilk
```

### Load a concept map from a file
For a concept map in the proposition format (i.e., the links/edge are unweighted, which means the values of the links/edges are 1 or 0), we can load it by using the function `cmap2graph` when set the argument `data_type='pairs'`. To do this, the data should be arranged in a way like this:


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


Your can save such kind of contents in a .txt file, like this:
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
You can also load a matrix when set the argument `data_type='array'` (this matrix can be seen as a weighted concept map linking each node together). For example, here is a matrix data that we want to load. This data was exported from the software JRateDrag, which was used in previous studies for conducting the sorting task.

![img1](/img/prx.png)

Let's take a look at the information of the data and then adjust the settings. **This is important because inappropriate settings will make your results wrong**. 

First, this is distance data (which means the values in the matrix represent dissimilarities) rather than data containing 1 or 0 only, so we need to set the argument `pfnet=True` to use the pathfinder algorithm to convert it into a *PFNet* (i.e., an unweighted graph that only contains a few links/edges). When we conduct the pathfinder algorithm, the imported matrix should be a dissimilarities matrix, and this is what this data is, so we do not need to do the matrix transformation (i.e., we set the argument `max=None` and `mix=None`, which are the default settings. Another usage of the argument `max` and `min` in the software JPathfinder defines the range of the values in the matrix, but it's fine to ignore these two arguments because all values will be within the range in most of the situation). 

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
Is is possible, but I do not recommend it unless you want to debug or test something.

### Load a text from a file

If you have a file like this, you can load it via the function `text2graph`. Here we use a document derived from the PISA reading test, the title of this document is *Collecting Nectar*.

![img1](/img/bee_text.png)

To do so, you need to provide the key terms in the text by defining a list object in Python (see `keyterms` below). Here are the codes.

```
keyterms = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
            'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
            'bees', 'evaporation', 'dry', 'fruit trees']
            
my_data = cookiemilk.text2graph(text='my_text.txt', keyterms=my_keyterms, as_lower=True)
```

**NOTE: if the text is written in English, I strongly recommend you to provide terms in the lower case and set the argument `as_lower=True`.** When the argument `as_lower=True` (the default setting), it will convert all of the words in the text to lower case, so that all key terms can be identified correctly. But, if there are key terms in upper case (e.g., abbreviations like 'GPS') and all of the corresponding terms in the text are also written in upper case, you can consider to set the argument `as_lower=False`.

**NOTE: if there are synonyms in the text, try to use the argument `synonym` in the function `text2graph`.** You can find more details about it on the page of this function.

### Load a text via codes
We can also load this text from a string object in Python directly.
```
text = "Bees make honey to survive. It is their only essential food. If there are 60,000 bees in a hive about one  third of them will be involved in gathering nectar which is then made into honey by the house bees. A small number of bees work as foragers or searchers. They find a source of nectar, then return to the hive  to tell the other bees where it is.  Foragers let the other bees know where the source of the nectar is by performing a dance which gives  information about the direction and the distance the bees will need to fly. During this dance the bee  shakes her abdomen from side to side while running in circles in the shape of a figure 8. The dance  follows the pattern shown on the following diagram. The diagram shows a bee dancing inside the hive on the vertical face of the honeycomb. If the middle  part of the figure 8 points straight up it means that bees can find the food if they fly straight towards the  sun. If the middle part of the figure 8 points to the right, the food is to the right of the sun."
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
for more information, please see references below:
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

Well, the propositional simialrity between these two graphs is 0.65.

## Step 3 Visualization
We can use the function `draw` to show a graph, it will draw the graph using `D3.js` and display it by `pywebview`. Let's take a look at `bee_cmap`.
```
cookiemilk.draw(bee_cmap)
```

result:
![img1](/img/draw.png)
