import re

# Ask the user to input their CPF (Brazilian ID number)
cpf = input('Insira seu cpf: ')

# Function to remove all non-digit characters from the CPF string
def formatar_cpf(cpf):
    return re.sub(r'\D', '', cpf)

# Function to verify the validity of a CPF number
def verificarCpf(cpf):
    cpfFormatado = formatar_cpf(cpf)  # Format the CPF by removing non-digit characters
    
    # CPF should have 11 digits after formatting
    if len(cpfFormatado) == 11:
        
        # Begin the calculation of the first verification digit
        i = 10
        soma = 0
        
        # Remove the last two digits (verification digits) from CPF
        cpfFormatadoSemVerificador = cpfFormatado[:-2]
        
        # Loop through each digit and multiply by a decrementing weight (10 to 2)
        for numero in cpfFormatadoSemVerificador:
            numero = int(numero)  # Convert the string digit to an integer
            soma = soma + (numero * i)
            i -= 1

        # Calculate the remainder of the division by 11
        resto = soma % 11
        verificador = 11 - resto  # Determine the first verification digit

        # Check if the calculated first verification digit matches the CPF's first verification digit
        if cpfFormatado[-2] == str(verificador): 
            print('Primeiro dígito verificador verificado')
            
            # Begin the calculation for the second verification digit
            cpfFormatadoSemVerificador2 = cpfFormatado[:-1]
            j = 11
            soma2 = 0
            
            # Loop through each digit (including the first verification digit) and multiply by a decrementing weight (11 to 2)
            for numero2 in cpfFormatadoSemVerificador2:
                numero2 = int(numero2)
                soma2 = soma2 + (numero2 * j)
                j -= 1

            # Calculate the second verification digit
            resto2 = soma2 % 11
            verificador2 = 11 - resto2

            # Check if the second verification digit matches
            if cpfFormatado[-1] == str(verificador2):
                print('Segundo dígito verificador verificado')               
                return True
            
            # Special case where the second verification digit should be '0' if the calculated value is greater than 10
            else:
                if verificador2 > 10 and cpfFormatado[-1] == '0':
                    print('Segundo dígito verificador verificado!')
                    return True
                else:
                    return False
                
        # Special case where the first verification digit should be '0' if the calculated value is greater than 10
        else:
            if verificador > 10 and cpfFormatado[-2] == '0':
                print('Primeiro dígito verificador verificado!')
                return True
            else:
                return False
    
    # If CPF is not 11 digits long, it is not valid
    else:
        return False

# Check if the CPF is valid and print a confirmation message
if verificarCpf(cpf):
    print('CPF VERIFICADO!')

# If the CPF is invalid, prompt the user to try again
else:
    print('Isso não é um CPF válido, tente novamente')
