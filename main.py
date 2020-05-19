from plotManipulator import plotManipulator


if __name__ == "__main__":

    q = "0"
    print("To exit program please press q")
    while q != "q":
        plotter = plotManipulator('data.csv')
        plotter.which_samples()
        plotter.which_lines()
        plotter.plot_Graph()
        print("To exit program please press q. If you want to continue press any other key.\n")
        q = input()