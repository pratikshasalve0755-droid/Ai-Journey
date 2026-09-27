# Practice 2 — Multiple Threads

## 📌 Objective

The objective of this practice is to understand how multiple threads can be created and used to execute multiple tasks concurrently.

## 🧠 Concepts Learned

- Creating multiple threads
- `Thread()` class
- `target` parameter
- `start()` method
- `join()` method
- Concurrent task execution
- Thread execution order
- Difference between sequential and concurrent execution

## 🔧 Technologies Used

- Python
- `threading`
- `time`

## 📚 What I Practiced

In this practice, I created multiple independent task functions and assigned each task to a separate thread.

Example flow:

Task 1 → Thread 1  
Task 2 → Thread 2  
Task 3 → Thread 3

The threads were then started and joined.

## 🔄 Thread Workflow

Create Thread 1  
Create Thread 2  
Create Thread 3  
↓  
Start Thread 1  
Start Thread 2  
Start Thread 3  
↓  
Wait using `join()`  
↓  
Continue Main Program

## 🎯 Key Learning

I learned that multiple threads can make progress concurrently.

I also observed that the output order may not always be the same because thread execution is managed by the operating system and Python's thread scheduler.

## 🚀 Outcome

Successfully created a program using multiple threads and developed a basic understanding of concurrent task execution in Python.