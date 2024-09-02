def Merge_Sort_Iterative(A, p, q, r):
    n_L = q - p + 1
    n_R = r - q
    L = [0] * n_L  # Creates a list L with n_L elements
    R = [0] * n_R  # Creates a list R with n_R elements

    # Copy data to temp arrays L[] and R[]
    for i in range(n_L):
        L[i] = A[p + i]

    for j in range(n_R):
        R[j] = A[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n_L and j < n_R:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1

    # Copy remaining elements of L[], if any
    while i < n_L:
        A[k] = L[i]
        i = i + 1
        k = k + 1

    # Copy remaining elements of R[], if any
    while j < n_R:
        A[k] = R[j]
        j = j + 1
        k = k + 1

if __name__ == "__main__":
    A = [2, 4, 5, 1, 3, 9]
    p = 0 #starting index of subarray
    q = int(len(A)//2)  # Midpoint of the subarray
    r = len(A) - 1 #ending index of subarray
    Merge_Sort_Iterative(A, p, q, r)
    print("Sorted array:", A)


def Merge_Sort_Recursive(A,p,r):
    if p >= r:
        return
    if p < r:
        q = (p + r) // 2
        Merge_Sort_Recursive(A, p, q)
        Merge_Sort_Recursive(A, q + 1, r)
        Merge_Sort_Iterative(A, p, q, r)
    return A

if __name__ == "__main__":
    A = [2, 4, 5, 1, 3, 9]
    p = 0
    r = len(A) - 1
    sorted_A = Merge_Sort_Recursive(A, p, r)
    print("Sorted Recursively:", sorted_A)
