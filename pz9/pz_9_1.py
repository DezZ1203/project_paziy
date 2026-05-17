#Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
#стран. Определить какие марки машин были доставлены во все указанные страны, какие в
#некоторые из стран и какие не доставлены ни в одну страну.all_countries = {'Германия', 'Франция', 'Италия', 'Испания'}
# Данные по маркам
exports = {
    'Toyota': {'Германия', 'Франция'},          # в некоторые, но не все
    'BMW': {'Германия', 'Франция', 'Италия', 'Испания'},  # во все
    'Ford': {'Италия'},                          # в некоторые (только одна)
    'Fiat': set(),                                # ни в одну (пустое множество)
    'Audi': {'Германия', 'Франция', 'Италия'},   # в некоторые (не хватает Испании)
    'Renault': {'Франция', 'Испания'},            # в некоторые
    'Opel': set()                                 # ни в одну
}

all_countries_set = set()      # марки, поставляемые во все страны
some_countries_set = set()     # марки, поставляемые в некоторые
no_countries_set = set()       # марки, не поставляемые ни в одну страну
# Проходим по всем маркам и их странам
for brand, countries in exports.items():
    if countries == all_countries_set:
        # Множество стран марки совпадает со множеством всех стран
        all_countries_set.add(brand)
    elif not countries:
        # Множество стран пустое
        no_countries_set.add(brand)
    else:
        # Остальные случаи
        some_countries_set.add(brand)

# Вывод результатов
print("Марки, доставленные во все указанные страны:")
if all_countries_set:
    for brand in sorted(all_countries_set):
        print(f"  {brand}")
else:
    print("  нет")

print("\nМарки, доставленные в некоторые из стран:")
if some_countries_set:
    for brand in sorted(some_countries_set):
        print(f"  {brand}")
else:
    print("  нет")

print("\nМарки, не доставленные ни в одну страну:")
if no_countries_set:
    for brand in sorted(no_countries_set):
        print(f"  {brand}")
else:
    print("  нет")