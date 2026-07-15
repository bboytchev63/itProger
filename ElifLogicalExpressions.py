# Given a test score, determine and print the letter grade using this scale:
# · 90 and above: "A"
# · 80-89: "B"
# . 70-79: "C"
# . 60-69: "D"
# . Below 60: "F"

score = 72

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

temperature = 55
is_raining = False

if not is_raining and temperature >= 65:
    print("Great day for a picnic!")
elif is_raining or temperature < 32:
    print("Stay indoors. Not a great day to be outside.")
else:
    print("A decent enough day for a short walk.")