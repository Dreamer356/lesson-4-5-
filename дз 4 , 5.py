import random

class NumberEncryptor:
    def __init__(self):
        self.number = None

    def encrypt(self, number):
        operation = random.choice(['add', 'subtract'])
        if operation == 'add':
            self.number = number + random.randint(1, 10)
        else:
            self.number = number - random.randint(1, 10)

    def __str__(self):
        if self.number is not None:
            return f"Зашифроване число: {self.number}"
        else:
            return "Немає зашифрованих даних."

encryptor = NumberEncryptor()
input_number = 42
encryptor.encrypt(input_number)
print(encryptor)