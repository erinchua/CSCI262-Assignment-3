import os, sys

dog_breeds = ["Shih Tzu", "Chow Chow", "Husky", "Pekingnese"]
tempList = []

with open('dog_breeds.txt', 'w') as writer:
    for i in dog_breeds:
        print(i)
        tempList.append(i)
        tempList.append(":")

    print(tempList)
    writer.writelines(tempList)