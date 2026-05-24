import sys

# ЭТИ ПУТИ ДОЛЖНЫ БЫТЬ ТОЧНЫМИ
sys.path.insert(0, 'storage')
sys.path.insert(0, 'logic')
sys.path.insert(0, 'ui')

from storage import save_history, load_history
from logic import calculate
from ui import get_numbers, show_result, show_history

print("=" * 40)
print("     КАЛЬКУЛЯТОР")
print("=" * 40)

while True:
    print("\n1 - Посчитать")
    print("2 - История")
    print("3 - Выйти")
    
    choice = input("Выберите: ")
    
    if choice == '1':
        a, b, op = get_numbers()
        r = calculate(a, b, op)
        show_result(a, b, op, r)
        save_history(f"{a} {op} {b} = {r}")
    elif choice == '2':
        show_history(load_history())
    elif choice == '3':
        break