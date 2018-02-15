import glob
import os
import time

from selenium.webdriver import Chrome, ChromeOptions


ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
       "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
       "SP", "SE", "TO"]


def set_driver(download_dir):
    options = ChromeOptions()
    prefs = {"download.default_directory": download_dir}
    options.add_experimental_option("prefs", prefs)
    options.experimental_options
    driver = Chrome(options=options)
    return driver


def download_data(sigla_uf):
    URL = ('https://sistemas.anatel.gov.br/stel/consultas/'
           'ListaEstacoesLocalidade/tela.asp?pNumServico=010&'
           f'pSiglaUF={sigla_uf}&acao=C&hdnImprimir=true&excel=true')
    driver.get(URL)
    print(f'{sigla_uf} - Iniciando download...')
    while True:
        download_finished = glob.glob('../data/Consulta.xls') != []
        if download_finished:
            time.sleep(1)
            break

    print('Download finalizado.')
    os.rename('../data/Consulta.xls', f'../data/{sigla_uf}.html')


download_dir = os.path.join(os.path.dirname(os.getcwd()), 'data')
driver = set_driver(download_dir)

for uf in ufs:
    download_data(uf)

driver.quit()
