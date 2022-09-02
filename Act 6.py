#Lab task 6

meters = input("Input distance (meters): ")
hr = input("Input time (hours): ")
min = input("Input time (minutes): ")
sec = input("Input time (seconds): ")

hr_total = float(hr) + (float(min) / 60) + ((float(sec) / 60) / 60)
sec_total = ((float(hr) * 60) * 60) + (float(min) * 60) + float(sec)
kms = float(meters) / 1000

miles = float(meters) / 1609.344
print("Your speed in meters/sec is:", float(meters) / sec_total)
print("Your speed in km/h is: ", kms / hr_total)
print("Your speed in miles/h is: ", miles / hr_total)

# I worked on this one with a class mate ecause I was so confused about the conversions