#Codigo criado para tratar a entrada de usuarios.

def nome() -> str:
    nome = input('Digite o seu nome maior que 3 caracteres: ')
    while len(nome) < 3:
        print('Nome menor que 3 caracteres')
        nome = input('Digite o seu nome: ')
    return nome

def idade() -> int:
    idade = int(input('Digite sua idade: '))
    while idade < 0 or idade > 150:
        print('Digite uma idade entre 0 e 150: ')
        idade = int(input('Digite sua idade: '))
    return idade

def salario() -> float:
    salario = float(input('Digite o seu salario maior que 0: '))
    while salario < 1:
        print('Digite um Salario maior que 0')
        salario = float(input('Digite o seu salario maior que 0: '))
    return salario

def sexo() -> str:
    sexo = input('Digite o seu sexo "f" ou "m" ').lower()
    while sexo != 'f' and sexo != 'm':
        salario = input('Digite o seu salario maior que 0: ')
        print('Sexo inválido. Digite f ou m.')
        sexo = input('Digite o sexo (f ou m): ')
    return sexo

def estado_civil() -> str:
    estado_civil = input("Digite o Estado civil 's', 'c', 'v', 'd' ").lower()
    while estado_civil not in ['s', 'c', 'v', 'd']:
        print('Estado civil inválido. Digite s (solteiro), c (casado), v (viúvo) ou d (divorciado).')
        estado_civil = input('Digite o seu estado civil: ')
    print('Você preencheu todos os requisitos. Nome: {}, idade: {}, salário: {}, sexo: {}, estado civil: {}'.format(nome(), idade(), salario(), sexo(), estado_civil))
    return estado_civil

# Uso das funções
nome_usuario = nome()
idade_usuario = idade()
salario_usuario = salario()
sexo_usuario = sexo()
estado_civil_usuario = estado_civil()
