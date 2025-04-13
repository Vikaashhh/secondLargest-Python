class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
            
        largest = second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
                
        return second_largest if second_largest != float('-inf') else -1

if __name__ == "__main__":
    # Take input as space-separated numbers
    input_numbers = input("Enter numbers separated by spaces: ")
    # Convert to list of integers
    arr = list(map(int, input_numbers.split()))
    # Create Solution object and get result
    sol = Solution()
    result = sol.getSecondLargest(arr)
    # Print the output
    print("Second largest number is:", result)
