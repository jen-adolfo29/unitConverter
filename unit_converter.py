# === UNIT CONVERTER ===

print()
print("=== UNIT CONVERTER ===")
print()

conversions_list = [(1, 'km', 'mi'),
                    (2, 'mi', 'km'),
                    (3, 'kg', 'lbs'),
                    (4, 'inch', 'ft'),
                    (5, 'cm', 'm')
                    ]
print('Conversions available: ')
print()

for conversions_number, from_unit, to_unit in conversions_list:
    print(f'{conversions_number}) {from_unit} -> {to_unit}')

print()
conversion = input('Enter number of conversion to use -> ')
conversion_index = int(conversion) - 1

conversions_number, from_unit, to_unit, = conversions_list[conversion_index]
print()
from_value = float(input(f'Enter {from_unit} --> '))
print()

if conversions_number == 1:
    to_value = from_value * 0.62
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversions_number == 2:
    to_value = from_value * 1.61
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversions_number == 3:
    to_value = from_value * 2.20
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversions_number == 4:
    to_value = from_value * 0.08
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversions_number == 5:
    to_value = from_value * 0.01
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

