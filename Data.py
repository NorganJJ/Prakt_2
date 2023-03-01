february = 28
january = 31
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

sumfeb = 0
sumjan = 0
summarch = 0
sumapril = 0
summay = 0
sumjune = 0
sumjuly = 0
sumaugust = 0
sumsep = 0
sumoct = 0
sumnov = 0
sumdec = 0

i = 1
while i < february:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumfeb += col
        print(sumfeb)
        sumfeb += digit
        print(sumfeb)
    else:
        sumfeb +=i
        print(sumfeb)
    i+=1

print(f"Итог за февраль: {sumfeb}")

i = 1
while i < january:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumjan += col
        print(sumjan)
        sumjan += digit
        print(sumjan)
    else:
        sumjan +=i
        print(sumjan)
    i+=1

print(f"Итог за январь: {sumjan}")

i = 1
while i < march:
    if i > 9:
        digit = i % 10
        col = i // 10
        summarch += col
        print(summarch)
        summarch += digit
        print(summarch)
    else:
        summarch +=i
        print(summarch)
    i+=1

print(f"Итог за март: {summarch}")

i = 1
while i < april:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumapril += col
        print(sumapril)
        sumapril += digit
        print(sumapril)
    else:
        sumapril +=i
        print(sumapril)
    i+=1

print(f"Итог за апрель: {sumapril}")

i = 1
while i < may:
    if i > 9:
        digit = i % 10
        col = i // 10
        summay += col
        print(summay)
        summay += digit
        print(summay)
    else:
        summay +=i
        print(summay)
    i+=1

print(f"Итог за май: {summay}")

i = 1
while i < june:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumjune += col
        print(sumjune)
        sumjune += digit
        print(sumjune)
    else:
        sumjune +=i
        print(sumjune)
    i+=1

print(f"Итог за июнь: {sumjune}")

i = 1
while i < july:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumjuly += col
        print(sumjuly)
        sumjuly += digit
        print(sumjuly)
    else:
        sumjuly +=i
        print(sumjuly)
    i+=1

print(f"Итог за июль: {sumjuly}")

i = 1
while i < august:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumaugust += col
        print(sumaugust)
        sumaugust += digit
        print(sumaugust)
    else:
        sumaugust +=i
        print(sumaugust)
    i+=1

print(f"Итог за август: {sumaugust}")

i = 1
while i < september:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumsep += col
        print(sumsep)
        sumsep += digit
        print(sumsep)
    else:
        sumsep +=i
        print(sumsep)
    i+=1

print(f"Итог за сентябрь: {sumsep}")

i = 1
while i < october:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumoct += col
        print(sumoct)
        sumoct += digit
        print(sumoct)
    else:
        sumoct +=i
        print(sumoct)
    i+=1

print(f"Итог за октябрь: {sumoct}")

i = 1
while i < november:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumnov += col
        print(sumnov)
        sumnov += digit
        print(sumnov)
    else:
        sumnov +=i
        print(sumnov)
    i+=1

print(f"Итог за ноябрь: {sumnov}")

i = 1
while i < december:
    if i > 9:
        digit = i % 10
        col = i // 10
        sumdec += col
        print(sumdec)
        sumdec += digit
        print(sumdec)
    else:
        sumdec +=i
        print(sumdec)
    i+=1

print(f"Итог за декабрь: {sumdec}")

finallysum = sumjan + sumfeb + summarch + sumapril + summay + sumjuly + sumaugust + sumsep + sumoct + sumnov + sumdec
print(f"Итоговая сумма цифр всех дат каждого месяца в году: {finallysum}")