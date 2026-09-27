# Practice 3 — Sequential vs Multithreading

## 📌 Objective

The objective of this practice is to compare sequential execution with multithreaded execution using the same set of tasks.

## 🧠 Concepts Learned

- Sequential execution
- Multithreading
- `Thread()` class
- `start()` method
- `join()` method
- `time.perf_counter()`
- Execution-time measurement
- Comparing sequential and concurrent execution

## 🔹 Version A — Sequential Execution

In the sequential version, the three tasks are executed one after another.

```text
Task 1
  ↓
Task 2
  ↓
Task 3