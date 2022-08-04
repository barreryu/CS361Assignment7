import csv

# main function that intereacts with user
def main():
    
    # prints out question and takes in user input
    print("Please enter in the stock ticker you are interested in:")
    x = input()

    # opens CSV file that contains all stock tickers and their correspoinding values
    file = csv.reader(open("/Users/Andi/Documents/CS361/Assignment7/stock_information_from_yfinance.csv", "r"))
    
    # iterates through the rows in the csv file to search for the ticker that the user inputted
    for row in file:

        # if the user input matches with the stock ticker they are searching for in the csv file
        if x == row[0]:

            # opens up file where the value will be placed into and write the corresponding ticker value
            placeinto = open("/Users/Andi/Documents/CS361/Assignment7/stock_information_for_display.txt", "w")
            placeinto.write(str(row[3]))
            placeinto.close

            # gives the user the value they are searching for
            print("The price of the ticker you are interested in is: $" + str(row[3]))

            return
    
    # tells user the ticker they search is not found in the file
    print("The ticker you searched for could not be found, sorry!")
    return
    

main()