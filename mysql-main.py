import mysql.connector
import fakers.faker_generator as faker_generator
import docker_databases.mysql.create_mysql as create_mysql
import docker_databases.mysql.insert_mysql as insert_mysql

config = {
    'user': 'bigdata_user',
    'password': 'bigdata_password',
    'host': '127.0.0.1',
    'database': 'bigdata_db',
    'port': 3307
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

#create_mysql.truncate_database(cursor)
create_mysql.create_mysql_tables(cursor)

users = faker_generator.generate_users(500)
for user in users:
    insert_mysql.insert_user(cursor, user)
    vehicles = faker_generator.generate_vehicle(2, user['id'])
    for vehicle in vehicles:
        insert_mysql.insert_vehicle(cursor, vehicle)
        availabilities = faker_generator.generate_availability(3, vehicle['id'])
        for availability in availabilities:
            insert_mysql.insert_availability(cursor, availability)
        rentals = faker_generator.generate_rentals(5, user['id'], vehicle['id'])
        for rental in rentals:
            insert_mysql.insert_rental(cursor, rental)

companies = faker_generator.generate_sponsoring_companies(100)
for company in companies:
    insert_mysql.insert_company(cursor, company)
    users_companies = faker_generator.generate_users_companies(5, company['id'])
    for user_company in users_companies:
        insert_mysql.insert_user_companies(cursor, user_company)

conn.commit()
cursor.close()
conn.close()