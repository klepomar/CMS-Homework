import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class plotManipulator:

    def __init__(self, *args, **kwargs):
        """Init function, csv file is loaded here and split into sample"""
        """ALso metada are stored and can be use later."""
        """Number of rows is also cut from all blank lines"""
        self.file = pd.read_csv(args[0], header=1, delimiter=",")
        rng = [2 * n for n in range(1, len(self.file.columns) // 2)]
        self.dfs = np.split(self.file, rng, axis=1)
        self.meta_data = []
        for n in range(len(self.dfs)):
            self.dfs[n] = self.dfs[n].rename(columns={'Wavelength (nm).' + str(n): 'Wavelength (nm)', 'Abs.' + str(n): 'Abs'})
            pom = self.dfs[n]
            index = np.where(pd.isnull(pom))
            index = np.where(pd.isnull(pom))
            index = index[0][0]
            pom_cela = pom.iloc[:index]
            self.meta_data.append(pom.iloc[index:])
            self.dfs[n] = pd.DataFrame(pom_cela)

    def which_samples(self):
        """Function for determine which sample wants to choose. Accept integer"""
        print("Input number of sample which you want to use for plot.\n")
        while True:
            self.sample = input()
            if(self.sample.isdigit() and int(self.sample) > 0 and int(self.sample) <= len(self.dfs) ): # add comparison if sample is okay
                self.sample = int(self.sample) - 1
                break
            else:
                print("Wrong input. Try again.\n")
                continue

    def which_lines(self):
        """Function for determine which interval wants to choose."""
        """ Accept integer and strin all(Not Case Sensitive). And prepare to plot"""
        print("Input interval of lines which you want to plot, separated by ',' ."
              "If you want to use all lines type all.\n")

        while True:
            self.inpt = input()
            if (self.inpt.capitalize() == "ALL"):  # add comparison if sample is okay
                self.to_plot = self.dfs[self.sample]
                break
            self.interval = tuple(self.inpt.split(','))
            """and int(self.interval[1]) <= self.dfs[self.sample].columns"""
            if (len(self.interval) == 2 and int(self.interval[0]) > 0 and int(self.interval[1]) > int(self.interval[0])):
                pom = int(self.interval[1]) - int(self.interval[0]) + 1
                self.to_plot = self.dfs[self.sample].head(int(self.interval[1]))
                self.to_plot = self.to_plot.tail(pom)
                break
            else:
                print("Wrong input. Try again.\n")
                continue

    def plot_Graph(self):
        """Function for plotting"""
        try:
            self.to_plot.plot(x="Abs", y="Wavelength (nm)")
            plt.show()
        except:
            self.to_plot = self.to_plot.astype(float)
            self.to_plot.plot(x="Abs", y="Wavelength (nm)")
            plt.show()
