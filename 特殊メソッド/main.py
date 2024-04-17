class Book:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class SupuNumber:
    def __init__(self, value) -> None:
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, SupuNumber):
            return f"1: {self.value} + {other.value}"
        else:
            print('error')
            return NotImplemented
    
class SupuNumber2:
    def __init__(self, value) -> None:
        self.value = value
    
    def __radd__(self, l_other):
        if isinstance(l_other, SupuNumber):
            return f"2: {l_other.value}{self.value}"
        else:
            return NotImplemented

class SupuInt(int):
    def __new__(cls, n):
        new_value = n * 1
        return super().__new__(cls, new_value)

class SupuUser:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        
    def __eq__(self, other):
        
        if self.id == other.id:
            print("SupuUser2内の__eq__")
            return True
        else:
            return False

class SupuTowSizeArray:
    def __setitem__(self, index, value):
        if index == 0:
            self.v_0 = value
        elif index == 1:
            self.v_1 = f"{value}{value}"
        else:
            raise IndexError('indexは0, 1だけです1')
        
    def __getitem__(self, index):
        if index == 0:
            return self.v_0
        elif index == 1:
            return self.v_1
        else:
            raise IndexError('indexは0, 1だけです')

if __name__ == "__main__":
    
    # book_1 = Book("はらぺこあおむし", 1200)
    # # print(book_1.name)
    
    s_n_1 = SupuNumber(10)
    s_n_2 = SupuNumber2(20)

    result = s_n_1 + s_n_2
    print(result)
    
    # s_int = SupuInt(10)
    # print(s_int, type(s_int))
    
    # user1 = SupuUser(1, "first")
    # user2 = SupuUser(2, "second")
    # print(user1 == user2)
    
    # s_a = SupuTowSizeArray()
    # s_a[0] = "Apple"
    # s_a[1] = "Banana"
    # print(s_a[0])
    # print(s_a[1])