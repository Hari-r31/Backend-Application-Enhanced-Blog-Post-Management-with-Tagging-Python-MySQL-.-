# 📝 Blog CLI Manager (Python + MySQL)

A simple command-line blog post manager built with **Python** and **MySQL**.  
It allows you to create posts with tags, view post titles, read post content, and search posts by tag — all from your terminal.

---

## 🚀 Features

- ✅ Create blog posts with comma-separated tags
- ✅ View all post titles
- ✅ Read full content of a post by title
- ✅ Search posts by a specific tag

---

## 🧰 Technologies Used

- Python 3.x
- MySQL
- mysql-connector-python

---

## 📦 Installation

### 1. Clone or Download the Repo

```bash
git clone https://github.com/yourusername/blog-cli-manager.git
cd blog-cli-manager
```

### 2. Install Required Python Packages

```bash
pip install mysql-connector-python
```

---

## 🗃️ MySQL Database Setup

### Step 1: Log in to MySQL

```bash
mysql -u root -p
```

### Step 2: Run the SQL below

```sql
CREATE DATABASE blog_db;
USE blog_db;

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE tags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE post_tags (
    post_id INT,
    tag_id INT,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);
```

---

## ⚙️ Configuration

In `blog_cli.py`, update the database credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_mysql_password',  # <-- change this
    'database': 'blog_db'
}
```

---

## 🏃 Run the App

```bash
python blog_cli.py
```

You’ll see a menu like:

```
=== Blog Manager ===
1. Create Post
2. View All Post Titles
3. View Post Content by Title
4. Search Posts by Tag
5. Exit
```

---

## ✍️ Example Usage

- Create a post: `"My First Post"` with tags like `python, learning`
- View all posts
- Read the content by entering the title
- Search by tag like `"python"`

---

## 📌 Future Ideas

- Add update/delete post feature
- Add user authentication
- Export posts to markdown or PDF
- Convert to a Flask-based web app

---

## 📖 License

This project is for educational purposes and personal use. No license is applied yet.

---

## 🙌 Author

**Hari Sai Kumar Thatholu**  
Learning Python + MySQL CLI Dev

