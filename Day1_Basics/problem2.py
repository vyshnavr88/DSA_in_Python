import heapq
def num():
    nums = [7, 3, 9, 1, 5]
    heapq.heapify(nums)
    print(nums[0])
def large():
    nums = [8, 2, 10, 4, 6]
    print((heapq.nlargest(3,nums)))
def sort():
    nums = [5, 1, 9, 3, 7]
    heapq.heapify(nums)
    main = []
    heapq.heappush(main,heapq.heappop(nums))
    heapq.heappush(main,heapq.heappop(nums))
    heapq.heappush(main,heapq.heappop(nums))
    heapq.heappush(main,heapq.heappop(nums))
    heapq.heappush(main,heapq.heappop(nums))
    print(main)
sort()


    

   




    
