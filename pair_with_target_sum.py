class Soultion:
    def search(selfself, arr, targetSum):
        left, right = 0, len(arr)-1
        while (left < right):
            currentSum = arr[left] + arr[right]
            if currentSum == targetSum:
                return [left, right]

            if targetSum > currentSum:
                left += 1 # bigger sum
            else:
                right -= 1 # smaller sum
        return [-1,-1] # if not found

# testing
def main():
    sol = Soultion();
    print(sol.search([1,2,3,4,6], 6))
    print(sol.search([2,2,5,9,11],11))

main()