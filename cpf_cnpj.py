import validate_docbr


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)

        elif len(documento) == 14:
            return DocCnpj(documento)

        else:
            raise ValueError("Quantidade de dígitos incorreta")

class DocCpf:
    def __init__(self,documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF INVÁLIDO")


    def valida(self,documento):
        validacao = validate_docbr.CPF()
        validacao = validacao.validate(documento)

        return (validacao)

    def format(self):
        mascara = validate_docbr.CPF()
        mascara = mascara.mask(self.cpf)

        return mascara

    def __str__(self):
        return self.format()



class DocCnpj:
    def __init__(self,documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ INVÁLIDO")


    def valida(self,documento):
        validacao = validate_docbr.CNPJ()
        validacao = validacao.validate(documento)
        
        return (validacao)

    def format(self):
        mascara = validate_docbr.CNPJ()
        mascara = mascara.mask(self.cnpj)

        return mascara

    def __str__(self):
        return self.format()
