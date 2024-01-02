import understand

db = understand.open("/home/mehran/Desktop/test/src/src.udb")

print ("\n")

for class_entity in db.ents("class"):
    print(class_entity.longname())

res = len(db.ents("class"))
print (f"\n\n******* Number of Classes: {res} *******\n\n")