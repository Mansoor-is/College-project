import mysql.connector
import csv

try:
    # Open the CSV file
    with open("data.csv", "r") as csv_file:
        # Read the CSV file with tab delimiter
        reader = csv.reader(csv_file, delimiter='\t')
        
        # Skip the header row (first row)
        next(reader)
        
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="mansoorkhan",
            database="school"
        )
        
        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Process each row in the CSV file
        for row in reader:
            # Print the raw row for debugging
            print(f"Processing row: {row}")

            # Clean up extra spaces from each field
            row = [field.strip() for field in row]

            # Ensure the row has at least two columns
            if len(row) < 2:
                print(f"Skipping malformed row: {row}")
                continue

            # Get the ID and name from the row
            id = row[0]
            name = row[1]

            # Check if the ID already exists in the database
            cursor.execute("SELECT COUNT(*) FROM student WHERE id = %s", (id,))
            if cursor.fetchone()[0] > 0:
                print(f"ID {id} already exists. Skipping...")
                continue

            # Insert the row into the database
            cursor.execute("INSERT INTO student (id, name) VALUES (%s, %s)", (id, name))

        # Commit the changes to the database
        conn.commit()

        print("Data inserted successfully.")

except mysql.connector.Error as err:
    print("MySQL Error:", err)
except Exception as e:
    print("Error:", e)
finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
