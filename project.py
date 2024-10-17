# Analyzer National ID 
import calendar as cal

name = input("Enter your name: \n")
ID = input("Enter Yor National ID :\n")
print("====================================")
#check if the ID is valid
if len(ID) == 14:

    #Collect The ID data
    century = int(ID[0])
    Year = int(ID[1:3])
    Month_OF_birth = int(ID[3:5])
    Day_OF_birth = int(ID[5:7])
    Gover_Number = int(ID[7:9])
    Sequence_Number = int(ID[9:12])
    Gender = int(ID[12])
    Goverment = None
    Year_OF_birth = None
    century_Date = None

    # Find The Century and Birth Date
    if century == 1:
        century_Date = "18"
        Year_OF_birth = int(f"{century_Date}0{Year}" if Year < 10 else f"{century_Date}{Year}")
    elif century == 2:
        century_Date = "19"
        Year_OF_birth = int(f"{century_Date}0{Year}" if Year < 10 else f"{century_Date}{Year}")
    elif century == 3:
        century_Date = "20"
        Year_OF_birth = int(f"{century_Date}0{Year}" if Year < 10 else f"{century_Date}{Year}")
    else:
        pass

    Date_of_birth = f"{Day_OF_birth}/{Month_OF_birth}/{Year_OF_birth}"
    Gender = "Female" if Gender % 2 == 0 else "Male"  # --> Find The Gender

    #Find The Goverment
    if Gover_Number == 1:
        Goverment = "Cairo"
    elif Gover_Number == 2:
        Goverment = "Alexandria"
    elif Gover_Number == 3:
        Goverment = "Port Said"
    elif Gover_Number == 4:
        Goverment = "Suez"
    elif Gover_Number == 11:
        Goverment = "Damietta"
    elif Gover_Number == 12:
        Goverment = "Dakahlia"
    elif Gover_Number == 13:
        Goverment = "Al Sharqia"
    elif Gover_Number == 14:
        Goverment = "Qalqilya"
    elif Gover_Number == 15:
        Goverment = "Kafr el-Sheikh"
    elif Gover_Number == 16:
        Goverment = "Gharbiya"
    elif Gover_Number == 17:
        Goverment = "Menofia"
    elif Gover_Number == 18:
        Goverment = "El beheira"
    elif Gover_Number == 19:
        Goverment = "El Esmailia"
    elif Gover_Number == 21:
        Goverment = "Giza"
    elif Gover_Number == 22:
        Goverment = "Bani Suwayf"
    elif Gover_Number == 23:
        Goverment = "El Fayoum"
    elif Gover_Number == 24:
        Goverment = "El Menia"
    elif Gover_Number == 25:
        Goverment = "Assiut"
    elif Gover_Number == 26:
        Goverment = "Sohag"
    elif Gover_Number == 27:
        Goverment = "Qena"
    elif Gover_Number == 28:
        Goverment = "Aswan"
    elif Gover_Number == 29:
        Goverment = "Luxor"
    elif Gover_Number == 31:
        Goverment = "Red Sea"
    elif Gover_Number == 32:
        Goverment = "New Valley"
    elif Gover_Number == 33:
        Goverment = "Matrouh"
    elif Gover_Number == 34:
        Goverment = "North Sinai"
    elif Gover_Number == 35:
        Goverment = "South Sinai"
    elif Gover_Number == 88:
        Goverment = "Out of the country"
    else:
        Goverment = None

    #print The All Data
    print(f"Hello : {name}")
    print(f"Your National ID is : {ID}")
    if century_Date is not None:
        print(f"Your Century Of Brith Is : {int(century_Date)+1}")
    else:
        pass
    print(f"Your Gender Is : {Gender}")
    print(f"Your Birth Goverment Is : {Goverment}")
    print("====================================")
    print(f"Your Date Of Brith Is : {Date_of_birth}")
    print(f"Your year of birth is : {Year_OF_birth}")
    print(f"your mounth of birth is : {Month_OF_birth}")
    print(f"your day of birth is : {Day_OF_birth}")
    print(f"Your Birth Order at {Date_of_birth} Is : {Sequence_Number}")
    print("====================================")
    if Year_OF_birth is not None:
        Calendar = cal.TextCalendar()
        print(Calendar.formatmonth(Year_OF_birth, Month_OF_birth))
        print("====================================")
        age = 2024 - Year_OF_birth
        print(f"Your Age is : {age}")
        print("====================================")
    else:
        pass
else:
    print("Error ID .. Please Enter 14 Digits")
