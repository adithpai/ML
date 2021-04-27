import random 
import csv
attributes = []

print("\n Given training dataset is : \n")

with open('../input/datasetfinds/data-find_s.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        attributes.append (row)
        print(row)
        
print("\nThe total number of training instances are : ",len(attributes))

noOfattr = len(attributes[0])-1

print("\nThe initial hypothesis is : ")
init_hypothesis = ['0']*noOfattr
print(init_hypothesis)

for j in range(0,noOfattr):
        init_hypothesis[j] = attributes[0][j]
        
for i in range(0, len(attributes)):
    if attributes[i][noOfattr] == 'Yes':
        print ("\nInstance ", i+1, "is", attributes[i], " and is Positive Instance")
        for j in range(0,noOfattr):
                if attributes[i][j]!=init_hypothesis[j]:
                    init_hypothesis[j]='?'
                else :
                    init_hypothesis[j]= attributes[i][j] 
                    
        print("The hypothesis for the training instance", i+1, " is: " , init_hypothesis, "\n")
        
     
    if attributes[i][noOfattr] == 'No':
        print ("\nInstance ", i+1, "is", attributes[i], " and is Negative Instance")
        print("The hypothesis for the training instance", i+1, " is: " , init_hypothesis, "\n")
        
        

print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(init_hypothesis)