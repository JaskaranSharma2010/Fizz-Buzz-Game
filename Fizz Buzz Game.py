#  This is a Fizz Buzz Game

print("If The Number is Divisible by 3, it will show - Fizz")
print("If The Number is Divisible by 5, it will show - Buzz")
print("If The Number is Divisible by both, it will show - Fizz Buzz!!")
print("If The Number is not Divisible by any number, it will show - The Number is not Divisible By Both")

Fizz = 3
Buzz = 5
Not_Divisible = "Your Number is not Divisible"

while True:
    num = int(input("Hey, Select a Number From 1 to 100:    "))

    if num % Fizz == 0 and num % Buzz == 0:
        print("Your Number is divisible by both, Fizz Buzz!!")
    elif num % Fizz == 0:
        print("Your Number is divisible by 3, Fizz")
    elif num % Buzz == 0:
        print("Your Number is divisible by 5, Buzz")
    else:
        print("Your Number is not divisible by any number")

    play_again = input("Do you want to play the game again? (Yes/No): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing the game")
        break