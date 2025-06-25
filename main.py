import csv
from pathlib import Path
import string
import locale
from random import SystemRandom as Sr

CAMINHO_ARQUIVO_TEMPLATE = Path(__file__).parent / 'fatura.txt'
CAMINHO_ARQUIVO_CSV = Path(__file__).parent / 'clientes.csv'
PASTA_SAIDA = Path(__file__).parent / 'faturas'

locale.setlocale(locale.LC_ALL, '')

PASTA_SAIDA.mkdir(exist_ok=True)

def converter_brl(valor: float):
    brl = 'R$ ' + locale.currency(valor, symbol=False, grouping=True)
    return brl

with open(CAMINHO_ARQUIVO_TEMPLATE, 'r', encoding='latin1') as f:
    texto_template = f.read()

template = string.Template(texto_template)

with open(CAMINHO_ARQUIVO_CSV, 'r',encoding='utf-8') as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        valor_float = float(linha['valor'])
        valor_formatado = converter_brl(valor_float)
        linha_formatada = dict(linha)
        linha_formatada['valor'] = valor_formatado
        mensagem = template.safe_substitute(linha_formatada)
        print(mensagem)
        print('---------------------------------------')

        id_ = Sr().choices(string.ascii_letters + string.digits, k=3)
        nome_cliente = linha_formatada['nome'].replace(' ', '_').lower()
        nome_arquivo = PASTA_SAIDA / f'fatura_{nome_cliente}_{id_}.txt'

        with open(nome_arquivo, 'w',encoding='utf-8') as arquivo_faturas:
            arquivo_faturas.write(mensagem)

        print(f'Fatura Criada: {nome_arquivo}')










