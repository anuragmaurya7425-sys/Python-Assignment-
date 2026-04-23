# Demonstrate use of break, continue, and pass in loops.

# Use of break statement 
for i in range(1, 11):
    if i == 5:
        break      # break terminate the loop
    print(i ,end=" ")
    
# Use of continue statement
for j in range(1,11):
    if j == 5:
        continue        # continue skip the current iteration and goes for next iteration
    print(j , end=" ")

# # Use of pass statement
for i in range(1, 11):
    pass                    # pass is use for future writing code if need any update