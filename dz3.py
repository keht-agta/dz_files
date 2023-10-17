import os


def count_str_file(file):
    file = 'files/'+file
    # print(file)
    with open(file, "r", encoding="utf-8") as f:
        return len(f.readlines())

def data_from_file(file):
    file = 'files/'+file
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

#Получаем список файлов в директории, объединяем в список с кол-вом строк
# в каждом файле и сотрируем список
# открываем файл на запись и записываем туда в цикле имя файла его длину и
# его содержимое
files = os.listdir('files')
sort_files = []
for file in files:
    sort_files.append([count_str_file(file),file])
sort_files = sorted(sort_files)
with open('result.txt', "w", encoding="utf-8") as f:
    for count, file_name in sort_files:
        f.writelines(file_name+'\n')
        f.writelines(str(count)+'\n')
        f.write(data_from_file(file_name)+'\n')


