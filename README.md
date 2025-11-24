

## 📚 Overview
This project demonstrates practical understanding of core Python concepts through four mini-projects. Each project focuses on real-world applications using **Sets, Dictionaries, Functions, and File Handling**.

---

## 🎯 Concepts Covered
- **Sets** - Managing unique collections of data  
- **Dictionaries** - Key-value pair storage and manipulation  
- **Functions** - Modular and reusable codestructure  
- **File Handling** - Reading from and writing to files  

---

## 📂 Projects Included

### 1️⃣ Project 1: Unique Phone Number Extractor
**Concepts Used:** Set, File Handling, Functions  

**What it does:**  
- Reads a file containing phone numbers (may have duplicates)  
- Extracts only unique phone numbers using a set  
- Displays them in a clean format  

**Example Input File (`phones.txt`):**
9876543210
9123456789
9876543210
8765432109
9123456789
9988776655

**Expected Output:**
Unique Phone Numbers Found:

9876543210

9123456789

8765432109

9988776655
Total Unique Numbers: 4

**Key Learning:** Sets automatically eliminate duplicate values, making them perfect for uniqueness operations.

---

### 2️⃣ Project 2: Book Word Frequency Counter
**Concepts Used:** Dictionary, File Handling, Functions  

**What it does:**  
- Reads text from a book/article file  
- Counts how many times each word appears  
- Displays top 10 most frequent words  

**Example Input File (`book.txt`):**
Python is powerful. Python is versatile.
Learning Python is exciting and Python programming is rewarding.
Python helps build amazing applications.


**Expected Output:**


Word Frequency Analysis:
Python: 5
is: 4
and: 1
powerful: 1
versatile: 1
...


**Key Learning:** Dictionaries excel at counting and frequency analysis tasks.

---

### 3️⃣ Project 3: Library Book Manager
**Concepts Used:** Set, Dictionary, Functions, File Writing  

**What it does:**  
- Manages library books with categories  
- Tracks unique book genres using sets  
- Stores book information with nested dictionaries  
- Saves complete library data to a file  

**Example Data:**


Book: "The Great Gatsby"
Author: F. Scott Fitzgerald
Genre: Fiction
Year: 1925

Book: "1984"
Author: George Orwell
Genre: Fiction
Year: 1949


**Output File (`library.txt`):**


The Great Gatsby: {'Author': 'F. Scott Fitzgerald', 'Genre': 'Fiction', 'Year': 1925}
1984: {'Author': 'George Orwell', 'Genre': 'Fiction', 'Year': 1949}

Available Genres: Fiction, Science, History


**Key Learning:** Combining sets and dictionaries creates powerful data management systems.

---

### 4️⃣ Project 4: Simple Expense Tracker
**Concepts Used:** Dictionary, Functions, File Handling  

**What it does:**  
- Records daily expenses by category  
- Updates expense amounts if category exists  
- Saves all expenses to a file  
- Calculates total spending  

**Example Usage:**


Add Expense:
Category: Food
Amount: 500

Category: Transport
Amount: 200

Category: Food
Amount: 300 (adds to existing)


**Output File (`expenses.txt`):**

Food: 800
Transport: 200
Entertainment: 500

Total Spent: 1500


**Key Learning:** Dictionaries naturally handle updates and aggregations.

---

## 💡 Key Takeaways
- Sets prevent duplicate data automatically  
- Dictionaries map keys to values efficiently  
- Functions make code modular and maintainable  
- File I/O enables data persistence  
- Nested structures organize complex data  

---

## 🚀 How to Run
1. Create input files as shown in examples  
2. Run each Python script  
3. Check output files generated  
4. Modify and experiment with the code  



## 📝 Code Structure
```

project/
│
├── project1_phone_extractor.py
├── project2_word_counter.py
├── project3_library_manager.py
├── project4_expense_tracker.py
│
├── input_files/
│ ├── phones.txt
│ ├── book.txt
│ └── library_data.txt
│
└── output_files/
├── unique_phones.txt
├── word_frequency.txt
├── library.txt
└── expenses.txt

```

## 🎓 Learning Outcomes
By completing this project, I have learned:  
- How to handle duplicate data using sets  
- How to structure data with dictionaries  
- How to write clean, reusable functions  
- How to perform file read/write operations  
- How to combine multiple concepts in practical applications  
- How to organize code in a professional manner  

---

## 👤 Author
**K Premila Singha**  
This project was created as part of Python programming practice to demonstrate understanding of fundamental concepts through practical implementation.

---

## 🔧 Technologies Used
- Python 3.x  
- File I/O Operations  
- Data Structures (Sets, Dictionaries, Lists)

