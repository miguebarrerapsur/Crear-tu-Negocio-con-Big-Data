from faker import Faker

def generate_users(n=10):
    fake = Faker('es_ES')
    return [{
        "id": fake.random_int(min=1, max=1000000),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "address": fake.address(),
        "password": fake.password(),
    } for _ in range(n)]

def generate_vehicle(n=10, user_id=0):
    fake = Faker('es_ES')
    vehicle_types = ['Sedán', 'SUV', 'Hatchback', 'Coupé', 'Pickup', 'Monovolumen', 'Furgoneta', 'Descapotable']
    car_brands = ['Seat', 'Renault', 'Peugeot', 'Citroën', 'Volkswagen', 'Toyota', 'Ford', 'Opel', 'Nissan', 'Hyundai']
    
    return [{
        "id": fake.random_int(min=0, max=1000000),
        "type": fake.random_element(elements=vehicle_types),
        "brand": fake.random_element(elements=car_brands),
        "vin": fake.vin(),
        "model": fake.bothify(text='??###', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        "year": fake.random_int(min=2010, max=2024),
        "passengers": fake.random_int(min=2, max=8),
        "plate": fake.license_plate(),
        "maximum_weight": fake.random_int(min=1200, max=3500),
        "user_id": user_id ,
    } for _ in range(n)]

def generate_rentals(n=10, user_id="", vehicle_id=0):
    fake = Faker('es_ES')
    rentals = []
    for _ in range(n):
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = fake.date_between(start_date='today', end_date='+1y')
        rentals.append({
            "id_user": user_id,
            "id_vehicle": vehicle_id,
            "start_date": start_date,
            "end_date": end_date,
            "total_price": round(fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=50.00, max_value=2000.00), 2),
        })
    return rentals

def generate_availability(n=10, vehicle_id=0):
    fake = Faker('es_ES')
    return [{
        "id_vehicle": vehicle_id,
        "start_date": fake.date_between(start_date='-1y', end_date='today'),
        "end_date": fake.date_between(start_date='today', end_date='+1y'),
    } for _ in range(n)]

def generate_sponsoring_companies(n=10):
    fake = Faker('es_ES')
    return [{
        "id": fake.random_int(min=1, max=100000),
        "name": fake.company(),
    } for _ in range(n)]

def generate_users_companies(n=10, company_id=0):
    fake = Faker('es_ES')
    return [{
        "id": fake.random_int(min=1, max=1000000),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "company_id": company_id,
        "password": fake.password(),
    } for _ in range(n)]
