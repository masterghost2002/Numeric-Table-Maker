############################### Numeric Table Calculator using a function ####################################
x = int(input("Enter The Number Of Which Table You Want\n"))

############################### Function for Multiplying The Values ##########################################
def table(n):
    return n * i ######################3 i is taken from for loop as a range ################################

"""
                            I have divided It Into Two parts
                            1. The range is fixed it will calculate table from  1 to 10 as normally we found
                            2. You can enter Range Manusally from where to where You want to Calculate Table

                                        by Rakesh Dhariwal
"""
range_selector = int(input("Please Select The Range From Where To Where U To Multiply\n1.Fixed Range(1-10)\n2.Enter Ending And Starting Point Manually\n"))

#################################### Applying The loops ##########################################33

if range_selector == 1:
    print(f"The Table Of {x} is: ")
    for i in range(1, 11):
        print(f"{x} x {i}   =  ", table(x))
elif range_selector == 2:
    print(f"The Table Of {x} is: ")
    for i in range(int(input("Starting Point Of Table\n")), int(input("Enter The Ending Point Of Table\n")) + 1):
        print(f"{x} x {i}  =  ", table(x))
else:
    print("Thank You For Using")


######################################## Rakesh Dhariwal  ##############################################

a = input()