import mysql.connector

# Step 1: Connection Details
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # <-- change if needed
        password="Hari@123",  # <-- change this
        database="blog_db"
    )

# Step 2: Menu
def main():
    while True:
        print("\n=== Blog Manager ===")
        print("1. Create Post")
        print("2. View All Post Titles")
        print("3. View Post Content by Title")
        print("4. Search Posts by Tag")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            create_post()
        elif choice == '2':
            view_posts()
        elif choice == '3':
            view_post_by_title()
        elif choice == '4':
            search_by_tag()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


# Step 3: Create Post
def create_post():
    title = input("Enter title: ")
    content = input("Enter content: ")
    tags = input("Enter comma-separated tags: ").split(',')

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    post_id = cursor.lastrowid

    for tag in tags:
        tag = tag.strip()
        cursor.execute("SELECT id FROM tags WHERE name=%s", (tag,))
        result = cursor.fetchone()
        if result:
            tag_id = result[0]
        else:
            cursor.execute("INSERT INTO tags (name) VALUES (%s)", (tag,))
            tag_id = cursor.lastrowid

        cursor.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (%s, %s)", (post_id, tag_id))

    conn.commit()
    cursor.close()
    conn.close()
    print("Post added.")

# Step 4: View Posts
def view_posts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM posts")
    rows = cursor.fetchall()
    print("\nPost Titles:")
    for (title,) in rows:
        print(f"- {title}")
    cursor.close()
    conn.close()

def view_post_by_title():
    title = input("Enter post title: ")
    
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT content FROM posts WHERE title = %s", (title,))
    result = cursor.fetchone()
    
    if result:
        print(f"\n--- Content ---\n{result[0]}")
    else:
        print("Post not found.")
    
    cursor.close()
    conn.close()

def search_by_tag():
    tag = input("Enter tag to search: ")

    conn = connect_db()
    cursor = conn.cursor()

    query = """
        SELECT p.title 
        FROM posts p
        JOIN post_tags pt ON p.id = pt.post_id
        JOIN tags t ON pt.tag_id = t.id
        WHERE t.name = %s
    """
    cursor.execute(query, (tag,))
    results = cursor.fetchall()

    if results:
        print(f"\nPosts with tag '{tag}':")
        for (title,) in results:
            print(f"- {title}")
    else:
        print("No posts found with that tag.")

    cursor.close()
    conn.close()



if __name__ == "__main__":
    main()
