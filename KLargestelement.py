size = 0
i = 0
j = 0
k = 0
temp = 0
print("enter array size")
size = int(input())
# creating an array of size specified by user
Arr = []
print("enter array values")
for i in range(size):
    x = int(input())
    Arr.append(x)
print("enter k value")
k = int(input())
# Sorting in increasing order using bubble sort
for i in range(size):
    for j in range(size):
        if Arr[i] < Arr[j]:
            # swap arr[i] and arr[j]
            Arr[i], Arr[j] = Arr[j], Arr[i]
print("sorted array is:")
# display output
for i in range(size):
    print(Arr[i], end=" ")
# display the Kth largest value
print(kth + "largest value is" + str(Arr[k - 1]))
