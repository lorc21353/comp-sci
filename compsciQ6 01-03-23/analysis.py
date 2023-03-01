people = []
sales = []

newDay = input("New day? (Y/N): ").lower()

if newDay == "y" or newDay == "n": 
    numberOfPeople = int(input("How many Employees are there? "))

if newDay == "y":
    people.append("\n"+input("Enter Name: ")+",")
    sales.append("\n"+input("Enter their number of sales in euros: €")+",")
elif newDay == "n":
    people.append(input("Enter Name: ")+",")
    sales.append(input("Enter their number of sales in euros: €")+",")
if newDay == "y" or newDay == "n": 
    for i in range(numberOfPeople-1):
        people.append(input("Enter Name: ")+",")
        sales.append(input("Enter their number of sales in euros: €")+",")
    
    
if newDay == "y" or newDay == "n":  
    totalSales = input("Enter total sales in euros: €")+","


finalPeople = ""
for i in people:
    finalPeople += i

finalSales = ""
for i in sales:
    finalSales += i 

f = open("people.csv", "a")
f.write(finalPeople)
f.close()

f = open("sales.csv", "a")
f.write(finalSales)
f.close()

if newDay == "y":
    f = open("totalSales.csv", "a")
    f.write("/n"+totalSales)
    f.close()
elif newDay == "n":
    f = open("totalSales.csv", "a")
    f.write(totalSales)
    f.close()
    
if newDay == "0":
    print("\n")
    f = open("people.csv")
    print(str(f.read()))
    f.close()
    print("\n")
    
    f = open("sales.csv")
    print(str(f.read()))
    f.close()
    print("\n")
    
    f = open("totalSales.csv")
    print(str(f.read()))
    f.close()