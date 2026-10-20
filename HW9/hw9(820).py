import sys

class Buffer:
    def __init__(self):
        self.data = []

    def _to_int(self, x):                                              
        if isinstance(x, bool):                                        
            raise ValueError(f"ошибка: поддерживаются только целые числа") 
           
        try:                                                           
            if isinstance(x, float) and not x.is_integer():          
                raise ValueError                                      
            return int(x)                                          
        except (ValueError, TypeError):                                
            raise ValueError(f"ошибка: поддерживаются только целые числа")      

    def add(self, *a):
        for x in a:

            if isinstance(x, (list, tuple)):
                self.data.extend(self._to_int(y) for y in x)  

            else:
                self.data.append(self._to_int(x))  

        while len(self.data) >= 5:
            print(sum(self.data[:5]))
            del self.data[:5]

    def get_current_part(self):
        return list(self.data)

def parse_line(line):
    parts = line.split()
    if not parts:
        return None
    
    result = []
    for p in parts:                                                    
        try:                                                           
            result.append(int(p))                                      
        except ValueError:                                             
            print(f"ошибка: поддерживаются только целые числа")                   
            return None                                                
    return result

buf = Buffer()
for line in sys.stdin:
    numbers = parse_line(line)
    if numbers is None:
        continue  # порожній або некоректний рядок пропускаємо
    buf.add(*numbers)
    print(buf.get_current_part())

# Дано послідовність цілих чисел. Необхідно її обробити і вивести на екран суму першої пʼятірки чисел
# із цієї послідовності, потім суму другої пʼятірки, і т. д. Але послідовність не дається відразу загалом.
# З плином часу до вас надходять її послідовні частини. Наприклад, спочатку перші три елементи, потім наступні шість,
# потім наступні два і т. д. Реалізуйте клас Buffer, який буде накопичувати в собі елементи послідовності і виводити 
# суму пʼятірок послідовних елементів у міру їх накопичення. Однією з вимог до класу є те, що він не повинен 
# зберігати в собі більше елементів, ніж йому дійсно необхідно, тобто, він не повинен зберігати елементи, 
# які вже увійшли в пʼятірку, для якої була виведена сума.

#   Вхідні дані:

#       1 2 3
#       4 5 6
#       7 8 9 10
#       1 1 1 1 1 1 1 1 1 1 1

#   Вихідні дані:
#       [1,2,3]
#       15
#       [6]
#       40
#       []
#       5 
#       5
#       [1]