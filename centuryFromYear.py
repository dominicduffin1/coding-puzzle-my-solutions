#Century from year - years 1 - 9999

year = input("Please enter a year between 1 and 9999. ")

year_length = len(year)

if year_length < 3: #Years 1 ▶️ 99
    century = 1
    print(century)
else:
    year_int = int(year)
    if year_length == 3: #Years 100 ▶️ 999
        if year_int % 100 == 0:
            century = year[0]
        else:
            century = year[0]
            century = int(century)
            century = century + 1
    elif year_length == 4: #Years 1000 ▶️ 9999
        if year_int % 100 == 0:
            century = year[0:2]
        else:
            century = year[0:2]
            century = int(century)
            century = century + 1
    print(century)