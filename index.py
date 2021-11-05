import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="Hospital_Lec"
    )

#db="CREATE database Hospital_Lec;"

tb1="CREATE TABLE Patient (PatientID int(10) PRIMARY KEY, PatientUser varchar(30), PatientPasswd varchar(30), PatientPID " \
    "varchar(20), PatientTitle varchar(10), PatientFName varchar(50), PatientLName varchar(50), PatientSex varchar(10)," \
    "PatientDOB date, PatientAge int(3), PatientAddress text(100), PatientPhone varchar(10), PatientDisease varchar(30));"
tb2="CREATE TABLE Staff (StaffID int(10) PRIMARY KEY, StaffUser varchar(30), StaffPasswd varchar(30)," \
    "StaffTitle varchar(10), StaffFName varchar(50), StaffLName varchar(50), StaffWard varchar(20), StaffType varchar(50));"
tb3="CREATE TABLE Doctor (DoctorID int(10) PRIMARY KEY, DoctorUser varchar(30), DoctorPasswd varchar(30)," \
    "DoctorTitle varchar(10), DoctorFName varchar(50), DoctorLName varchar(50), DoctorWard varchar(50), DoctorExpert varchar(50));"
tb4="CREATE TABLE Laboratory (LabID int(10) PRIMARY KEY, LabName varchar(50), LabType varchar(45), LabBuilding varchar(50)," \
    "LabFloor varchar(4), LabRoomNo varchar(6), LabStatus varchar(12));"
tb5="CREATE TABLE Laboratory_Reservation (LabResNo int(10) PRIMARY KEY, LabID int(10), StaffID int(10)," \
    "PatientID int(10), AppointmentID int(10), LabResDate date, LabResTime time);"
tb6="CREATE TABLE Appointment (AppointmentID int(10) PRIMARY KEY, RequestID int(10), StaffID int(10), DoctorID int(10)," \
    "PatientID int(10), AppointmentDate date, AppointmentTime time, AppointmentType varchar(50));"
tb7="CREATE TABLE Prescription (PrescriptionNo int(8) PRIMARY KEY, DoctorID int(10), StaffID int(10), AppointmentID int(10)," \
    "Recommendation text(200));"
tb8="CREATE TABLE Hospital_Lec.Order (PrescriptionNo int(8), SuppliesID int(6));"
tb9="CREATE TABLE Supplies (SuppliesID int(6) PRIMARY KEY, MedID int(8), ProductID int(8));"
tb10="CREATE TABLE Medicine (MedID int(8) PRIMARY KEY, MedName varchar(50), MedType varchar(50), MedAmount varchar(6)," \
    "MedRec text(250), MedProvider varchar(40));"
tb11="CREATE TABLE Product (ProductID int(8) PRIMARY KEY, ProductName varchar(50), ProductType varchar(50), " \
    "ProductAmount varchar(6), ProductRec text(250), ProductProvider varchar(40));"
tb12="CREATE TABLE Request (RequestID int(10) PRIMARY KEY, PatientID int(10), StaffID int(10), RequestDate date, Request" \
     "time time, Sympton varchar(45), RequestStatus varchar(12)); "

at18="ALTER TABLE Patient MODIFY PatientID int(10) NOT NULL AUTO_INCREMENT;"
at19="ALTER TABLE Staff MODIFY StaffID int(10) NOT NULL AUTO_INCREMENT;"
at20="ALTER TABLE Doctor MODIFY DoctorID int(10) NOT NULL AUTO_INCREMENT;"
at21="ALTER TABLE Laboratory MODIFY LabID int(10) NOT NULL AUTO_INCREMENT;"
at22="ALTER TABLE Laboratory_Reservation MODIFY LabResNo int(10) NOT NULL AUTO_INCREMENT;"
at23="ALTER TABLE Appointment MODIFY AppointmentID int(10) NOT NULL AUTO_INCREMENT;"
at24="ALTER TABLE Prescription MODIFY PrescriptionNo int(8) NOT NULL AUTO_INCREMENT;"
at25="ALTER TABLE Supplies MODIFY SuppliesID int(6) NOT NULL AUTO_INCREMENT;"
at26="ALTER TABLE Medicine MODIFY MedID int(8) NOT NULL AUTO_INCREMENT;"
at27="ALTER TABLE Product MODIFY ProductID int(8) NOT NULL AUTO_INCREMENT;"
at28="ALTER TABLE Request MODIFY RequestID int(10) NOT NULL AUTO_INCREMENT;"

at1="ALTER TABLE Laboratory_Reservation ADD FOREIGN KEY (LabID) REFERENCES Laboratory(LabID);"
at2="ALTER TABLE Laboratory_Reservation ADD FOREIGN KEY (StaffID) REFERENCES Staff(StaffID);"
at3="ALTER TABLE Laboratory_Reservation ADD FOREIGN KEY (PatientID) REFERENCES Patient(PatientID);"
at4="ALTER TABLE Laboratory_Reservation ADD FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID);"
at5="ALTER TABLE Appointment ADD FOREIGN KEY (StaffID) REFERENCES Staff(StaffID);"
at6="ALTER TABLE Appointment ADD FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID);"
at7="ALTER TABLE Appointment ADD FOREIGN KEY (PatientID) REFERENCES Patient(PatientID);"
at8="ALTER TABLE Appointment ADD FOREIGN KEY (RequestID) REFERENCES Request(RequestID);"
at9="ALTER TABLE Prescription ADD FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID);"
at10="ALTER TABLE Prescription ADD FOREIGN KEY (StaffID) REFERENCES Staff(StaffID);"
at11="ALTER TABLE Prescription ADD FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID);"
at12="ALTER TABLE Hospital_Lec.Order ADD FOREIGN KEY (PrescriptionNo) REFERENCES Prescription(PrescriptionNo);"
at13="ALTER TABLE Hospital_Lec.Order ADD FOREIGN KEY (SuppliesID) REFERENCES Supplies(SuppliesID);"
at14="ALTER TABLE Supplies ADD FOREIGN KEY (MedID) REFERENCES Medicine(MedID);"
at15="ALTER TABLE Supplies ADD FOREIGN KEY (ProductID) REFERENCES Product(ProductID);"
at16="ALTER TABLE Request ADD FOREIGN KEY (PatientID) REFERENCES Patient(PatientID);"
at17="ALTER TABLE Request ADD FOREIGN KEY (StaffID) REFERENCES Staff(StaffID);"

cursor=connection.cursor()

#cursor.execute(db)

cursor.execute(tb1)
cursor.execute(tb2)
cursor.execute(tb3)
cursor.execute(tb4)
cursor.execute(tb5)
cursor.execute(tb6)
cursor.execute(tb7)
cursor.execute(tb8)
cursor.execute(tb9)
cursor.execute(tb10)
cursor.execute(tb11)
cursor.execute(tb12)

cursor.execute(at18)
cursor.execute(at19)
cursor.execute(at20)
cursor.execute(at21)
cursor.execute(at22)
cursor.execute(at23)
cursor.execute(at24)
cursor.execute(at25)
cursor.execute(at26)
cursor.execute(at27)
cursor.execute(at28)

cursor.execute(at1)
cursor.execute(at2)
cursor.execute(at3)
cursor.execute(at4)
cursor.execute(at5)
cursor.execute(at6)
cursor.execute(at7)
cursor.execute(at8)
cursor.execute(at9)
cursor.execute(at10)
cursor.execute(at11)
cursor.execute(at12)
cursor.execute(at13)
cursor.execute(at14)
cursor.execute(at15)
cursor.execute(at16)
cursor.execute(at17)

connection.commit()