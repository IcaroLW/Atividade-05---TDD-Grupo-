import re

class ValidadorSenha:
    def validar(self, senha: str):
        erros = []

        if len(senha) < 8:
            erros.append("A senha deve ter pelo menos 8 caracteres")

        if len(re.findall(r'\d', senha)) < 2:
            erros.append("A senha deve conter pelo menos 2 dígitos")

        if not re.search(r'[A-Z]', senha):
            erros.append("A senha deve conter pelo menos uma letra maiuscula")

        if not re.search(r'[!@#$%^&*(),.?\":{}|<>_\[\]\\/\-+=;\'`~]', senha):
            erros.append("A senha deve conter pelo menos um caractere especial")

        return {
            "valida": len(erros) == 0,
            "erros": erros
        }
