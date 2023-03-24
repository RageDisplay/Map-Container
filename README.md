# Map-Container

# Лабораторная работа №2 – Контейнер map

*Задача*: реализовать ассоциативный массив (контейнер map) на основе двоичного дерева поиска (красно-черного или AVL). Каждый узел двоичного дерева должен содержать пару ключ-значение. Пользователь должен иметь возможность: получить значение по ключу, изменить значение по ключу, добавить в контейнер новую пару.

Для реализации контейнера `map` на основе двоичного дерева поиска на языке Python, можно создать класс `BinarySearchTree`. Каждый узел дерева будет представляться объектом `Node`, который содержит ключ (`key`), значение (`value`), и ссылки на правый (`right`) и левый (`left`) поддеревья.

Класс `BinarySearchTree` будет содержать методы для добавления элемента (`add`), поиска элемента по ключу (`find`), изменения значения элемента по ключу (`update`) и вывода содержимого контейнера (`print_tree`).
