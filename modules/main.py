import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))


sys.path.insert(0, os.path.join(current_dir, 'modules', 'storage'))
sys.path.insert(0, os.path.join(current_dir, 'modules', 'logic'))
sys.path.insert(0, os.path.join(current_dir, 'modules', 'ui'))

from storage import save_history, load_history
from logic import calculate
from ui import get_numbers, show_result, show_history

print("=" * 40)
print("     ДОБРО ПОЖАЛОВАТЬ В КАЛЬКУЛЯТОР")
print("=" * 40)

while True:
    print("\nЧто хотите сделать?")
    print("1 - Посчитать")
    print("2 - Посмотреть историю")
    print("3 - Выйти")
    
    choice = input("Ваш выбор (1-3): ")
    
    if choice == '1':
        a, b, op = get_numbers()
        result = calculate(a, b, op)
        show_result(a, b, op, result)
        save_history(f"{a} {op} {b} = {result}")
    
    elif choice == '2':
        history = load_history()
        show_history(history)
    
    elif choice == '3':
        print("\nДо свидания!")
        break
    
    else:
        print("Неверный выбор, попробуйте снова")