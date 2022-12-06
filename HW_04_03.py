''' 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.'''

''' "... до 240" - однозначно не укзаано, 240 включительно или нет, 
предлог "до" имеет двоякое значение. Если в функции range второй параметр 240 
- то 240 не будет включаться в генерацию. 
Для включения нужно увеличить второй параметр до 241'''

res = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(res)
