import mysql.connector

def insert_user(cursor, user):
    cursor.execute(
        "INSERT INTO users (id, first_name, last_name, email, password, address) VALUES (%s, %s, %s, %s, %s, %s)",
        (user['id'],user['first_name'], user['last_name'], user['email'], user['password'], user['address'])
    )

def insert_vehicle(cursor, vehicle):
    cursor.execute(
        "INSERT INTO vehicles (id, type, brand, vin, model, year, passengers, plate, maximum_weight,user_id) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (vehicle['id'], vehicle['type'], vehicle['brand'], vehicle['vin'], vehicle['model'], vehicle['year'], vehicle['passengers'], vehicle['plate'], vehicle['maximum_weight'], vehicle['user_id'])
    )

def insert_availability(cursor, availability):
    cursor.execute(
        "INSERT INTO availability (id_vehicle, start_date, end_date) VALUES (%s, %s, %s)",
        (availability['id_vehicle'], availability['start_date'], availability['end_date'])
    )

def insert_rental(cursor, rental):
    cursor.execute(
        "INSERT INTO rentals (id_user, id_vehicle, start_date, end_date, total_price) VALUES (%s, %s, %s, %s, %s)",
        (rental['id_user'], rental['id_vehicle'], rental['start_date'], rental['end_date'], rental['total_price'])
    )

def insert_company(cursor, company):
    cursor.execute(
        "INSERT INTO companies (id, name) VALUES (%s, %s)",
        (company["id"], company['name'],)
    )

def insert_user_companies(cursor, user):
    cursor.execute(
        "INSERT INTO userscompanies (id, first_name, last_name, email, password, company_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (user['id'],user['first_name'], user['last_name'], user['email'], user['password'], user['company_id'])
    )
