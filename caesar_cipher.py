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
    'home', 'caesar', 'cipher', 'tux'
}


#  MAIN FUNCTION
def caesar_cipher(message, shift, operation=1):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    lst = []

    shift = shift * operation
    for i in message:
        if i.lower() not in alp:
            lst.append(i)
            continue
        
        original_lower = i.lower()
        index = alp.find(original_lower)
        if index != -1:
            cesar_ind = (index + shift) % 26
            if i.isupper():
                lst.append(alp[cesar_ind].upper())
            else:
                lst.append(alp[cesar_ind])
        else:
            print('Some error')

    result = ''.join(lst)
    print('Result:\n → ', result)

    
#  BRUTE-FORCE MODE
def brute():
    message = input('Enter a message for decryption: ')
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp_size = 26
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
                cesar_ind = ((index - shift) % 26)
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
        

        if answer == 'y':
            print(f'Shift {shift:2}: {result}')

    if answer == 'n':
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


def main_loop():
    print_logo()
    while True:  # Main cycle
        dore = greeting_window()
        
        if dore == 1 or dore == 2:
            operation = 1 if dore == 1 else -1
            
            # Encryption|Decryption cycle
            while True:
                message = input('Enter your message: ')
                shift = int(input('Enter shift: '))
                caesar_cipher(message, shift, operation)
                
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
                brute()
                
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