import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="Hospital_Lec"
    )

inp1="INSERT INTO Patient VALUES (1001, 'patient1', '12345', '1100000000001', 'Ms.', 'Seulgi', 'Kang', 'Female', '1994-02-10'," \
    "27, 'Seoul-teukbyeolsi, Jongno-gu, Sajik-ro-3-gil 23, 102-dong 304-ho, Hong Gildong gwiha 30174', '0100000001', NULL);"
inp2="INSERT INTO Patient VALUES (1002, 'patient2', '12345', '1100000000002', 'Mr.', 'Jake', 'Sim', 'Male', '2002-11-15'," \
    "18, '147-8, Gwanghwal-myeon, Gimje-si, Jeollabuk-do, 25481', '0100000002', 'Heart disease');"
ins1="INSERT INTO Staff VALUES (2001, 'staff1', '12345', 'Mr.', 'Sam', 'Travis', 'Radionuclide tests', 'Admin');"
ins2="INSERT INTO Staff VALUES (2002, 'staff2', '12345', 'Ms.', 'Jessica', 'Ellis', 'ICU', 'Nurse');"
ind1="INSERT INTO Doctor VALUES (3001, 'doctor1', '12345', 'Dr.', 'Payu', 'Sugunya', 'Brain surgery', 'Neurologists');"
ind2="INSERT INTO Doctor VALUES (3002, 'doctor2', '12345', 'Dr.', 'Paryahchet', 'Piengsirinkun', 'Child psychology', 'Psychiatrist');"
inl1="INSERT INTO Laboratory VALUES (91001, 'X-Ray room', 'X-Ray', 'Eladis Rozer 1', '5th', '352', 'Unavaliable');"
inl2="INSERT INTO Laboratory VALUES (91002, 'Blood testing room', 'Blood test', 'Eladis Rozer 2', '3rd', '210', 'Avaliable');"
inl3="INSERT INTO Laboratory VALUES (91003, 'Urea testing room', 'Urea test', 'Eladis Rozer 2', '3rd', '211', 'Avaliable');"
inm1="INSERT INTO Medicine VALUES (101, 'Acetaminophen', 'Tablet', 'a maximum daily dose for adults of 3 g, " \
     "with no more than 650 mg every 6 hours, as needed.', 'MedLine Plus Drug');"
inm2="INSERT INTO Medicine VALUES (102, 'Aspirin', 'Tablet', 'a daily dose between 75 mg and 325 mg'," \
     "'MedLine Plus Drug');"
inm3="INSERT INTO Medicine VALUES (103, 'Pseudoephedrine', 'Tablet', '30 to 60 mg orally every 4 to 6 hours as needed'," \
     "'MedLine Plus Drug');"
inpr1="INSERT INTO Product VALUES (201, 'Antiseptic', 'Agent', 'preventing infections on the skin, particularly for cuts," \
     "scrapes, or minor burns.', 'MedLine Plus Drug');"
inpr2="INSERT INTO Product VALUES (202, 'Bandage', 'Healer', 'dressing where a wound is present', 'MedLine Plus Drug');"
inpr3="INSERT INTO Product VALUES (203, 'Syringe', 'Injector', 'inject fluid into, or withdraw fluid from, the body'," \
     "'MedLine Plus Drug');"

cursor=connection.cursor()

cursor.execute(inp1)
cursor.execute(inp2)
cursor.execute(ins1)
cursor.execute(ins2)
cursor.execute(ind1)
cursor.execute(ind2)
cursor.execute(inl1)
cursor.execute(inl2)
cursor.execute(inl3)
cursor.execute(inm1)
cursor.execute(inm2)
cursor.execute(inm3)
cursor.execute(inpr1)
cursor.execute(inpr2)
cursor.execute(inpr3)

connection.commit()