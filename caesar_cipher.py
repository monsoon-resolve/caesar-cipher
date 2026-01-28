from sys import exit


def print_logo():
    logo = """
    ═══════════════════════════════════════════════════════════
    
    [ALPHABET ROTATION ENGINE]    
    ORIGINAL: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    SHIFT:    ████████████ (+3)                                 ↓
    RESULT:   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
        
    ╭────────────────────────────────────────────────────╮
    │                                                    │
    │   ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗   │
    │  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  │
    │  ██║     ███████║█████╗  ███████╗███████║██████╔╝  │
    │  ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗  │
    │  ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║  │
    │   ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  │
    │                                                    │
    │      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗     │
    │     ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗    │ 
    │     ██║     ██║██████╔╝███████║█████╗  ██████╔╝    │ 
    │     ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗    │ 
    │     ╚██████╗██║██║     ██║  ██║███████╗██║  ██║    │ 
    │      ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    │
    ╰────────────────────────────────────────────────────╯
                
                                            𝐵𝓎 𝓂 𝑜𝓃𝓈𝑜𝑜𝓃 𝓇𝑒𝓈𝑜𝓁𝓋𝑒
    ═══════════════════════════════════════════════════════════
                                            """
    print(logo)


common_words = {
    # English words
    'the', 'and', 'that', 'have', 'for', 'not', 'with', 'you', 'this', 'but',
    'from', 'they', 'say', 'her', 'she', 'will', 'one', 'all', 'would', 'there',
    'their', 'what', 'about', 'who', 'get', 'which', 'when', 'make', 'like', 'time',
    'just', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could',
    'them', 'see', 'other', 'than', 'then', 'look', 'only', 'come', 'its', 'over',
    'think', 'also', 'back', 'after', 'work', 'first', 'well', 'even', 'want', 'because',
    'these', 'give', 'most', 'hello', 'world', 'python', 'code', 'program', 'computer',
    'message', 'text', 'file', 'data', 'system', 'information', 'test', 'example',
    'encrypt', 'decrypt', 'caesar', 'cipher', 'shift', 'letter', 'word', 'number',
    'space', 'result', 'answer', 'question', 'choice', 'menu', 'exit', 'enter',
    'again', 'please', 'thank', 'sorry', 'really', 'quite', 'almost', 'enough',
    'maybe', 'perhaps', 'sometimes', 'never', 'always', 'often', 'usually', 'seldom',
    'rarely', 'attack', 'dawn', 'secret', 'hidden', 'password', 'security', 'crypto',
    'encryption', 'decryption', 'brute', 'force', 'algorithm', 'person', 'thing',
    'place', 'government', 'company', 'group', 'problem', 'become', 'mean', 'help',
    'different', 'important', 'public', 'against', 'among', 'without', 'within',
    'following', 'behind', 'beyond', 'except', 'above', 'system', 'program',
    'linux', 'arch', 'ubuntu', 'gentoo', 'mint', 'host', 'kali', 'win', 'windows',
    'home', 'caesar', 'cipher', 'tux',
    
    # Russian words
    'свой', 'при', 'что', 'это', 'она',
    'так', 'они','оно', 'для','ваш','что', 'это', 'она','быть',
    'или', 'уже', 'ему', 'вот', 'где', 'даже', 'как', 'его', 
    'мой', 'без', 'над', 'под', 'после', 'этот', 'какой', 'слово',
    'делать', 'знать', 'стать', 'день', 'человек', 'рука', 'глаз',
    'время', 'дело', 'жизнь', 'друг', 'дом', 'мир', 'конец', 'вид',
    'голова', 'сторона', 'город', 'земля', 'вода', 'лицо', 'нога',
    'место', 'дверь', 'окно', 'стол', 'стул', 'книга', 'бумага',
    'номер', 'пример', 'работа', 'слово', 'ночь', 'деньги', 'утро',
    'вечер', 'неделя', 'месяц', 'год', 'час', 'минута', 'секунда',
    'хорошо', 'плохо', 'большой', 'маленький', 'новый', 'старый',
    'молодой', 'красивый', 'сильный', 'слабый', 'быстрый', 'медленный',
    'теплый', 'холодный', 'дорогой', 'дешевый', 'легкий', 'тяжелый',
    'веселый', 'грустный', 'серьезный', 'важный', 'нужный', 'лишний',
    'правда', 'ложь', 'счастье', 'любовь', 'дружба', 'семья',
    'мама', 'папа', 'брат', 'сестра', 'друг', 'подруга', 'ребенок',
    'кто', 'что', 'какой', 'где', 'куда', 'когда', 'почему', 'зачем',
    'сколько', 'чей', 'как', 'можно', 'нужно', 'надо', 'можно',
    'весь', 'все', 'всё', 'каждый', 'никто', 'ничто', 'некто',
    'что-то', 'кое-что', 'кто-то', 'кое-кто', 'где-то', 'куда-то',
    'быть', 'мочь', 'хотеть', 'знать', 'думать', 'говорить', 'сказать',
    'делать', 'сделать', 'идти', 'ходить', 'бежать', 'стоять', 'сидеть',
    'лежать', 'спать', 'есть', 'пить', 'читать', 'писать', 'смотреть',
    'видеть', 'слышать', 'слушать', 'понимать', 'понять', 'узнать',
    'вспоминать', 'помнить', 'забывать', 'ждать', 'искать', 'найти',
    'брать', 'взять', 'давать', 'дать', 'получать', 'получить',
    'открывать', 'открыть', 'закрывать', 'закрыть', 'начинать', 'начать',
    'кончать', 'кончить', 'продолжать', 'продолжить', 'кончаться',
    'интернет', 'компьютер', 'телефон', 'программа', 'файл', 'папка',
    'ссылка', 'сайт', 'страница', 'сообщение', 'письмо', 'пароль',
    'логин', 'пользователь', 'админ', 'модератор', 'чат', 'форум',
    'игра', 'фильм', 'музыка', 'видео', 'фото', 'картинка',
    'документ', 'проект', 'задача', 'проблема', 'решение', 'ответ',
    'вопрос', 'команда', 'система', 'версия', 'обновление', 'ошибка',
    'шифр', 'шифрование', 'расшифровка', 'ключ', 'алгоритм', 'код',
    'текст', 'сообщение', 'секрет', 'тайна', 'безопасность', 'защита',
    'взлом', 'атака', 'защита', 'проверка', 'доступ', 'блокировка',
    'сертификат', 'подпись', 'шифровать', 'дешифровать', 'взламывать',
    'линукс', 'пайтон', 'питон', 'слово', 'привет'
}


