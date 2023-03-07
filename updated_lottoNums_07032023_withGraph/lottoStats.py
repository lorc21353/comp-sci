#import libraries
import matplotlib.pyplot as plt

# declare my variables
lottoNums = []
frequencyTable = []
maxValue = 100
debugMode = -1
# init Table
# using a frequency table makes it very easy to avoid recursion, making it faster for large data sets such as all previous lotto numbers
maxValue += 1
# create the frequency table and give it the amount of value spots it needs to account for every number possible in the data set
for i in range(maxValue):
    frequencyTable.append(0)


print("type a non-number to exit the loop")
while True:
    try:
        lottoNums.append(int(input("enter a number: ")))
    except:
        #check if list is empty
        if lottoNums == []:
            #ask user to enter debug mode
            if input("Enter debug mode? ") == "1":
                #open file
                f = open("randnums.csv")
                #read and split the file into an array
                tempNums = f.read().split(",")
                #move the numbers into a fresh array (the original csv array sometimes causes problems if not formatted perfectly)
                for i in tempNums:
                    lottoNums.append(i)
                #close the file
                f.close()
            else:
                # if the list is still empty throw an error
                print("cannot run on empty data set")
                raise Exception("err: cannot run on empty set")
        # exit the loop
        break
    
    
# getting the biggest and smallest here allows me to use an unsorted list
biggest = int(lottoNums[0])
smallest = int(lottoNums[0])
# for all the numbers in lottonums list get the value, convert it into an integer
for i in lottoNums:
    w = int(i)
    # increment the position assigned to that number in the table by one (the assigned space is equal the the index value of that number)
    frequencyTable[w]+=1
    # check if that number is a new smallest or biggest
    if w < smallest:
        smallest = w
    if w > biggest:
        biggest = w
    
delete = []
oneToHundred = []
# for the length of the frequency table check if that section has at least one as a value and print it if it does
for i in range(len(frequencyTable)):
    if frequencyTable[i] > 0:
        print(str(i)+":", frequencyTable[i])
        oneToHundred.append(i)
    else:
         delete.append(i)
         
    
# minus the biggest and smallest to get the range and print it to console
print("range:", biggest-smallest)


# create graph
for i in reversed(delete):
    del(frequencyTable[i])
#for i in range(maxValue):
#    oneToHundred.append(i+1)
plt.pie(frequencyTable, labels = oneToHundred)
plt.legend(["frequency"])
plt.title("Frequency plot for entered values")
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.show()