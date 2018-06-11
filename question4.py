points= int(input('Enter the points,must be under 200 : '))

if points < 50:
    print("Sorry! No prize this time.")

if points >= 51 and points <= 150:
    print("Congratulations! You won a [WOODEN DOG]!")

elif points >=151 and points <= 180:
    print("Congratulations! You won a [BOOK]!")

elif points >= 181 and points <=200:
    print("Congratulations! You won a [CHOCOLATES]!")
else:
    print("wrong points")