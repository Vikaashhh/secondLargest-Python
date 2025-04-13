# 📌 Day-1: Find the Second Largest Number – Python DSA Challenge

Welcome to Day 1 of my **160 Days of DSA in Python** challenge! 🚀  
This project is part of a daily commitment to strengthen my Data Structures and Algorithms (DSA) foundation using Python.

---

## 🧠 Problem Statement

**Objective:**  
Given an array of integers, your task is to find the **second largest** number in the list.  
If no such number exists (e.g., all elements are the same or array has less than two elements), return `-1`.

---

## ✅ Example

**Input:**
12 23 34 45 534

**Output:**
Second largest number is: 45

---

## 🧾 Approach

The solution follows a **single-pass** logic with `O(n)` time complexity:

1. Initialize two variables `largest` and `second_largest` with negative infinity.
2. Traverse the array:
   - Update `largest` and `second_largest` accordingly.
3. If a valid `second_largest` is found (not `-inf`), return it; otherwise, return `-1`.

---

## 🧑‍💻 Code Overview

```python
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
```
The code includes an interactive CLI that allows users to input space-separated integers and see the second largest number instantly.

🏁 How to Run
Make sure Python is installed on your system.

Clone the repository or download the Python file.

Open a terminal and navigate to the project directory.

Run the script:
python SecondLargest.py

Input your numbers when prompted.


📂 File Structure
bash
Copy
Edit
Day-1-SecondLargest/
│
├── SecondLargest.py     # Main Python logic
└── README.md             # Project documentation

📌 Topics Covered
- Arrays
- Conditional logic
- Edge case handling
- Python I/O
-Clean code structure


🚀 What's Next?
I’ll be updating this repository daily with fresh problems from the GeeksforGeeks 160 Days DSA Challenge, complete with clean Python implementations and insights. Follow along to grow with me! 🌱


🤝 Let's Connect
📷 Instagram – @framesby.vikash
💼 LinkedIn – Vikash Joshi

