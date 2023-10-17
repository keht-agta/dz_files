from pprint import pprint
class Ingridients:
    
    def __init__(self, string) -> None:
        array_ingridient = string.strip().split(' | ')
        # ingredient_name, quantity,measure 
        self.ingirdients_list = {'ingredient_name' : array_ingridient[0],
        'quantity' : array_ingridient[1], 'measure' : array_ingridient[2]}

def make_cook_book(file_name):
    cook_book_ = {}
    with open(file_name, "r",encoding="utf-8") as f:
      while True:
        name = f.readline().strip()
        if not name:
            break #конец файла
        cook_book_[name] = []
        count = int(f.readline().strip())
        # print(int(count))
        for i in range(count):
            line = f.readline().strip().split(' | ')
            # print(line)
            cook_book_[name].append({'ingredient_name' : line[0], 'quantity' : line[1], 'measure' : line[2]})
        f.readline()
    return cook_book_

def get_shop_list_by_dishes(dishes, person_count):
   shop_list = {}
   for  dish in dishes:
      for ingridients in cook_book.get(dish):
          value_ = ingridients.pop('ingredient_name')
          double_ingridient = shop_list.get(value_)
          if double_ingridient :
             print(double_ingridient)
             ingridients['quantity'] = double_ingridient['quantity'] + int(ingridients['quantity']) * person_count
          else: 
             ingridients['quantity'] = int(ingridients['quantity']) * person_count
          # print(ingridients)
          shop_list[value_] = ingridients
          
             
      # print(len(cook_book.get(dish)))
      # shop_list[]

   return shop_list


# Задача №1 выполнено
cook_book = make_cook_book("recipes.txt")     
# pprint(cook_book)

# Задача №2
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

pprint(get_shop_list_by_dishes(['Яичница', 'Омлет'], 2))
# pprint(cook_book)