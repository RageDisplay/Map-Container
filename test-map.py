from map import BinarySearchTree

test = BinarySearchTree()
test.add(4, "четыре") #Добавить элемент с ключом
test.add(2, "два")
test.add(6, "шесть")
test.add(1, "один")
test.add(3, "три")
test.add(5, "пять")
test.add(7, "семь")

test.print_tree() #Вывести дерево с ключами

print("Найдено: "+test.find(4)) #Найти элемент под ключом 4

test.update(4, "Красивое четыре") #Заменить элемент под ключом 4

test.print_tree()

print("Найдено: "+test.find(4)) 