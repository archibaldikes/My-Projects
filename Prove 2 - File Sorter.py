'''
Ben Bennington
CS 241
'''
import csv 



def main():
    file = getFile()
    print()
    average(file)
    print()
    max(file)
    print()
    min(file)
 


def getFile():
    fileName = input('Please enter the data file: ')
    return fileName
    

def average(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        comRate = [float(row[6]) for row in reader]
        avg = (sum(comRate) / int(len(comRate)))
        print('The average commercial rate is: ' + str(avg))
    return 

        
def max(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        high = 0
        zipcode = 0
        state = 0
        name = 0
        for row in reader:
            if float(row[6]) > high:
                          high = float(row[6])
                          zipcode = row[0]
                          state = row[3]
                          name = row [2]
        print('The highst rate is: ')
        print('{} ({}, {}) - ${}'.format(name, zipcode, state, high))
        return


def min(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        low = 2
        zipcode = 0
        state = 0
        name = 0
        for row in reader:
            if float(row[6]) < low:
                          low = float(row[6])
                          zipcode = row[0]
                          state = row[3]
                          name = row [2]
        print('The lowest rate is: ')
        print('{} ({}, {}) - ${}'.format(name, zipcode, state, low))
        return


if __name__ == "__main__":
    main()

