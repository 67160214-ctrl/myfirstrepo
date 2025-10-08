class BubbleSorter:
    def __init__(self,list):
        self.list = list
    
    def display(self):
        return self.list
    
    def sort(self):
        n = len(self.list)
        for i in range(n):
            for j in range(0,n - i -1):
                if self.list[j] > self.list[j + 1]:
                   self.list[j] , self.list[j+1] = self.list[j+1], self.list[j]
            print(f"After round {i + 1}: {self.display()}")

if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)

    print("Before sorting:")
    print(sorter.display())

    sorter.sort()

    print("After sorting:")
    print(sorter.display())