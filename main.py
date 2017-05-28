from tkinter import Tk, Label
import fetchdata as fetch_data

'''
The entry point of the programme from the command line.

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 26 May 2017

'''

WINDOW_WIDTH = 1000         # The height of the main window initialized
WINDOW_HEIGHT = 600         # The width of the main window initialized


def main():
    '''
    The entry point of the programme from the command line
    '''
    mainWindow = Tk()
    mainWindow.wm_title("Stock Markets")
    mainWindow.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))

    title = Label(mainWindow, text="The Stock Market", font=("Sans-Serif", 35))
    title.grid(row = 0, column = 0, padx = (WINDOW_WIDTH / 2) - (WINDOW_WIDTH / 6), columnspan = 3, pady = 15)

    instance = fetch_data.FetchData(mainWindow)
    instance.build_menu()

    mainWindow.mainloop()


if __name__ == '__main__':
    main()
