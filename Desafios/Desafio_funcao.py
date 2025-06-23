# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input("Digite os dados do paciente").strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# Função para definir a prioridade2
def atendimento(pacientes):
    nome, idade, status = pacientes
    urgente = "urgente" in status
    return(0 if urgente else 1,-idade)

# Ordena os pacientes de acordo com a prioridade e mantém ordem de chegada entre iguais
pacientes_ordenados = sorted(pacientes, key=atendimento)

# Extrai apenas os nomes para exibir
nomesPacientes = [paciente[0] for paciente in pacientes_ordenados]

# Exibe o resultado
print("Ordem de Atendimento:", ", ".join(nomesPacientes))
