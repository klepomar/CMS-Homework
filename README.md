# CMS-Homework

This small program is used for plotting data from csv file.
It is possible to choose which sample and which lines (spectrum) we want to plot
into graph.

There are also meta data for which I didnt find purpose at this demo. But they are saved and it is possible to work with them if needed.

Application is run from main.py. But all operations are corporated into class plotHandler.User can interact with application using command line first time he is asked which sample wants to use. If number is bigger than number of samples store in memory then he is informed about this and can enter sample number again. After choosing sample user can define which lines need to be plotted. If all lines need to be plotted it is neccesery to write all into command line (not case sensitive).
Interval ends are seprated by ','. It is also important to start with smaller number and end with bigger. Again if any problem occure. You are inform about invalidity of your input and you can try again. 

Modules required are as follow. Matplotlib, Pandas, numPy. These are standart modules for Python. They should not cause any problem. Used version of Python is 3.8

I encountered 1 bug. Sometimes dataframe plot whil throw exception. I resolved to try except syntax use. And was able to plot it anyway.


Marco Klepoch