# Part 1 Introduction

## 1.1 What is cookiemilk

The Python package *cookiemilk* is an easy-to-use tool to process knowledge structure data automatically and quickly, including (a) data conversion (e.g., converting concept maps or essays to graphs), (b) graph-based features calculation, and (c) graph visualization. The *cookiemilk* package is mainly based on the Linear Aggregate Approach (Clariana et al., 2009), but also enables calculations of some features introduced by Pirnay-Dummer and Ifenthaler (2011). The name of the package is inspired by my cats. Cookie is an American Shorthair cat, and Milk is a British Shorthair cat.

![img1](/img/logo.svg)

**References**

Clariana, R. B., Wallace, P. E., & Godshalk, V. M. (2009). Deriving and measuring group knowledge structure from essays: The effects of anaphoric reference. *Educational Technology Research and Development*, *57*, 725-737.

Pirnay-Dummer, P., & Ifenthaler, D. (2011). Reading guided by automated graphical representations: How model-based text visualizations facilitate learning in reading comprehension tasks. *Instructional Science*, *39*(6), 901-919.

## 1.2 Installation

Windows:
```
py -m pip install --upgrade cookiemilk
```

Unix/macOS:
```
python3 -m pip install --upgrade cookiemilk
```

## 1.3 Import
```
import cookiemilk
```

## 1.4 Main functions

|Usage             | Functions     | Description |
|:-----------------|:--------------|:------------|
|Data arrangement  |cmap2graph              | import a concept map and convert it into a graph          |
|                  |text2graph              | import a text and convert it into a graph                 |
|                  |graph2prxfile           | save a graph in a proximity matrix as a plaintext file    |
|Data processing   |pathfinder_network      | calculate the PFNet of a given graph                      |
|                  |calc_surface_matching   | calculate the surface similarity between two graphs       |
|                  |calc_graphical_matching | calculate the graphical similarity between two graphs     |
|                  |calc_gcent              | calculate the graphical centrality (GC) of a given graph  |
|                  |numerical_sim           | calculate the numerical similarity                        |
|                  |calc_tversky            | calculate the Tversky similarity between two graphs       |
|Visualization     |draw                    | draw and/or save a graph                                  |
|                  |average_graph           | generate an average graph                                 |
|Others            |quick_analysis          | conduct data analysis using the above functions           |

## 1.5 Dependencies
`networkx`: A Python package for network analysis

`numpy`: A Python package for scientific computing

`pywebview`: A Python package for building GUI with JavaScript, HTML, and CSS

`d3.js`: A JavaScript library for manipulating documents based on data

## 1.6 Citation
To cite the `cookiemilk` package in publications use:

Wei, Z. (2023). *cookiemilk: An easy-to-use Python package to process knowledge structure data automatically*. South China Normal University, Guangzhou, China. Python package, [https://pypi.org/project/cookiemilk/](https://pypi.org/project/cookiemilk/).

BibTeX:
```
@Manual{,
    title = {cookiemilk: An easy-to-use Python package to process knowledge structure data automatically},
    author = {Wei, Ziqian},
    organization = {South China Normal University},
    address = {Guangzhou, China},
    year = {2023},
    note = {Python package},
    url = {https://pypi.org/project/cookiemilk/},
}
```
