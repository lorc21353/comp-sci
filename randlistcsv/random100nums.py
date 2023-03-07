#import random and create empty str
import random
nums = ""

# generate 100 nums
for i in range(100):
    randNumber = random.randint(0,100)
    nums += str(randNumber)+","

#open the file and write it
f = open("randlist.csv", "w")
f.write(nums)
f.close()