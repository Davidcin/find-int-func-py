a = [1,1,1,1,1,1,10,1,1,1,1]
def find_it(array):
     for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count+=1
        if count % 2 != 0:
            return array[i]
print(find_it(a))