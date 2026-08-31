pointsgeneral = int(input("gesamtpunktzahl:"))
youtpoints = int(input("deine punkte:"))

notenprozent = youtpoints / pointsgeneral * 100

if notenprozent > 95:
    print("sehrgut (1)")

elif notenprozent > 80:
    print("gut (2)")

elif notenprozent > 65:
    print("befridigent (3)")

elif notenprozent > 50:
    print("ausreichend (4)")

elif notenprozent > 33:
    print("manglehat (5)")

else:
    print("ungenügend (6)")




