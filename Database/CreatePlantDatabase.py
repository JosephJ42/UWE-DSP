# == CreatePlantDatabase ==
# Creates the plant information and care database to be used in the IdentiFlora application.

import sqlite3

# Creates database
connection = sqlite3.connect("plantInformation.db")
cursor = connection.cursor()

# Created the plant information table in the database
createPlantInfoCommand = """CREATE TABLE IF NOT EXISTS
plantInfo(plant_name TEXT PRIMARY KEY, plant_description TEXT, watering TEXT, light_levels TEXT, 
ideal_temperature TEXT, ideal_humidity TEXT, feeding_and_fertilizing TEXT, special_information TEXT )"""

cursor.execute(createPlantInfoCommand)

# Add plant data to plantInfo table 
cursor.execute("INSERT INTO plantInfo VALUES ('aglonema', 'Aglaonema is easily recognizable by its green camouflage patterns on the upper sides of the leaves', 'Every 7 to 9 days', 'Bright but indirect light', '21°C to 29°C', 'Prefers humid conditions', 'Fertilize once or twice yearly using a water-soluble houseplant fertilize', 'none')")
cursor.execute("INSERT INTO plantInfo VALUES ('calathea', 'Calathea plants are part of the family of plants known as Marantaceae which is a species of flowering plants from tropical areas such as Africa. They are famous for their wide green colorful leaves.' , 'Every 7 days', 'Medium to slow levels of indirect sunlight', '18°C - 30°C', 'Prefers humid conditions' , 'Small amounts every four weeks', 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('janda_bolong', 'Janda Bolong aka Monstera adansonii is known for its beautiful heart-shaped leaves. The leaves contain large oval-shaped perforations which lead to its common name of swiss cheese plant', 'One to two times a week', 'Bright but indirect light', '18°C - 30°C', 'Prefers humid conditions', 'Fertilize at least once every two weeks', 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('keladi', 'Caladiums are tropical perennials with colorful heart-shaped leaves native to tropical forests in South and Central America.' , 'Every 7 days', 'Bright but indirect light' , '21°C - 30°C' , 'Prefers humid conditions', 'Fertilize heavily every 4 to 6 weeks' , 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('aloe_vera', 'Aloe vera is a herb with succulent leaves that are arranged in a rosette. The leaves are grey to green and sometimes have white spots on their surfaces. They have sharp, pinkish spines along their edges.' , 'Every 3 weeks', 'Bright but indirect light' , '13°C to 27°C' , 'Happy in any levels of humidity', ' Fertilize sparingly, no more than once a year' , 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('chlorophytum_comosum', 'Chlorophytum comosum, usually called spider plants are an evergreen, perennial plant with tuberous roots and tuft appearance.' , 'Every 2-3 days', 'Bright but indirect light' , '18-24°C ' , 'Prefers humid conditions, but can happily handle any level of humidity', 'Fertilize every 2 to 4 weeks' , 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('crassula_ovata', 'Commonly known as the jade plant or money plant, Crassula ovata is a large, much-branched, hairless and floriferous shrub from southern Africa.' , 'Once every 2 to 3 weeks', 'Young plants should be kept in bright, indirect sunlight; large, well-established jade plants can handle more direct sunlight.' , '18°C - 23°C' , 'Prefers low humidity', 'Fertilize once every six months.' , 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('dracaena_warneckii', 'Dracaena Warneckii is a dracaena family native of tropical Africa. This dracaena species is known for its sword-like green leaves that are rigid and sharply pointed' , 'every 5 to 7 days', 'Medium to bright light situation' , '16° to 27°C' , 'Prefers average levels of humidity', 'Feed once or twice a year' , 'Note: these plants can be toxic if directly or indirectly consumed ie accidental consuption of sap after handling the plant')")
cursor.execute("INSERT INTO plantInfo VALUES ('dracaena_angolensi', 'Dracaena Angolensis also known as the cylindrical snake plant, is a succulent plant native to Angola that have  striped, elongate, smooth, greenish-gray subcylindrical leaves.' , 'every 3 weeks.', 'Prefers full direct sunlight' , '18°C - 27°C' , 'Prefers average levels of humidity', 'Fertilize sparingly, no more than once a year' , 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('schefflera', 'Schefflera, also called umbrella trees, are relatively large plants with long, shiny, oval green leaves that droop gracefully from a central stalk, resembling an umbrella' , 'Every 7-14 days', 'Bright, indirect light' , '13°C to 24°C' , 'Happy in any levels of humidity', 'Fertilize once a month' , 'N/A')")
cursor.execute("INSERT INTO plantInfo VALUES ('fittonia_albivenis', 'Fittonia Albivenis, also called nerve plants or mosaic plants, are a creeping evergreen perennial with accented veins of white to deep pink and a short fuzz covering its stems.' , 'Every 4 to 7 days', 'low to medium light levels' , '15°C - 26°C' , 'Prefers humid conditions', 'Fertilize every 1-2 months' , 'N/a')")

# Check all data has been inputted correctly
cursor.execute ("SELECT * From plantInfo")
results = cursor.fetchall()
print(results)
connection.commit()
