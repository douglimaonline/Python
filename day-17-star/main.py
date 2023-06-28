class Pessoa:
    def __init__(self):
        Pessoa.name = ''
        Pessoa.age = 0

    def birthday(self):
        Pessoa.age += 1


pessoa1 = Pessoa()
pessoa1.name = 'dodoritos'

print(pessoa1.age)

pessoa1.birthday()
pessoa1.birthday()
print(pessoa1.age)
