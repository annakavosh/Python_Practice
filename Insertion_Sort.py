# Insertion Sort

class SortAlgo:
    def __init__(self, A, n):
        self.A = A
        self.n = n

    def Insertion_Sort(self):
        for i in range(1, self.n):
            key = self.A[i]
            #insert A[i] into the sorted subarray A[1:i-1]
            j = i - 1
            while j >= 0 and self.A[j] > key:
                self.A[j+1] = self.A[j]
                j = j -1
            self.A[j+1] = key
        return self.A


if __name__ == "__main__":
    A= [3,5,2,4,6,7,1]
    n = len(A)
    sorter = SortAlgo(A, n)
    sorted_A = sorter.Insertion_Sort()
    print(sorted_A)


# A= [3,5,2,4,6,7,1]
# n = len(A)
# sorted_A = Insertion_Sort(A, n)
# print(sorted_A)