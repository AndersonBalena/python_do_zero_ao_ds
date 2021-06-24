import pandas as pd

# Carregar o conjunto de casas disponíveis para compra
data = pd.read_csv("./datasets/kc_house_data.csv")

print("Quantas casas estão disponíveis para compra?")
print("R: " + str(data.shape[0]) + " casas.")

print("Quantos atributos as casas possuem?")
print("R: " + str(data.shape[1]) + " atributos.")

print("Quais são os atributos da casa?")
print("R: " + str(data.columns))

print("Qual a casa mais cara?")
higuer_price = data[['id', 'price']].sort_values('price', ascending=False)
print(higuer_price)

print("Qual a casa com o maior número de quartos?")
more_bedrooms = data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False)
print(more_bedrooms)

print("Qual a soma total de quartos do conjunto de dados?")
print(data['bedrooms'].sum())

print("Quantas casas possuem 2 banheiros?")
house_two_bathrooms = data[['bathrooms']][data['bathrooms'] == 2].count()
print(house_two_bathrooms)

print("Qual o preço médio de todas as casas no conjunto de dados?")
total_price = data['price'].sum()
total_houses = str(data.shape[0])
average_price = float(total_price) / float(total_houses)
print(average_price)

print("Qual o preço médio de casas com 2 banheiros?")
total_price = float(data['price'][data['bathrooms'] == 2].sum())
total_houses = float(data['bathrooms'][data['bathrooms'] == 2].count())
average_price = float(total_price) / float(total_houses)
print(average_price)

print("Qual o preço mínimo entre as casas com 3 quartos?")
three_bedrooms = data[['id', 'bedrooms', 'price']][data['bedrooms'] == 3]
minimum_value = three_bedrooms.sort_values('price')
print(minimum_value)

print("Quantas casas possuem mais de 1300 metros quadrados na sala de estar?")
houses_counter = data[['id', 'sqft_living']][data['sqft_living'] > 1300].count()
print(houses_counter)

print("Quantas casas tem mais de 2 andares?")
houses_counter = data[['floors']][data['floors'] > 2].count()
print(houses_counter)

print("Quantas casas tem vista para o mar?")
houses_counter = data[['waterfront']][data['waterfront'] == 1].count()
print(houses_counter)

print("Das casas com a vista para o mar, quantas tem 3 quartos?")
waterfront_houses = data[['bedrooms']][data['waterfront'] == 1]
waterfront_houses_with_3_bedrooms = waterfront_houses[['bedrooms']][waterfront_houses['bedrooms'] == 2].count()
print(int(waterfront_houses.count()))
print(int(waterfront_houses_with_3_bedrooms))

print("Das casas com mais de 1300 metros quadrados de sala de estar quantas tem 3 banheiros?")
houses_larger_than_1300 = data[['bathrooms']][data['sqft_living'] > 1300]
houses_larger_than_1300_with_3_bathrooms = houses_larger_than_1300[['bathrooms']][houses_larger_than_1300['bathrooms']
                                                                                  == 3].count()
print(int(houses_larger_than_1300.count()))
print(int(houses_larger_than_1300_with_3_bathrooms))
