viewing_figures = []
holder = 0
prime_time = ""
agreement = ""
average_figures = 0

program_name = input("Please enter the name of the program: ")

for eaStr in range(1, 6):
    holder = input("Please enter the viewing figures for episode " + str(eaStr))
    viewing_figures.append(int(holder))

prime_time = input("Is this a prime time show?")

while prime_time != "yes" and prime_time != "Yes" and prime_time != "No" and prime_time != "no":
    prime_time = input("I'm sorry, the answer must be either yes or no... Please try again: ")

agreement = input("Have all of the actors agreed?")

print(viewing_figures)
print("The average viewing figures are ")
average_figures = sum(viewing_figures) / (len(viewing_figures))
average_figures = round(average_figures)
print(average_figures)

if agreement == "No" or agreement == "no":
    series_kept_on = False
elif average_figures >= 4000000 and prime_time == "No" or prime_time == "no":
    series_kept_on = True
elif average_figures >= 6000000 and prime_time == "Yes" or prime_time == "yes":
    series_kept_on = True
else:
    series_kept_on = False

print("")

for eaStr in range(len(viewing_figures)):
    print("The viewing figures for episode " + str(eaStr + 1) + " are " + str(viewing_figures[eaStr]))

print("The average viewing figures is " + str(average_figures))

if series_kept_on is False:
    print("\n" + program_name + " will be kept on")
else:
    print("\n" + program_name + " will not be kept on")
