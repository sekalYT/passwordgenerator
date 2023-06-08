import random
import string

def select_language():
    print("Select Language")
    print("1 - English")
    print("2 - Russian")
    choice = input()
    if choice == "1":
        generate_password("en")
    elif choice == "2":
        generate_password("ru")
    else:
        print("Invalid choice")
        select_language()

def generate_password(language):
    if language == "en":
        all_characters = string.ascii_letters + string.digits + string.punctuation
        prompt = "Enter desired password length: "
        generated_message = "Generated password:"
    elif language == "ru":
        all_characters = string.ascii_letters + string.digits + string.punctuation + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        prompt = "Введите желаемую длину пароля: "
        generated_message = "Сгенерированный пароль:"
    else:
        print("Invalid language")
        select_language()
        return

    length = int(input(prompt))
    random_password = ''.join(random.choice(all_characters) for _ in range(length))
    print(generated_message, random_password)

select_language()
