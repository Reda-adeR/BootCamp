import datetime
my_age = input("Saisir votre âge : ")
yearToday = (datetime.datetime.now())
print("votre age apres dans l'annee:",(yearToday.year+int(my_age)), " est : ",(int(my_age)+24))
yearOfBirth = input("Saisir votre année de naissance : ")
print("votre age est :" ,(yearToday.year-int(yearOfBirth)))