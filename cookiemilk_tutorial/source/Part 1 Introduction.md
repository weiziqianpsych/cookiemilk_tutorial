# Part 1 Introduction

## 1.1 What is cookiemilk

The Python package *cookiemilk* is an easy-to-use tool to process knowledge structure data automatically and quickly. It includes (a) data conversion, such as converting concept maps or essays to graphs, (b) graph-based features calculation, and (c) graph visualization. The *cookiemilk* package is primarily based on the Linear Aggregate Approach (Clariana et al., 2009) but also allows for the calculation of some features introduced by Pirnay-Dummer and Ifenthaler (2011). 

The code was initially written for a specific analysis purpose when I was working on my Master's thesis. Although I reorganized the code to make it flexible for use in different analysis plans, the package has not been fully validated, and some errors may occur. Please feel free to contact me via [weiziqianpsych@outlook.com](weiziqianpsych@outlook.com) to report any issues and help me improving the package and this tutorial website!

The name of the package is inspired by my cats, Cookie (the grey-strip one in the figure below) and Milk (the black one in the figure below).

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

**NOTE**: Like many other Python packages, *cookiemilk* functions the same way on devices with different operating systems. This means you can run the example code in this tutorial on either a Windows PC or a Mac. The only difference is the method of installation.

## 1.3 Import
```
import cookiemilk
```

## 1.4 Main functions

|Usage             | Functions     | Description |
|:-----------------|:--------------|:------------|
|Data arrangement  |cmap2graph              | import a concept map and convert it into a graph          |
|                  |text2graph              | import a text and convert it into a graph                 |
|Data processing   |pathfinder_network      | calculate the PFNet of a given graph                      |
|                  |calc_surface_matching   | calculate the surface similarity between two graphs       |
|                  |calc_graphical_matching | calculate the graphical similarity between two graphs     |
|                  |calc_gcent              | calculate the graphical centrality (GC) of a given graph  |
|                  |numerical_sim           | calculate the numerical similarity                        |
|                  |calc_tversky            | calculate Tversky's similarity between two graphs       |
|Visualization     |draw                    | plot and/or save a graph                                  |
|                  |average_graph           | generate an average graph                                 |
|Others            |quick_analysis          | conduct data analysis using the above functions           |

## 1.5 Dependencies
`networkx`: A Python package for network analysis

`numpy`: A Python package for scientific computing

`pywebview`: A Python package for building GUI with JavaScript, HTML, and CSS

`d3.js`: A JavaScript library for manipulating documents based on data

## 1.6 Citation
To cite *cookiemilk* in publications use:

Wei, Z., Zhang, Y., Clariana, R. B., & Chen, X. (2024). The effects of reading prompts and post-reading generative learning tasks on multiple document integration: Evidence from concept network analysis. Educational Technology Research and Development, 72, 661–685. [https://doi.org/10.1007/s11423-023-10326-w](https://doi.org/10.1007/s11423-023-10326-w)
