def main():
    # n = int(input("Digite o numero de paginas: "))
    # matrix = []
    # print("Digite a matriz de adjacencia, separando os números por espaço:")
    # for i in range(n):
    #     # Lê a linha como uma string, divide em espaços, converte para inteiros e adiciona à matriz
    #     linha = list(map(int, input(f"Digite a linha {i+1}: ").split()))
    #     matrix.append(linha)

    

    matrix = [
        [0,1,1,1],
        [1,0,0,0],
        [0,1,0,1],
        [1,1,0,0]
    ]

    n = len(matrix) #Quantidade de paginas

    #Normaliza matriz de adjacencia
    for i in range(n):
        row_sum = sum(matrix[i])
        for j in range(n):
            if matrix[i][j]>0:
                matrix[i][j] = 1/row_sum

    # Atualiza page_rank até estabilizar
    precisao = 3
    page_rank = [1/n] * n
    suporte_vet = [0] * n
    count = 0

    while True:
        print(f"Iteração: {count+1}")
        for i in range(n): 
            
            suporte_vet[i] = 0  # Reinicia suporte_vet para a nova iteração
            for j in range(n):
                if matrix[j][i] > 0:
                    suporte_vet[i] += round(page_rank[j] * matrix[j][i],precisao)
            suporte_vet[i] = round(suporte_vet[i],precisao)
        
        print(f"{page_rank} , {suporte_vet}")
        count+=1

        if page_rank == suporte_vet:
            break  # Sai do loop se page_rank estabilizou
        
        page_rank = suporte_vet.copy()  # Atualiza page_rank para a próxima iteração
        

    for i in range(len(page_rank)):
        print(f"PageRank da página {i+1} = {page_rank[i]:.2f}")
    
main()

