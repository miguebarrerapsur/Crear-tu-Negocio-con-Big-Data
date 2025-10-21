from faker import Faker
import fakers.faker_generator as faker_generator

fake = Faker('es_ES')

print("=== USUARIOS ===")
print(faker_generator.generate_users(5))

print("\n=== VEHÍCULOS ===")
print(faker_generator.generate_vehicle(5))

print("\n=== ALQUILERES ===")
print(faker_generator.generate_rentals(5))

print("\n=== DISPONIBILIDAD ===")
print(faker_generator.generate_availability(5))

print("\n=== EMPRESAS PATROCINADORAS ===")
print(faker_generator.generate_sponsoring_companies(5))

print("\n=== CAMPAÑAS PUBLICITARIAS ===")
print(faker_generator.generate_advertising_campaigns(5))