lottoNums = []
frequencyTable = []
maxValue = 100
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
         break
    
# getting the biggest and smallest here allows me to use an unsorted list
biggest = lottoNums[0]
smallest = lottoNums[0]
for i in lottoNums:
    frequencyTable[i]+=1
    if i < smallest:
        smallest = i
    if i > biggest:
        biggest = i
    
for i in range(len(frequencyTable)):
    if frequencyTable[i] > 0:
        print(str(i)+":", frequencyTable[i])
        
print("range:", biggest-smallest)