def verificar_letra_a(string):

    string_lower = string.lower()
    
    count_a = string_lower.count('a')
    
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

entrada = input("Informe uma string: ")

verificar_letra_a(entrada)
