import requests, json


def check_word():
    category = input("Введите категорию: ")
    country = input("Введите страну: ")
    cat_words = category.split(" ")
    url = "http://pyphrasy.herokuapp.com/inflect?phrase={word}&cases=gent"
    category_list = list()
    for cat in cat_words:
        resp_cat = requests.get(url.format(word=cat))
        categor = json.loads(resp_cat.content.decode("utf-8"))['gent']
        category_list.append(categor)
    category = " ".join(category_list)
    resp_country = requests.get(url.format(word=country))
    country = json.loads(resp_country.content.decode("utf-8"))['gent']
    print("База производителей {} из {}.".format(category, country))


if __name__ == "__main__":
    check_word()