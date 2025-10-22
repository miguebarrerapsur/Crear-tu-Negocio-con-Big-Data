import mysql.connector

def truncate_database(cursor):
    truncate_tables = """
    TRUNCATE TABLE users;
    TRUNCATE TABLE vehicles;
    TRUNCATE TABLE availability;
    TRUNCATE TABLE companies;
    TRUNCATE TABLE userscompanies;
    TRUNCATE TABLE rentals;
    """
    cursor.execute(truncate_tables)


def create_mysql_tables(cursor):
    crear_tabla_users = """
    CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        email VARCHAR(100),
        password VARCHAR(100),
        address VARCHAR(100)
    )
    """
    cursor.execute(crear_tabla_users)

    crear_tabla_companies = """
    CREATE TABLE IF NOT EXISTS companies (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        password VARCHAR(100)
    )
    """
    cursor.execute(crear_tabla_companies)

    crear_tabla_users_companies = """
    CREATE TABLE IF NOT EXISTS userscompanies (
        id INT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        email VARCHAR(100),
        password VARCHAR(100),
        company_id INT,
        FOREIGN KEY (company_id) REFERENCES companies(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )
    """
    cursor.execute(crear_tabla_users_companies)

    crear_tabla_vehicles = """
    CREATE TABLE IF NOT EXISTS vehicles (
        id INT PRIMARY KEY,
        type VARCHAR(100),
        brand VARCHAR(100),
        vin VARCHAR(100),
        model VARCHAR(100),
        year VARCHAR(100),
        passengers VARCHAR(100),
        plate VARCHAR(100),
        maximum_weight VARCHAR(100),
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
    """
    cursor.execute(crear_tabla_vehicles)

    crear_tabla_vehicle_availability = """
    CREATE TABLE IF NOT EXISTS availability (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_vehicle INT,
        start_date DATE,
        end_date DATE,
        FOREIGN KEY (id_vehicle) REFERENCES vehicles(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )
    """
    cursor.execute(crear_tabla_vehicle_availability)

    crear_tabla_rentals = """
    CREATE TABLE IF NOT EXISTS rentals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_user INT,
        id_vehicle INT,
        start_date DATE,
        end_date DATE,
        total_price DECIMAL(10, 2),
        FOREIGN KEY (id_user) REFERENCES users(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
        FOREIGN KEY (id_vehicle) REFERENCES vehicles(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
    """
    cursor.execute(crear_tabla_rentals)