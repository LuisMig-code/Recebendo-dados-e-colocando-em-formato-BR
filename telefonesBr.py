import re

class telefonesBr:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Número Incorreto")

    def valida_telefone(self,telefone):
                # colocamos com código do país não sendo obrigatório com o elemento "?"
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

        resposta = re.findall(padrao,telefone)

        #o método "findall" retorna uma lista , se houver elementos , ele retorna True , caso o contrário , retorna False
        if resposta:
            return True
        else :
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,self.telefone)

        # ASO O USUARIO NÃO DIGITE O CÓDIGO DO PAÍS , VAMOS CONSIDERÁ-LO COMO +55
        if resposta.group(1) == None:
            codigo_do_pais = "55"
        else :
            codigo_do_pais = resposta.group(1)

        numero_formatado = "+{} ({})({})-({})".format(
            codigo_do_pais,
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )

        return numero_formatado

    def __str__(self):
        return self.format_numero()
