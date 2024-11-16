# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "processamento de linguagem natural":
        return "habilidades de IA para entender e gerar linguagem humana"
    
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:                         
    elif conceito == "machine learning":
        return "permite que sistemas aprendam e melhorem a partir de dados"
        
    elif conceito == "visão computacional":
        return "capacidade da IA para interpretar e entender o mundo visual"
        
    elif conceito == "ia generativa":
        return "gera novos resultados a partir de dados existentes"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito".  
print(descrever_conceito(entrada))