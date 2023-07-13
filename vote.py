age = int(input("Enter Your Age : "))

vote = int(18)

GG = vote-age
GG = str(GG)

if vote > age:
    print("You Are Not Eligible For Vote" + " You Will Be Eligible In " + GG + " Years")
else:
    print("You Are Eligible")
