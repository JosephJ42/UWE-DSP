import sqlite3

from matplotlib.pyplot import connect

#

connection = sqlite3.connect("plantInformation.db")

cursor = connection.cursor()

createTable1Command = """CREATE TABLE IF NOT EXISTS
plantInfo(plant_name TEXT PRIMARY KEY, plant_description TEXT, watering TEXT, light_levels TEXT, ideal_temperature TEXT, ideal_humidity TEXT, feeding_and_fertilizing TEXT, special_information TEXT )"""

cursor.execute(createTable1Command)

# Add plant data

cursor.execute("INSERT INTO plantInfo VALUES ('aglonema', 'Aglaonema is easily recognizable by its green camouflage patterns on the upper sides of the leaves', 'Every 7 to 9 days', 'Bright but indirect light', '21 C to 29 C', 'Prefers humid conditions', 'Fertilize once or twice yearly using a water-soluble houseplant fertilize', 'none')")
cursor.execute("INSERT INTO plantInfo VALUES ('calathea', 'Calathea plants are part of the family of plants known as Marantaceae which is a species of flowering plants from tropical areas such as Africa. They are famous for their wide green colorful leaves.' , 'Every 7 days', 'Medium to slow levels of indirect sunlight', '18 C - 30 C', 'Prefers humid conditions' , 'Small amounts every four weeks', 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('janda_bolong', 'Janda Bolong aka Monstera adansonii is known for its beautiful heart-shaped leaves. The leaves contain large oval-shaped perforations which lead to its common name of swiss cheese plant', 'One to two times a week', 'Bright but indirect light', '18 C - 30 C', 'Prefers humid conditions', 'Fertilize at least once every two weeks', 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('keladi', 'Caladiums are tropical perennials with colorful heart-shaped leaves native to tropical forests in South and Central America.' , 'Every 7 days', 'Bright but indirect light' , '21 C - 30 C' , 'Prefers humid conditions', 'Fertilize heavily every 4 to 6 weeks' , 'N/A')")


#

cursor.execute ("SELECT * From plantInfo")

results = cursor.fetchall()

print(results)

connection.commit()




