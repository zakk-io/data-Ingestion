# 📂 PDF & DOCX to Markdown Converter

A simple Python script that converts all **PDF** and **DOCX** files inside a folder into clean **Markdown (.md)** files.

Built using **Docling**.

---

## 🚀 Why This Project?

When building:

* RAG systems
* AI chatbots
* Q&A assistants
* Knowledge base search systems

You first need clean, structured text.

PDF files are layout-based and messy.
Markdown is clean and structured.

This script automates:

```
Folder with PDFs/DOCX → Clean Markdown files
```

Perfect for the data ingestion phase of AI pipelines.

---

## 📦 Features

✅ Converts all `.pdf` and `.docx` files
✅ Skips unsupported file types
✅ Creates output folder automatically
✅ Keeps original filenames
✅ Handles errors per file
✅ Simple and beginner-friendly

---

## 🛠 Requirements

* Python 3.10+
* Virtual environment recommended

Install dependency:

```bash
pip install docling
```

---

## 📁 Project Structure

Example structure:

```
project/
│
├── script.py
├── input_docs/
│   ├── file1.pdf
│   ├── report.docx
│   └── notes.txt
```

After running:

```
project/
│
├── markdown_output/
│   ├── file1.md
│   ├── report.md
│
├── input_docs/
└── script.py
```

`.txt` files are skipped automatically.

---

## ▶️ How to Use

### 1️⃣ Run the Script

```bash
python main.py
```

### 2️⃣ Provide Folder Paths

You will be prompted:

```
Enter input folder path:
Enter output folder path:
```

Example:

```
Enter input folder path: input_docs
Enter output folder path: markdown_output
```

---

## 🔄 What Happens Internally

For each supported file:

1. Reads PDF or DOCX
2. Converts to structured document
3. Exports content as Markdown
4. Saves as `.md` file in output folder

---

## 📌 Supported File Types

* `.pdf`
* `.docx`

---

## 🧠 Use Case in AI / RAG Systems

This script helps in:

```
Document → Markdown → Cleaning → Chunking → Embeddings → Vector DB
```

Markdown preserves:

* Headings
* Sections
* Lists
* Structure

Which improves retrieval quality in RAG systems.

---

## ⚠️ Notes

* If input folder does not exist → script exits safely
* If a file fails → script continues with other files
* Output folder is created automatically if missing

---

## 🔮 Future Improvements (Optional)

You can extend this script to:

* Process subfolders recursively
* Add chunking logic
* Export JSON with metadata
* Add CLI arguments
* Add logging
* Add token statistics

