# Contact Search & Duplicate Finder

A practical Python command-line utility designed to search through a contact database and instantly identify duplicate entries. 

## 🚀 Features
* **Partial Matching:** Search contacts instantly by name, email, or career using a minimum of 4 characters.
* **Smart Duplicate Detection:** Uses Python `sets` to automatically flag if a searched contact has duplicate profiles in the system.

## 🧠 What I Learned From This Project
* Implemented nested loops and conditional tracking to isolate matching data.
* Mastered a tricky loop-state bug regarding data persistence across multiple user searches.
* Used Python's any() function to removed an inner nested for loop for cleaner, easier-to-read syntax

## 🛠️ How to Run
1. Make sure you have Python installed.
2. Run the script in your terminal:
   ```bash
   python main.py
   ```
