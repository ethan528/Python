n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
answer = []
for i,j in zip(arr1,arr2):
    a12 = str(bin(i|j)[2:])
    a12=a12.zfill(n)
    a12=a12.replace('1','#')
    a12=a12.replace('0',' ')
    answer.append(a12)
print(answer)