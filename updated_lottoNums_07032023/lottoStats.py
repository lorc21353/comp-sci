lottoNums = []
frequencyTable = []
maxValue = 100
debugMode = -1
# init Table
# using a frequency table makes it very easy to avoid recursion, making it faster for large data sets such as all previous lotto numbers
maxValue += 1
for i in range(maxValue):
    frequencyTable.append(0)


print("type a non-number to exit the loop")
while True:
    try:
        lottoNums.append(int(input("enter a number: ")))
    except:
        if lottoNums == []:
            if input("Enter debug mode? ") == "1":
                f = open("randnums.csv")
                tempNums = f.read().split(",")
                for i in tempNums:
                    lottoNums.append(i)
                f.close()
            else:
                print("cannot run on empty data set")
                raise Exception("err: cannot run on empty set")
                
        break
    
    
# getting the biggest and smallest here allows me to use an unsorted list
biggest = int(lottoNums[0])
smallest = int(lottoNums[0])
for i in lottoNums:
    w = int(i)
    frequencyTable[w]+=1
    if w < smallest:
        smallest = w
    if w > biggest:
        biggest = w
    
for i in range(len(frequencyTable)):
    if frequencyTable[i] > 0:
        print(str(i)+":", frequencyTable[i])
        
print("range:", biggest-smallest)