import csv 

filename = "data.csv"

def main():
    csv_file = open(filename, 'a')
    wr = csv.writer(csv_file)
    wr.writerow([["one", "two", "three", "four"], "blue", "5", "342.2"])
    
main()
