# Introduction

## What is cookiemilk

`cookiemilk` is an easy-to-used Python package to process knowledge structure data automatically and quickly, including (a) convert a variety of forms of data (e.g., concept map, essay/summary) into a graph, (b) calculate graph-based features, and (c) similarity comparison.

The name of the package is inspired by my cats. Cookie is an American Shorthair cat, and Milk is a British Shorthair cat.

![img1](/img/cookiemilk_Small.png)

Say with me: Thank you Cookie and Milk for helping me process data!

## Installation

Windows:
```
py -m pip install --upgrade cookiemilk
```

Unix/macOS:
```
python3 -m pip install --upgrade cookiemilk
```

## Import
```
import cookiemilk
```

## Dependencies
`networkx`: A Python package for network analysis

`numpy`: A Python package for scientific computing

`pywebview`: A Python package for building GUI with JavaScript, HTML, and CSS

`d3.js`: A JavaScript library for manipulating documents based on data

## Functions

| Usage             | Functions     | Description |
|:-----------------|:--------------|:------------|
| Data arrangement | cmap2graph()             | import a concept map and convert it into a graph      |
|                  | text2graph()             | import a text and convert it into a graph       |
|                  | read_file()              | a basic function to read file  |
|                  | get_data_files_name      | read multiple files under a given folder |
|                  |    graph2prxfile()       | save a graph as a .prx file |
|  Data processing   |  pathfinder_network()    | calculate the PFNet of a given graph  |
|                  |calc_surface_matching()   | calculate the surface similarity between two graphs |
|                  |calc_graphical_matching() | calculate the graphical similarity between two graphs  |
|                  | calc_gcent()             | calculate the graphical centrality (GC) of a given graph |
|                  |   numerical_sim()        | calculate the numerical similarity (e.g., GC similarity)  |
|                  |calc_tversky()            | calculate the Tversky similarity between two graphs        |
|Visualization     |draw()                    | draw a graph via D3.JS     |

## Citation
To cite the `cookiemilk` package in publications use:

Wei, Z. (2023). *cookiemilk: An easy-to-use Python package to process knowledge structure data automatically*. South China Normal University, Guangzhou, China. Python package version 0.0.3, [https://pypi.org/project/cookiemilk/](https://pypi.org/project/cookiemilk/).

Corresponding BibTeX entry:

@Manual{, \
    title = {cookiemilk: An easy-to-used Python package to process knowledge structure data automatically}, \
    author = {Wei, Ziqian}, \
    organization = {South China Normal University}, \
    address = {Guangzhou, China}, \
    year = {2023}, \
    note = {Python package version 0.0.3}, \
    url = {https://pypi.org/project/cookiemilk/}, \
}
