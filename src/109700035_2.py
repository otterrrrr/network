N = input()
for i in range(int(N)):
    nums = list(map(int, input().split(" ")))
    nums.pop(0)

    a = 0
    b = sum(nums)

    min_value = float("inf")
    min_index = -1

    for j in range(1, len(nums)+1, 1):
        a = a + nums[j-1]
        b = b - nums[j-1]
        A = a // j

        if (len(nums) - j) == 0:
            B = 0
        else:    
            B = b // (len(nums) - j)

        result = abs(A - B)
        #print(A,B)
        if result < min_value:
            min_value = result
            min_index = j-1
    print(min_index) 


