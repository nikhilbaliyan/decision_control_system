age1= int(input('Enter the 1st person age : '))
age2= int(input('Enter the 2nd person age : '))
age3= int(input('Enter the 3rd person age : '))
if age1 > age2 and age1 > age3 and age2 > age3:
    print("1st person is oldest and 3rd person is youngest")
elif age1 > age2 and age1 > age3 and age3 > age2:
    print("1st person is oldest and 2nd person is youngest")
elif age2 > age3 and ag2 > age1 and age1 > age3:
    print("2nd person is oldest and 3rd person is youngest")
elif age2 > age3 and ag2 > age1 and age3 > age1:
    print("2nd person is oldest and 1st person is youngest")
elif age3 > age1 and age3 > age2 and age2 > age1:
    print("3rd person is oldest and 1st person is youngest")
elif age3 > age1 and age3 > age2 and age1 > age2:
    print("3rd person is oldest and 1st person is youngest")