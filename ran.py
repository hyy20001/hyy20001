CODE 
import random # Generates a list of 100 random integers between 10 and 200. 
data = set() 
while len(data)<100: 
data.add(random.randint(10,200)) 
data = list(data) # Display the contents of the list 2pts print(data) print("\n