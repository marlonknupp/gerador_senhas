import secrets
import string

def gerar_senha(tamanho=12, maiusculas=True, minusculas=True, simbolos=True, numeros=True):
    caracteres = ""

    if minusculas:
        caracteres += string.ascii_lowercase
    if maiusculas:
        caracteres += string.ascii_uppercase
    if simbolos:
        caracteres += string.punctuation
    if numeros:
        caracteres += string.digits

    if not caracteres:
        return "⚠️ Marque pelo menos uma opção!"

    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))
