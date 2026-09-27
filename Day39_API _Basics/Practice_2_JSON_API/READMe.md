
---

# 📦 Practice 2 — JSON API

Create:

`Day_39_API_Basics/Practice_2_JSON_API/README.md`

```markdown
# 📦 Practice 2 — JSON API

## 📌 Overview

This practice project focuses on working with **JSON data received from an API**.

The program sends a request to an API, receives the response, converts the JSON response into Python data, and extracts useful information.

This practice connects the concepts learned earlier in **Day 32 — JSON Handling** with the new concept of APIs.

---

## 🎯 Objectives

The main objectives of this practice are:

- Understand JSON responses from APIs.
- Learn how APIs commonly return structured data.
- Use `response.json()`.
- Convert JSON data into Python objects.
- Access values from dictionaries.
- Work with nested API data.
- Display selected information from an API response.

---

## 🛠️ Technologies Used

- Python
- `requests` library
- JSON
- REST API

---

## 🔑 Concepts Learned

### 1. JSON API Response

Many APIs return data in JSON format.

Example:

```json
{
    "name": "Python",
    "version": "3.14",
    "type": "Programming Language"
}