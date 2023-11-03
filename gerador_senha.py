import string
import 

def gerar_senha(tamanho=15):
     = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso para gerar uma senha de tamanho 12
senha_gerada = gerar_senha()
print("Senha gerada:", senha_gerada)
