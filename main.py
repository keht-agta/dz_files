from pprint import pprint

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

# составляем список для покупки.
# Из книги рецептов выбираем нужный нам рецепт.
# создаем новый словарь из прежнего где key= название, а значение оставшийся словарь
# с зимененным кол-вом в зависимости от повторения и кол-ва персон
def get_shop_list_by_dishes(dishes, person_count):
   shop_list = {}
   for  dish in dishes:
      for ingridients in cook_book.get(dish):
          value_ = ingridients.pop('ingredient_name')
          double_ingridient = shop_list.get(value_)
          if double_ingridient : 
             ingridients['quantity'] = double_ingridient['quantity'] + int(ingridients['quantity']) * person_count
          else: 
             ingridients['quantity'] = int(ingridients['quantity']) * person_count       
          shop_list[value_] = ingridients
   return shop_list


# Задача №1 выполнено
cook_book = make_cook_book("recipes.txt")  
pprint(cook_book)   
# Задача №2 выполнено
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(get_shop_list_by_dishes(['Яичница', 'Омлет'], 2))
#кол-во яиц в яичнице взято для наглядного примера что яйца суммируются
