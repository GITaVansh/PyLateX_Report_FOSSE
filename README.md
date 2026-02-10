# 🏗️ PyLaTeX-Beam-Analysis-Automator

## 📖 Project Overview
This project is a Python-based automation tool designed to generate comprehensive, submission-ready engineering reports for **Simply Supported Beams**. 

By processing loading data from Excel, the script performs structural calculations and leverages **PyLaTeX** to typeset a professional PDF. Unlike standard reporting tools, this script generates **native LaTeX vector graphics**, ensuring that diagrams remain perfectly sharp at any scale.

---

## ✨ Features
* **✅ Automated Data Processing:** Reads point loads and beam geometry from Excel using `pandas`.
* **✅ Native LaTeX Tables:** Reconstructs force data into searchable, professional `tabular` environments.
* **✅ TikZ/pgfplots Vector Diagrams:** Programmatically generates **Shear Force Diagrams (SFD)** and **Bending Moment Diagrams (BMD)** using TikZ—no low-resolution images.
* **✅ Structured Documentation:** Includes a Title Page, Table of Contents, Introduction with embedded beam diagrams, and a detailed Analysis section.
* **✅ Professional Aesthetics:** Mimics industrial software outputs (like Midas) with shaded contour plots and axis legends.



[Image of a Shear Force and Bending Moment Diagram for a simply supported beam]


---

## 🛠 Technical Stack
* **Language:** Python 3.10+
* **Data Handling:** `pandas`, `openpyxl`
* **Typesetting Engine:** `PyLaTeX`
* **Graphics Engine:** `TikZ` / `pgfplots`
* **LaTeX Backend:** TeX Live, MiKTeX, or MacTeX (required for compilation)

---

## 🚀 Quick Start

### 1. Prerequisites
You must have a LaTeX distribution installed on your machine:
* **Windows:** [MiKTeX](https://miktex.org/)
* **Linux/Mac:** [TeX Live](https://www.tug.org/texlive/)

### 2. Installation
Clone the repository and install the Python dependencies:
```bash
git clone [https://github.com/GitaVansh/PyLaTeX-Beam-Analysis-Automator.git](https://github.com/YOUR_USERNAME/PyLaTeX-Beam-Analysis-Automator.git)
cd PyLaTeX-Beam-Analysis-Automator
pip install -r requirements.txt
