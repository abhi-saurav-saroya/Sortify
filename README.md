<h1 align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=ffffff&center=true&vCenter=true&width=650&lines=Sortify+-+Smart+File+Organizer"
    alt="Sortify - Smart File Organizer"
  />
</h1>

<p align="center"><i>Turning chaos into order, one file at a time.</i></p>

---

Sortify is a **command-line file organization tool built in Python**, designed to automatically categorize and organize files into dedicated folders based on their file extensions.

The project focuses on **Python fundamentals, file system automation, modular software design, path manipulation, error handling, logging systems, and practical utility development**, all implemented using Python's standard library.

> Note: Sortify is designed as a learning-focused automation project and currently organizes files within a user-specified directory while preserving existing files through automatic duplicate filename handling.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Category-Automation-22c55e?style=for-the-badge" alt="Automation"/>
  <img src="https://img.shields.io/badge/Type-CLI_Tool-f97316?style=for-the-badge" alt="CLI Tool"/>
  <img src="https://img.shields.io/badge/Domain-File_Management-6366f1?style=for-the-badge" alt="File Management"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Logging-Enabled-2563eb?style=for-the-badge" alt="Logging"/>
  <img src="https://img.shields.io/badge/Duplicate_Handling-Supported-7c3aed?style=for-the-badge" alt="Duplicate Handling"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License"/>
</p>

## Features

1. ### Automatic File Organization

   * Categorizes files based on extension
   * Creates category folders automatically
   * Supports multiple file types
   * Handles unknown file types gracefully

2. ### Duplicate File Handling

   * Detects filename conflicts
   * Automatically renames duplicates
   * Preserves existing files
   * Prevents accidental overwrites

3. ### Organization Statistics

   * Displays category-wise file counts
   * Shows total files moved
   * Tracks renamed files
   * Provides organization summary

4. ### Logging System

   * Records organization sessions
   * Logs file movements
   * Logs automatic renaming events
   * Maintains operation history

5. ### User Experience

   * Interactive menu-driven interface
   * Path validation
   * Progress display during organization
   * Clear success and error feedback

## Project Architecture

<p align="center">
  <img src="assets\dir-structure.png" alt="Project Structure" width="500">
</p>

## Log File Example

<p align="center">
  <img src="assets\log-example.png" alt="Sortify Log Example" width="600">
</p>

## Tech Stack

<div align="center">

| Component              | Technology   |
| ---------------------- | ------------ |
| Language               | Python 3     |
| File System Operations | os           |
| File Management        | shutil       |
| Logging                | datetime     |
| Version Control        | Git + GitHub |

</div>

## Build & Run Instructions

### Requirements

* Python 3.10 or higher
* Git (optional, for cloning the repository)

### Clone the Repository

```bash
git clone https://github.com/abhi-saurav-saroya/sortify.git
cd sortify
```

### Run the Application

```bash
python main.py
```

or

```bash
python3 main.py
```

### Usage

1. Launch Sortify.
2. Select **Organize Folder** from the main menu.
3. Enter the path of the folder you want to organize.
4. Wait for the organization process to complete.
5. Review the generated statistics and log history.

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="Footer"/>

<i>Built to learn, designed to automate, engineered one file at a time. 📂</i>

<i>Turning chaos into order, one file at a time.</i>

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

**© 2026 Open Source Project | Sortify - Smart File Organizer | MIT License**

</div>
