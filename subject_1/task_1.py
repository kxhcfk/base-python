# Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники.
# Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца, его возраст и кличку,
# а потом выведет все эти данные в одно предложение.
#
# Например: Это желторотый питон по кличке "Каа". Возраст: 34 года.

type_of_pet = input()
age_of_pet = input()
nickname_of_pet = input()

print("Это", type_of_pet, "по кличке", "\"" + age_of_pet + "\".", "Возраст:", nickname_of_pet)
