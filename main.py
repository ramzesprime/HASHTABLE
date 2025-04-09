from prettytable import PrettyTable
import sys

def next_prime(n:int) -> int:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    while not is_prime(n):
        n += 1
    return n

class Table():
    def __init__(self,NUM):
        self.unique_keys = []
        self.hash_table = {}
        self.HASHSIZE = next_prime(NUM)
        self.colusi = 0
        
        
    def menu(self):
        print ("what do you want?")
        print("1 - show a table")
        print("2 - make a new value")
        print("3 - delete any value")
        print("4 - search any value")
        print("5 - show a colusiions coef")
        print("6 - exit") 
        choice = int(input())
        if choice == 6:
            sys.exit
        elif choice == 1:
            self.show()
        elif choice == 2:
            self.make_a_new()
        elif choice == 3:
            self.delete()
        elif choice == 4:
            self.search()
        elif choice == 5:
            self.show_col()
        else:
            print("invalid value!")
            self.menu()
            
    def hashing(self,value:str,flag:bool) -> int:
        if flag:
            key = sum(ord(c) for c in value) % self.HASHSIZE
            while key in self.unique_keys:
                key += 1
                self.colusi += 1
            self.unique_keys.append(key)
            return key
        else:
            key = sum(ord(c) for c in value) % self.HASHSIZE
            return key
            
            
    def make_a_new(self):
        print("input your value!")
        value = str(input())

        print("input a price!")
        price = int(input())
        print("input amount!")
        amount = int(input())
        key = self.hashing(value,True)
        print("successfly created a new", {value}, "with key", {key})
        cortesh = (value,price,amount)
        self.hash_table.setdefault(key,cortesh)
        self.menu()
        
    def probe(self,value:str,flag:bool):
        key = self.hashing(value, False)
        for i in range(self.HASHSIZE):
            probe = (key + i) % self.HASHSIZE
            if probe in self.hash_table:
                entry = self.hash_table[probe]
                if entry[0] == value:
                    if flag:
                        del self.hash_table[probe]
                        print(f"Deleted {value} with key {probe}")
                        self.menu()
                        return
                    if flag is False:
                        print(f"A {value} have key {probe}")
                        self.menu()
                        return
            else:
                break 
        print("Value not found.")
        self.menu()
    
    def search(self):
        print("enter your value for search!")
        value = input()
        self.probe(value,False)
    
    def delete(self):
        print("Enter value to delete:")
        value = input()
        self.probe(value,True)

        
    def show(self):
        if self.hash_table:
            table = PrettyTable()
            table.field_names = ["KEY", "Value", "Price", "Amount"]
            for key, (name, price, amount) in self.hash_table.items():
                table.add_row([key, name, price, amount])
            print(table)
            self.menu()
        else:
            print("таблица пуста.")
            self.menu()
            
    def show_col(self):
        try:
            print(self.colusi/len(self.hash_table))
        except ZeroDivisionError:
            print("a table is empty")
        self.menu()
            
sex = Table(35)
sex.menu()