#  MAIN FUNCTION
def caesar_cipher(message, shift, operation=1, alp = None):
    lst = []
    alp_size = len(alp)

    shift = shift * operation
    for i in message:
        if i.lower() not in alp:
            lst.append(i)
            continue
        
        original_lower = i.lower()
        index = alp.find(original_lower)
        if index != -1:
            cesar_ind = (index + shift) % alp_size
            if i.isupper():
                lst.append(alp[cesar_ind].upper())
            else:
                lst.append(alp[cesar_ind])
        else:
            print('Some error')

    result = ''.join(lst)
    print('Result:\n → ', result)

    
#  BRUTE-FORCE MODE
def brute(alp):
    message = input('Enter a message for decryption: ')
    alp_size = len(alp)
    answer = input('Show all shifts? (Y/N): ').lower()
    #  VARIABLES FOR BETTER RESULTS
    best_shift = 0
    best_text = ""
    best_percent = 0

    for shift in range(1, alp_size+1):
        lst = []
        for i in message:
            if i.lower() not in alp:
                lst.append(i)
                continue
            index = alp.find(i.lower())
            if index != -1:
                cesar_ind = ((index - shift) % alp_size)
                if i.isupper():
                    lst.append(alp[cesar_ind].upper())
                else:
                    lst.append(alp[cesar_ind])
        
        result = ''.join(lst)
        percent = clean(result)
        
        if percent > best_percent:
            best_shift = shift
            best_text = result
            best_percent = percent
        

        if answer in ['y', 'д', 'yes', 'да']:
            print(f'Shift {shift:2}: {result}')

    if answer in ['n', 'н', 'no', 'нет']:
        if best_percent == 0:
            print('Try enter \'Y\' next time')
        else:
            print(f"\nMost likely (shift {best_shift}, confidence {best_percent:.1f}%):")
            print(f"→ {best_text}")


#  AFTER-ACTION SELECTION FUNCTION
def get_choice():
    print('What should we do next?')
    while True:
        try:
            choi = int(input('[1] Again        [2] Main menu\n[3] Exit\n→ '))
            if choi in [1, 2, 3]:
                return choi
            else:
                print('Enter 1, 2 or 3')
        except ValueError:
            print('Enter a number')


#  PROBABLITY FUNCTION OF A CORRECT WORD
def clean(result):
    if not result:
        return 0
    
    words = result.split()
    if not words:
        return 0
    score = 0
    
    for word in words:
        cleaned_word = word.strip('.,!?;:"\'')
        if cleaned_word.lower() in common_words:
            score += 1
    
    return score / len(words) * 100


#  TUI INTERFACE
def greeting_window():
    print('What mode do you want to use?')
    while True:
        try:
            dore = int(input('[1] Encryption        [2] decryption\n[3] Brute-Force       [4] Exit\n→ '))
            if 1 <= dore <= 3:
                break
            elif dore == 4:
                exit()
            else:
                print('You can enter a number in the range from 1 to 4')
        except ValueError:
            print('Please enter a number')
    return dore

def lang():
    alp_en = 'abcdefghijklmnopqrstuvwxyz'
    alp_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    print('Please select your language')
    while True:
        try:
            language = int(input('[1] English        [2] Russian\n→ '))
        except ValueError:
            print('Enter an integer')
        if not language in [1, 2]:
            print('Please enter a number in 1, 2')
        elif language == 1:
            return alp_en
        else:
            return alp_ru


def main_loop():
    print_logo()
    language = lang()
    while True:  # Main cycle
        dore = greeting_window()
        
        if dore == 1 or dore == 2:
            operation = 1 if dore == 1 else -1
            
            # Encryption|Decryption cycle
            while True:
                message = input('Enter your message: ')
                shift = int(input('Enter shift: '))
                caesar_cipher(message, shift, operation, language)
                
                choice = get_choice()
                if choice == 1:  # Again
                    continue
                elif choice == 2:  # Back
                    break
                elif choice == 3:  #  Exit
                    exit()
        
        elif dore == 3:
            # brute-force cycle
            while True:
                brute(language)
                
                choice = get_choice()
                if choice == 1:  # Again
                    continue
                elif choice == 2:  # Back
                    break
                elif choice == 3:  # Exit
                    exit()


try:
    main_loop()
except KeyboardInterrupt:
    print("\n\nThe program was closed by the user")