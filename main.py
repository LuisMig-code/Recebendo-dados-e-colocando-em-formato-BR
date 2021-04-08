from cpf_cnpj import Documento
from telefonesBr import telefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco


ex_cnpj = '16975528000116'
ex_cpf = '61589964080'

documento = Documento.cria_documento(ex_cnpj)
print("CNPJ:" , documento)

documento2 = Documento.cria_documento(ex_cpf)
print("CPF:" , documento2)


telefone_obj = telefonesBr("9887954878")
print("Telefone:" , telefone_obj)


cadastro = DatasBr()
print(cadastro.tempo_cadastro())


cep = 65025001
obj_cep = BuscaEndereco(cep)

bairro , cidade , uf  = obj_cep.acessa_via_cep()

print(bairro,cidade,uf)
