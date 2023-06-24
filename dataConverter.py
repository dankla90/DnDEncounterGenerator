#Name,Size,Type,Alignment,CR,XP,Arctic,Coastal,Desert,Forest,Grassland,Hill,Mountain,Swamp,Underdark,Underwater,Urban,Other Plane,source
# This is a converter for csvdata for making a dict readable by the encounter program, but expanded to include 
# the enviroment list for more selection. 
import csv

monster_data = {}

# Parse the monster data and populate the dictionary

with open('copy4.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Skip header row
    for row in reader:
        name = row[0]
        name = name.strip("'’,/\n")
        name = name.replace("'","\\'").strip("\\'")
        size = row[1]
        monster_type = row[2]
        alignment = row[3]
        cr = row[4]
        xps = row[5]
        xp = int(xps)
        arctic = row[6]
        coastal = row[7]
        desert = row[8]
        forest = row[9]
        grassland = row[10]
        hill = row[11]
        mountain = row[12]
        swamp = row[13]
        underdark = row[14]
        underwater = row[15]
        urban = row[16]
        other_plane = row[17]
        source = row[18]
        
        environment = [arctic, coastal, desert, forest, grassland, hill, mountain, swamp, underdark, underwater, urban, other_plane]
        attributes = [size, monster_type, alignment, cr, xp, source]
        
        # Update the monster_data dictionary with the new entry
        monster_data[f"'{name}'"] = attributes + [environment]

# Save the monster data dictionary to a new document

output_file = 'monster_data.txt'

with open(output_file, 'w') as file:
    for key, value in monster_data.items():
        file.write(f"{key}: {value}\n")

print(f"Monster data saved to {output_file}")