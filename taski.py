
#Task 2
def square_number(num):
	return num*num  
def test_square_number():
  assert square_number(2) == 4
  assert square_number(8) == 64
  assert square_number(10) == 100
  print("YOUR CODE IS CORRECT!")
test_square_number()

#Task 3
def is_odd(num):
	if num%2 == 0:
		return False
	else:
		return True
def test_is_odd():
  assert is_odd(2) == False
  assert is_odd(3) == True
  assert is_odd(8) == False
  assert is_odd(100) == False
  assert is_odd(101) == True
  print("YOUR CODE IS CORRECT!")
test_is_odd()

#Task 4
def last_letter(word):
	return word[-1:]
def test_last_letter():
  assert last_letter('hello!') == '!'
  assert last_letter('banana') == 'a'
  assert last_letter('8') == '8'
  assert last_letter('funnyguys') == 's'
  assert last_letter('101') == '1'
  print("YOUR CODE IS CORRECT!")
test_last_letter()

#Task 5
def string_length(word):
	return len(word)
def test_string_length():
  assert string_length('hello!') == 6
  assert string_length('banana') == 6
  assert string_length('8') == 1
  assert string_length('funnyguys') == 9
  assert string_length('101') == 3
  print("YOUR CODE IS CORRECT!")
test_string_length()

#Task 6
def bigger_guy(age, age1):
	if age1 > age:
		return age1
	else:
		return age
def test_bigger_guy():
  assert bigger_guy(1, 2) == 2
  assert bigger_guy(10, 20) == 20
  assert bigger_guy(20, 10) == 20
  assert bigger_guy(10, 10) == 10
  assert bigger_guy(2, 1) == 2
  assert bigger_guy('a', 'b') == 'b' # 'b' is greater than 'a'
  print("YOUR CODE IS CORRECT!")
test_bigger_guy()

#Task 7
def biggest_guy(age, age1, age2):
	if age > age1 and age > age2:
		return age
	elif age1 > age and age1 > age2:
		return age1
	else:
		return age2    
def test_biggest_guy():
  try:
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'

  except (AssertionError) as e:
    print(e)
    print("Wrong!!")
    print("Correct buddy!!!")
test_biggest_guy()

# Task 8
def choice_to_number(choice):
	if choice == 'Usain':
		return 1
	elif choice  == 'Me':
		return 2
	else:
		return 3

def number_to_choice(number):
	if number == 1:
		return 'Usain'
	elif number == 2:
		return 'Me'
	else:
		return 'Aybek'

def test_choice_to_number():
  assert choice_to_number('Usain') == 1
  assert choice_to_number('Me') == 2
  assert choice_to_number('Aybek') == 3

def test_number_to_choice():
  assert number_to_choice(1) == 'Usain'
  assert number_to_choice(2) == 'Me'
  assert number_to_choice(3) == 'Aybek'

def test_all():
  try:
      test_choice_to_number()
      test_number_to_choice()

  except AssertionError:
      print("wrong")

  else:
    print("success")
test_all()

## Problem 5:
  # Спросите у пользователя 2 даты. Формат ввода должен быть следующим: ДД, ММ, ГГГГ
  # Посчитайте разницу в днях между двумя датами.

  # Пример:
    # Date 1: 10, 05, 2019
    # Date 2: 11, 12, 2020
    # Результат: 151 день

    # Date 1: 29, 08, 1999
    # Date 2: 20, 03, 2030
    # Результат: 11161 день

date_1 = (28, 5, 1988)
date_2 = (7, 9, 1989)

print(abs(date_1[0] - date_2[0]) + 30*abs(date_2[1]-date_1[1]) + 365*abs(date_2[2] - date_1[2]))
 

