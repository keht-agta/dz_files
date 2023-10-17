from pprint import pprint
class Ingridients:
    
    def __init__(self, string) -> None:
        array_ingridient = string.strip().split(' | ')
        # ingredient_name, quantity,measure 
        self.ingirdients_list = {'ingredient_name' : array_ingridient[0],
        'quantity' : array_ingridient[1], 'measure' : array_ingridient[2]}

cook_book_ = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
   'Яичница': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Колбаса', 'quantity': 50, 'measure': 'г'}, 
   ],  
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }



cook_book = {}
# omlet = Ingridients('Яйцо', 2,'шт.')     
# print(type(omlet.ingirdients_list))
# print(omlet.ingirdients_list)
# cook_book = {}
with open('recipes.txt', "r",encoding="utf-8") as f:
    name = f.readline().strip()
    cook_book[name] = []
    count = int(f.readline().strip())
    print(int(count))
    for i in range(count):
        line = f.readline().strip().split(' | ')
        print(line)
        cook_book[name].append({'ingredient_name' : line[0], 'quantity' : line[1], 'measure' : line[2]})

pprint(cook_book)

    # cook_book[line] += 
    # while line:
    #     cook_book
    #     line = f.readline()
    #     print(line)

#print(type(cook_book['Омлет'][0]))

        