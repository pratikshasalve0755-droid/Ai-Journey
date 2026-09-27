
---

# 📘 Practice 2 — Employee Salary Filter

**File:** `Practice_2_Employee_Salary_Filter/README.md`

```markdown
# Practice 2 – Employee Salary Filter

## 📌 Description

This practice program demonstrates how List Comprehension can be used to filter employee salary data.

The program identifies employees based on their salary conditions.

---

## 🎯 Objective

The objective is to understand how List Comprehension can be used to filter and process structured data.

---

## 🧠 Concepts Used

- Lists
- Dictionaries
- List Comprehension
- Conditional Expressions
- Filtering
- Functions
- Loops

---

## 💡 Example

A List Comprehension can filter employees based on salary:

```python
high_salary = [
    employee for employee in employees
    if employee["salary"] > 50000
]