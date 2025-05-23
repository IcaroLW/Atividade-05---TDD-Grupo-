import re

class ValidadorSenha:
    def validar(self, senha: str):
        erros = []
        erros.extend(self._validar_tamanho(senha))
        erros.extend(self._validar_digitos(senha))
        erros.extend(self._validar_maiuscula(senha))
        erros.extend(self._validar_especial(senha))
        
        return {
            "valida": len(erros) == 0,
            "erros": erros
        }

    def _validar_tamanho(self, senha):
        return ["A senha deve ter pelo menos 8 caracteres"] if len(senha) < 8 else []

    def _validar_digitos(self, senha):
        return ["A senha deve conter pelo menos 2 dígitos"] if len(re.findall(r'\d', senha)) < 2 else []

    def _validar_maiuscula(self, senha):
        return ["A senha deve conter pelo menos uma letra maiuscula"] if not re.search(r'[A-Z]', senha) else []

    def _validar_especial(self, senha):
        return ["A senha deve conter pelo menos um caractere especial"] if not re.search(r'[!@#$%^&*(),.?\":{}|<>_\[\]\\/\-+=;\'`~]', senha) else []
=======

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

