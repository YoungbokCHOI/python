import sqlite3
import xml.etree.ElementTree as ET

# Connect to the SQLite database
conn = sqlite3.connect('..\\DB\\YBDB.db')
c = conn.cursor()

# Execute the SQL query to fetch the data from the EMP table
c.execute("SELECT emp_no, emp_name, emp_age FROM EMP")
rows = c.fetchall()

# Create the root element for the XML
root = ET.Element("employees")

# Iterate over each row and add it to the XML
for row in rows:
    # Create an employee element
    employee = ET.SubElement(root, "employee")

    # Add emp_no, emp_name, and job as child elements of the employee element
    ET.SubElement(employee, "emp_no").text = str(row[0])
    ET.SubElement(employee, "emp_name").text = row[1]
    ET.SubElement(employee, "emp_age").text = row[2]

# Create an ElementTree object and write the XML data to a file
tree = ET.ElementTree(root)
tree.write(".\\emp_20240408.xml")
