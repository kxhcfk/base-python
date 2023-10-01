# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов.
# Он должен запрашивать по порядку этапы развития человека (проверим твое умение гуглить, что тоже очень важно для программиста.)
# и в конце вывести все стадии, разделенные знаком =>, что будет означать постепенный переход от одного к другому.
# В следующих уроках мы дополним эту форму до полноценного теста, который будет проверять правильность ответов, а пока - начнем с малого.
#
# Напоминаем, что разделить эти данные тебе поможет команда sep внутри команды print, например,
# чтобы разделить переменные знаком + нужно ввести: print(a1, a2, a3, sep='+')
#
# Подсказка: последняя стадия развития - Homo sapiens sapiens.

stage_of_evolution_1 = input("First stage of evolution: ")
stage_of_evolution_2 = input("Second stage of evolution: ")
stage_of_evolution_3 = input("Third stage of evolution: ")
stage_of_evolution_4 = input("Fourth stage of evolution: ")
stage_of_evolution_5 = input("Fifth stage of evolution: ")
stage_of_evolution_6 = input("Sixth stage of evolution: ")
stage_of_evolution_7 = input("Seventh stage of evolution: ")
stage_of_evolution_8 = input("Eighth stage of evolution: ")
stage_of_evolution_9 = input("Ninth stage of evolution: ")

print(
    stage_of_evolution_1,
    stage_of_evolution_2,
    stage_of_evolution_3,
    stage_of_evolution_4,
    stage_of_evolution_5,
    stage_of_evolution_6,
    stage_of_evolution_7,
    stage_of_evolution_8,
    stage_of_evolution_9,
    sep="=>"
)
