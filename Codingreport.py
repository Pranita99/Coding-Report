import random
error_comment="String"
errors=random.randint(0,10)
lines_of_code=random.randint(10,200)
test_cases_passed_hidden=random.randint(0,16)
time_execution=random.sample(range(1,11),8)
time_complexity=12
threshold=4
f= open("report.txt","w+")
import matplotlib.pyplot as plt 

# corresponding y axis values 
y = time_execution
x = [item for item in range(1, len(y)+1)]

# plotting the points 
plt.plot(x, y, color='red', marker='o', markerfacecolor='red', markersize=5, ls='--') 

# setting x and y axis range 
plt.ylim(0,max(y)+1) 
plt.xlim(0,max(x)+1) 

# naming the x axis 
plt.xlabel('Test Case') 
# naming the y axis 
plt.ylabel('Time of Execution') 

# giving a title to my graph 
plt.title('Execution Time') 
