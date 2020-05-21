from plotManipulator import plotManipulator


def plot_data(name):
    """Main function for plotting accepting one parameter which should be name of file"""
    q = "0"
    print("To exit program please press q")
    while q != "q":
        plotter = plotManipulator(name)
        plotter.which_samples()
        plotter.which_lines()
        plotter.plot_Graph()
        print("To exit program please press q. If you want to continue press any other key.\n")
        q = input()