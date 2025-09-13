📝 Time & Space Complexity Notes
1️⃣ Time Complexity

Time Complexity measures how fast an algorithm runs as the input size n grows.

Common Types
Complexity	Example	Growth
O(1)	Accessing arr[0]	Constant
O(log n)	Binary Search	Logarithmic
O(n)	Linear Search	Linear
O(n log n)	Merge Sort, Quick Sort	Linearithmic
O(n²)	Bubble Sort, Nested Loops	Quadratic
O(2ⁿ)	Recursive Fibonacci	Exponential
2️⃣ Space Complexity

Space Complexity measures how much extra memory your algorithm uses as input grows.

Common Examples
Algorithm	Extra Memory	Space Complexity
Linear Search	Only variables i, target	O(1)
Binary Search (iterative)	Variables low, high, mid	O(1)
Binary Search (recursive)	Function call stack	O(log n)
Copy array	New array same size	O(n)

💡 Key Idea:

O(1) → constant extra memory

O(n) → grows linearly with input

O(n²) → grows quadratically

3️⃣ Notes / Tips

Counting only extra memory used, not input size itself.

Recursion uses call stack memory, so recursive algorithms may use extra space.

Always aim for low time + low space if possible.