# Zigzag.py

print("Name:Tejaswini M",
       "AUID:1AY24AI111",
       "Section:O")
print("Enter the number of zigzag lines to be printed:")
n=int(input())
for _ in range(n):  
    for i in range(5):
        print(" " * i + "*")
    for i in range(3, -1, -1):
        print(" " * i + "*")