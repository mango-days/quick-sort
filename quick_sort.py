array = [1, 4, 9, 3, 5, 2, 8, 6, 7]
def quick (array):
    if (len(array)>1):
        pivot = array[-1]
        i=-1
        for j in range (0, len(array)-1, 1):
            if (array[j]<pivot):
                i+=1
                temp= array[i]
                array[i]=array[j]
                array[j]=temp
        array[-1] = array[i+1]
        array[i+1] = pivot
        return (quick(array[:i+1]) + array[i+1: i+2] + quick(array[(i+2):]))
    return (array)
print(quick(array))