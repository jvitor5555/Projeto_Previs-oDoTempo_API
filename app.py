def NomeCidade()->str:
    
    print(60*"-")
    print("Insira os acentos corretamente e use apenas letras mínusculas")
    print(60*"-")
    cidade = str(input("Informe o nome da cidade procurada: \n"))
    
    nomecidade = cidade.lower()
    
    return nomecidade
    

def EntradaPais ()->str:
          
    entrada = str(input("Informe a sigla do páis - exemplo - 'BR' para Brásil \n"))
            
    pais = entrada.upper()
    
    return pais
            
          
def clima()->str:
    
    import requests
    
    nome_cidade = NomeCidade()
    
    nome_pais  = EntradaPais()
    
    chave_api = '3c81d4265b989ef7b4dbe86b272b9670'
    
    lang = 'pt_br'
    
    link = f"https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={chave_api}&lang={lang}"
    
    conversao = 273.15
    
    requisicao = requests.get(link)
    
    requisicao_dicionario = requisicao.json()
    
    descricao = requisicao_dicionario["weather"][0]["description"]
    
    temperatura = requisicao_dicionario["main"]["temp"] - conversao
    
    validacao_pais = requisicao_dicionario["sys"]["country"] 
    validacao_cidade = requisicao_dicionario["name"]
    
    validacao_cidade_formatado = validacao_cidade.lower()
    
    if validacao_pais == nome_pais or validacao_cidade_formatado == nome_cidade:
        resultado = f"O clima na cidade {nome_cidade} é de {temperatura:.2f} °C e o dia terá ou será {descricao} --- Sigla do páis - {validacao_pais}"
        return resultado
    else:
        print("Cidade ou país inválido")
        

if __name__ == '__main__':
    clima() 