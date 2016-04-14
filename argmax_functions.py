import numpy as np

#write a function that will return the index of the highest value in an array, arr
#arr = [-1,0,5,1,5,3,4,3]


def argmax1(arr):
    ''' Returns the index from the largest item in an array
    Input: int list
    Return: int
    '''
    largest_int = max(arr)
    for a, i in enumerate(arr):
        if largest_int == i:
            return a



if __name__ == '__main__':
    arr = [-1,0,5,1,5,3,4,3]

    #reference answer from numopyp library
    print np.argmax(arr)
    print argmax1(arr)
