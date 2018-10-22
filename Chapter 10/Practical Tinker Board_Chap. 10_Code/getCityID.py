import pyowm
 
owm = pyowm.OWM('api_key')
 
registry = owm.city_id_registry()
 
results = registry.ids_for('city_name')
 
print(results)
