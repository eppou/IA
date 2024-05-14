import numpy as np

# Função de ativação (utilizaremos a função sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada da função de ativação
def sigmoid_derivative(x):
    return x * (1 - x)

# Dados de entrada e saída para a função lógica XOR
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Inicialização dos pesos
np.random.seed(1)
input_weights = np.random.random((2, 2))  # Pesos entre a camada de entrada e a camada oculta
output_weights = np.random.random((2, 1)) # Pesos entre a camada oculta e a camada de saída

# Execução do algoritmo por duas épocas (cada uma com 4 iterações)
epochs = 2
for epoch in range(epochs):
    print("Época:", epoch+1)
    for iteration in range(4):
        # Forward Propagation
        input_layer = X[iteration]
        hidden_layer_input = np.dot(input_layer, input_weights)
        hidden_layer_output = sigmoid(hidden_layer_input)

        output_layer_input = np.dot(hidden_layer_output, output_weights)
        output = sigmoid(output_layer_input)

        # Cálculo do erro
        error = y[iteration] - output

        # Backpropagation
        # Parte 1: Cálculo do gradiente na camada de saída
        output_delta = error * sigmoid_derivative(output)

        # Parte 2: Propagação do erro para a camada oculta
        hidden_error = output_delta.dot(output_weights.T)
        hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)

        # Atualização dos pesos
        output_weights += hidden_layer_output.reshape(2,1) * output_delta
        input_weights += input_layer.reshape(2,1) * hidden_delta

        # Print do erro a cada iteração
        print("Erro na iteração {}: {:.5f}".format(iteration+1, np.mean(np.abs(error))))

# Teste da rede neural treinada
print("\nTeste da rede neural treinada:")
for i in range(4):
    input_layer = X[i]
    hidden_layer_input = np.dot(input_layer, input_weights)
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, output_weights)
    output = sigmoid(output_layer_input)

    print("Entrada:", input_layer, "Saída:", output)
