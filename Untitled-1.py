def fibonacci(num):
    seq = [0, 1]
    while (num > seq[-1]):
        seq.append(seq[-1] + seq[-2])
    if (num == seq[-1]):
        return "Numero pertecente a sequencia" + str(seq) 
    return "Numero n pertecente a sequencia"


def inverter_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

string_invertida = inverter_string(input("Digite uma string: "))
print(string_invertida)
print(fibonacci(int(input("Digite um numero: "))))

