

def dice():
    path_to_file = input("Введите полный путь до файла: ")
    try:
        file = open(path_to_file, 'r')
    except FileNotFoundError:
        return print("Файл не найден.")
    lines = file.readlines()
    file.close()
    clear_list = [i.replace("\n", "") for i in lines if i[0] != "\n"]
    dice_list = [i.split(" ") for i in clear_list[1:]]
    dice_quantity = clear_list[0]
    data = [[r[0] + r[2], r[1] + r[3], r[4] + r[5]] for r in dice_list]
    sort_list = [sorted(["".join(sorted(r)) for r in i]) for i in data]
    new_list = list()
    [new_list.append(y) for y in sort_list if y not in new_list]
    result = "Результат: {}".format(len(new_list))
    print(result)
    return result


if __name__ == "__main__":
    dice()