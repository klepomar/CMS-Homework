# CMS-Homework

This small program is used for plotting data from csv file.
It is possible to choose which sample and which lines (spectrum) we want to plot
into graph.

There are also meta data for which I didnt find purpose at this demo. But they are saved and it is possible to work with them if needed.

This is pip package which can be install by typing:
*python3 -m pip install dist\cms-0.0.2-py3-none-any.whl*
then we need to *import data_plot* and then we ca use function plot_data
wich accept one paramater and that is path to data file.

Modules required are as follow. Matplotlib, Pandas, numPy. These are standart modules for Python. They should not cause any problem. Used version of Python is 3.8

I encountered 1 bug. Sometimes dataframe plot whil throw exception. I resolved to try except syntax use. And was able to plot it anyway.


Marco Klepoch