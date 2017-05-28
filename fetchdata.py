from tkinter import Button, Label, NONE
import matplotlib.pyplot as graphs
import graph_data as graphInstance

'''
A class that allows a secondary window to be created to display data
parsed from the Google Finance Website for the selected stock

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 26 May 2017

'''


class FetchData:

    def __init__(self, main_window):
        '''
        Initializes the window that projects the graph data for the stock markets. This
        is built on top of the main window which allows the user to choose options regarding
        which stock to view data for

        Args:
            main_window (Toplevel widget on screen SCREENNAME): The main window onto which we are projecting the graph data
        '''
        self.main_window = main_window
        self.dataset = NONE


    def build_menu(self):
        '''
        Builds a menu for the user to select a stock's detail from

        '''
        dowButton = Button(self.main_window, text = "DOW", bg="lightblue", command= lambda: self.parse_data("DOW"))
        dowButton.grid(row=2, column=0, pady=25)

        microsoftButton = Button(self.main_window, text = "Microsoft", bg="lightblue",
                                 command = lambda: self.parse_data("MSFT"))
        microsoftButton.grid(row=3, column=0, pady=25)

        yahooButton = Button(self.main_window, text = "Yahoo", bg="lightblue", command= lambda: self.parse_data("YHOO"))
        yahooButton.grid(row=4, column=0, pady=25)

        netflixButton = Button(self.main_window, text="Netflix", bg="lightblue", command= lambda: self.parse_data("NFLX"))
        netflixButton.grid(row=5, column=0, pady=25)

        ciscoButton = Button(self.main_window, text="Cisco", bg="lightblue", command= lambda: self.parse_data("CSCO"))
        ciscoButton.grid(row=6, column=0, pady=25)

        bankOfAmericaButton = Button(self.main_window, text="Costco Wholesale Corporation", bg="lightblue",
                                     command= lambda: self.parse_data("COST"))
        bankOfAmericaButton.grid(row=7, column=0, pady=25)


    def parse_data(self, stock_code_name):
        '''
        Parses the data from the downloaded excel sheet given by the Google Finance Link

        Args:
            stock_code_name (str): The stock name's code that we are querying for
        '''
        constructedList = graphInstance.parse_data(stock_code_name)
        self.dataset = constructedList
        allLabels = self.return_labels(self.dataset)
        self.grid_all_labels(allLabels, stock_code_name)


    def return_labels(self, given_stock_spreadsheet):
        '''
        Displays the most recent numerical data for the selected stock on the screen
        once the stock is selected from the menu

        Args:
            given_stock_spreadsheet (list)(list) The parsed data from the spreadsheet in the form of a 2D
                List (list within list). We select list[1] for each case to skip over the titles on the file,
                and our next index, and the next index is the data we want
        Returns:
            (list) : A list of labels that can be attached to the GUI when displaying the initial data
                for the stock
        '''
        allLabels = []

        allLabels.append(Label(self.main_window, text = "Most Recent Date :   "))
        allLabels.append(Label(self.main_window, text = given_stock_spreadsheet[1][0]))

        allLabels.append(Label(self.main_window, text = "Stock Opening Value :   "))
        allLabels.append(Label(self.main_window, text = given_stock_spreadsheet[1][1]))

        allLabels.append(Label(self.main_window, text = "Highest Value of Stock (During Date) :   "))
        allLabels.append(Label(self.main_window, text = given_stock_spreadsheet[1][2]))

        allLabels.append(Label(self.main_window, text = "Lowest Value of Stock (During Date) :   "))
        allLabels.append(Label(self.main_window, text = given_stock_spreadsheet[1][3]))

        allLabels.append(Label(self.main_window, text = "Stock Closing Value :   "))
        allLabels.append(Label(self.main_window, text = given_stock_spreadsheet[1][4]))

        allLabels.append(Label(self.main_window, text = "Volume of Stocks Traded (During Date) :   "))
        allLabels.append(Label(self.main_window, text = given_stock_spreadsheet[1][5]))

        return allLabels


    def grid_all_labels(self, all_labels, stock_code_name):
        '''
        Puts all the constructed values on the appropriate spaces on the GUI's grid.

        Args:
            all_labels (list) : A list of all the constructed labels
            stock_code_name (str) : The name of the stock we have parsed the data for
        '''

        stockTitle = Label(self.main_window, text = stock_code_name, font=("Sans-Serif", 20))
        stockTitle.grid(row=1, column=0, columnspan=3)

        viewGraphButton = Button(self.main_window, text = "View Graph", bg="lightblue",
                                 command=lambda: self.plot_all_lines(stock_code_name))
        viewGraphButton.grid(row=2, column=2)

        all_labels[0].grid(row=3, column=1, pady=25)
        all_labels[1].grid(row=3, column=2, pady=25)

        all_labels[2].grid(row=4, column=1, pady=25)
        all_labels[3].grid(row=4, column=2, pady=25)

        all_labels[4].grid(row=5, column=1, pady=25)
        all_labels[5].grid(row=5, column=2, pady=25)

        all_labels[6].grid(row=6, column=1, pady=25)
        all_labels[7].grid(row=6, column=2, pady=25)

        all_labels[8].grid(row=7, column=1, pady=25)
        all_labels[9].grid(row=7, column=2, pady=25)

        all_labels[10].grid(row=8, column=1, pady=25)
        all_labels[11].grid(row=8, column=2, pady=25)


    def plot_all_lines(self, stock_code_name):
        '''
        Plots the lines of the stock opening values and stock closing values

        Args:
            stock_code_name (str): The name of the stock we are parsing data for
        '''

        selectedStockData = graphInstance.parse_data(stock_code_name)
        graphs.title("Data for {}".format(stock_code_name))

        # Plots all available data for stock opening values
        graphs.plot(graphInstance.collect_all_opening_values(selectedStockData))

        # Plots all available data for stock closing values
        graphs.plot(graphInstance.collect_all_closing_values(selectedStockData), 'r')

        graphs.xticks([])

        graphs.ylabel('Value in USD ($)')
        dateList = graphInstance.collect_date_range(selectedStockData)
        graphs.xlabel('Data Between Dates {} and {}'.format(dateList[-1], dateList[0]))

        graphs.text(125, 60, "Blue -> Stock Opening Values for the Day")
        graphs.text(123, 59, "Red -> Stock Closing Values for the Day")

        graphs.grid(True)
        graphs.show()
