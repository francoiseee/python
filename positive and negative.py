#Gurango, Christine Francoise O.
#ICT-104

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

if start < 0:
    neg = abs(start)
    pos = end
else:
    neg = abs(end)
    pos = start

if start or end >= 0:
    pos = pos + 1

print(f"The positive numbers: {pos}")
print(f"The negative numbers: {neg}")






