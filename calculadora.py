def calculator():
  # Obtém os valores de entrada do usuário
  num1 = float(input('Enter the first number: '))
  num2 = float(input('Enter the second number: '))

  # Obtém a operação desejada do usuário
  operation = input('Enter the operation (+, -, *, /): ')

  # Realiza a operação e exibe o resultado
  if operation == '+':
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
  elif operation == '-':
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
  elif operation == '*':
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
  elif operation == '/':
    result = num1 / num2
    print(f'{num1} / {num2} = {result}')
  else:
    print('Invalid operator')

# Chamada da função calculator
calculator()