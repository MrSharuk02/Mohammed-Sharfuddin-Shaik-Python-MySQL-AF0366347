import mysql.connector
from faker import Faker
import random

# Initialize Faker instance
fake = Faker()

# Function to connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sharfoddin@28",
        database="hotelmanagementsystem"
    )

# Function to insert fake customer data into the 'customers' table
def insert_customers(n):
    conn = connect_to_db()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    used_emails = set()  # Set to store used emails and ensure uniqueness
    
    for _ in range(n):
        first_name = fake.first_name()  # Generate fake first name
        last_name = fake.last_name()  # Generate fake last name
        age = random.randint(18, 75)  # Generate random age between 18 and 75
        gender = random.choice(['Male', 'Female'])  # Randomly choose gender
        email = fake.email()  # Generate fake email
        
        # Ensure unique email
        while email in used_emails:
            email = fake.email()
        used_emails.add(email)
        
        phone = fake.phone_number()  # Generate fake phone number
        if len(phone) > 15:  # Ensure phone number fits in the database field
            phone = phone[:15]
        address = fake.address().replace("\n", ", ")  # Generate fake address
        
        # SQL query to insert customer data
        query = "INSERT INTO customers (first_name, last_name, age, gender, email, phone, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, age, gender, email, phone, address))
    
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection

# Function to insert fake room data into the 'rooms' table
def insert_rooms(n):
    conn = connect_to_db()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    room_types = ['Single', 'Double', 'Suite', 'Deluxe']  # List of room types
    used_room_numbers = set()  # Set to store used room numbers and ensure uniqueness
    
    for _ in range(n):
        room_number = fake.bothify(text='###')  # Generate fake room number
        
        # Ensure unique room number
        while room_number in used_room_numbers:
            room_number = fake.bothify(text='###')
        used_room_numbers.add(room_number)
        
        room_type = random.choice(room_types)  # Randomly choose room type
        capacity = random.randint(1, 4)  # Generate random capacity between 1 and 4
        price_per_night = round(random.uniform(50.0, 500.0), 2)  # Generate random price per night
        status = random.choice(['Available', 'Booked', 'Maintenance'])  # Randomly choose status
        
        # SQL query to insert room data
        query = "INSERT INTO rooms (room_number, room_type, capacity, price_per_night, status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (room_number, room_type, capacity, price_per_night, status))
    
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection

# Function to insert fake staff data into the 'staff' table
def insert_staff(n):
    conn = connect_to_db()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    positions = ['Manager', 'Receptionist', 'Housekeeping', 'Chef']  # List of staff positions
    
    for _ in range(n):
        first_name = fake.first_name()  # Generate fake first name
        last_name = fake.last_name()  # Generate fake last name
        age = random.randint(18, 65)  # Generate random age between 18 and 65
        gender = random.choice(['Male', 'Female'])  # Randomly choose gender
        position = random.choice(positions)  # Randomly choose staff position
        hire_date = fake.date_between(start_date='-3y', end_date='today')  # Generate random hire date within the last 3 years
        salary = round(random.uniform(15000.0, 80000.0), 2)  # Generate random salary
        
        # SQL query to insert staff data
        query = "INSERT INTO staff (first_name, last_name, age, gender, position, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, age, gender, position, hire_date, salary))
    
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection

# Function to insert fake service data into the 'services' table
def insert_services(n):
    conn = connect_to_db()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    service_names = ['Spa', 'Gym', 'Breakfast', 'Airport Shuttle']  # List of service names
    
    for _ in range(n):
        service_name = random.choice(service_names)  # Randomly choose service name
        description = fake.sentence(nb_words=10)  # Generate fake service description
        price = round(random.uniform(50.0, 1000.0), 2)  # Generate random service price
        service_status = random.choice(['Available', 'Unavailable'])  # Randomly choose service status
        
        # SQL query to insert service data
        query = "INSERT INTO services (service_name, description, price, service_status) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (service_name, description, price, service_status))
    
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection

# Function to insert fake booking data into the 'bookings' table
def insert_bookings(n):
    conn = connect_to_db()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    
    for _ in range(n):
        customer_id = random.randint(1, 500)  # Generate random customer ID
        room_id = random.randint(1, 500)  # Generate random room ID
        staff_id = random.randint(1, 500)  # Generate random staff ID
        check_in_date = fake.date_between(start_date='-1y', end_date='today')  # Generate random check-in date within the last year
        check_out_date = fake.date_between(start_date=check_in_date, end_date='+15d')  # Generate random check-out date after check-in date
        total_amount = round(random.uniform(100.0, 5000.0), 2)  # Generate random total amount for booking
        booking_status = random.choice(['Confirmed', 'Cancelled', 'Completed'])  # Randomly choose booking status
        
        # SQL query to insert booking data
        query = "INSERT INTO bookings (customer_id, room_id, staff_id, check_in_date, check_out_date, total_amount, booking_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (customer_id, room_id, staff_id, check_in_date, check_out_date, total_amount, booking_status))
    
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection

# Function to insert fake payment data into the 'payments' table
def insert_payments(n):
    conn = connect_to_db()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    payment_methods = ['Credit Card', 'Debit Card', 'Cash', 'Online']  # List of payment methods
    
    for _ in range(n):
        booking_id = random.randint(1, 500)  # Generate random booking ID
        payment_date = fake.date_between(start_date='-1y', end_date='today')  # Generate random payment date within the last year
        amount = round(random.uniform(100.0, 5000.0), 2)  # Generate random payment amount
        payment_method = random.choice(payment_methods)  # Randomly choose payment method
        payment_status = random.choice(['Pending', 'Completed', 'Failed'])  # Randomly choose payment status
        
        # SQL query to insert payment data
        query = "INSERT INTO payments (booking_id, payment_date, amount, payment_method, payment_status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (booking_id, payment_date, amount, payment_method, payment_status))
    
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection

# Function to insert fake booking service data into the 'booking_services' table
def insert_booking_services(n):
    conn = connect_to_db()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object for executing SQL queries
    
    for _ in range(n):
        booking_id = random.randint(1, 500)  # Generate random booking ID
        service_id = random.randint(1, 500)  # Generate random service ID
        quantity = random.randint(1, 10)  # Generate random quantity of services
        total_price = round(random.uniform(50.0, 500.0), 2) * quantity  # Calculate total price based on quantity
        
        # SQL query to insert booking service data
        query = "INSERT INTO booking_services (booking_id, service_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (booking_id, service_id, quantity, total_price))
    
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection

if __name__ == "__main__":
    insert_customers(500)  # Insert 500 fake customers
    insert_rooms(500)  # Insert 500 fake rooms
    insert_staff(500)  # Insert 500 fake staff members
    insert_services(500)  # Insert 500 fake services
    insert_bookings(500)  # Insert 500 fake bookings
    insert_payments(500)  # Insert 500 fake payments
    insert_booking_services(500)  # Insert 500 fake booking services

