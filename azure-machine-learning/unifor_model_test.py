import streamlit as st
import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

st.header("Predição de Valores de Imóveis")
st.divider()

regioes = {}
regioes['REGIONAL 1'] = 'VILA VELHA,JARDIM GUANABARA,BARRA DO CEARÁ,CRISTO REDENTOR,PIRAMBU,CARLITO PAMPLONA,JACARECANGA,JARDIM IRACEMA, FLORESTA,ÁLVARO WEYNE'
regioes['REGIONAL 2'] = 'MEIRELES,ALDEOTA,VARJOTA, PAPICU,DE LOURDES,CAIS DO PORTO, MUCURIPE,VICENTE PINZÓN,JOAQUIM TÁVORA, DIONÍSIO TORRES,SÃO JOÃO DO TAUAPE'
regioes['REGIONAL 3'] = 'QUINTINO CUNHA, OLAVO OLIVEIRA,ANTÔNIO BEZERRA, PADRE ANDRADE,PRESIDENTE KENNEDY,VILA ELLERY, MONTE CASTELO , SÃO GERARDO,FARIAS BRITO,PARQUE ARAXÁ, PARQUELÂNDIA, AMADEU FURTADO,RODOLFO TEÓFILO'
regioes['REGIONAL 4'] = 'JOSÉ BONIFÁCIO, BENFICA,FÁTIMA,DAMAS, JARDIM AMÉRICA, BOM FUTURO,MONTESE,ITAOCA, PARANGABA,VILA PERI,PARREÃO, VILA UNIÃO,AEROPORTO'
regioes['REGIONAL 5'] = 'GRANJA LISBOA, GRANJA PORTUGAL, BOM JARDIM, SIQUEIRA,BONSUCESSO'
regioes['REGIONAL 6'] = 'ALTO DA BALANÇA,AEROLÂNDIA,JARDIM DAS OLIVEIRAS, CIDADE DOS FUNCIONÁRIOS,PARQUE MANIBURA,PARQUE IRACEMA, CAMBEBA,MESSEJANA,JOSÉ DE ALENCAR, CURIÓ, GUAJERU,LAGOA REDONDA,COAÇU, SÃO BENTO,PAUPINA'
regioes['REGIONAL 7'] = 'PRAIA DO FUTURO I,PRAIA DO FUTURO II,COCÓ, CIDADE 2000,MANUEL DIAS BRANCO,SALINAS, GUARARAPES,LUCIANO CAVALCANTE,EDSON QUEIROZ, SAPIRANGA/COITÉ,SABIAGUABA'
regioes['REGIONAL 8'] = 'CASTELÃO, SERRINHA, ITAPERI,DENDÊ,DIAS MACÊDO, BOA VISTA, PARQUE DOIS IRMÃOS,PASSARÉ,PLANALTO AYRTON SENNA,PREFEITO JOSÉ WALTER'
regioes['REGIONAL 9'] = 'CAJAZEIRAS,BARROSO,CONJUNTO PALMEIRAS,JANGURUSSU,PARQUE SANTA MARIA, ANCURI,PEDRAS'
regioes['REGIONAL 10'] = 'PARQUE SÃO JOSÉ, NOVO MONDUBIM, CANINDEZINHO, CONJUNTO ESPERANÇA, PARQUE SANTA ROSA, PARQUE PRESIDENTE VARGAS,ARACAPÉ,MARAPONGA, JARDIM CEARENSE, MONDUBIM,VILA MANOEL SÁTIRO'
regioes['REGIONAL 11'] = 'PICI, BELA VISTA, PANAMERICANO, COUTO FERNANDES,DEMÓCRITO ROCHA,AUTRAN NUNES, DOM LUSTOSA, HENRIQUE JORGE, JÓQUEI CLUBE,JOÃO XXIII,GENIBAÚ, CONJUNTO CEARÁ I,CONJUNTO CEARÁ II'
regioes['REGIONAL 12'] = 'CENTRO, MOURA BRASIL,PRAIA DE IRACEMA'

left_column, right_column = st.columns(2)

with left_column:
    tipo_imovel = st.selectbox(
        'Selecione o tipo de imóvel',
        ['CASA', 'APARTAMENTO'])

    regiao = st.selectbox(
        'Selecione a região',
        regioes.keys())
    
    area = st.number_input("Área", value=57, placeholder="informe a área do imóvel")

    quartos = st.number_input("Número de Quartos", value=1, placeholder="informe o número de quartos")

    vagas = st.number_input("Número de Vagas", min_value=0, value=1, placeholder="informe o número de vagas")

    suites = st.number_input("Número de Suítes", min_value=0, value=1, placeholder="informe o número de suítes")

    banheiros = st.number_input("Número de Banheiros", min_value=0, value=1, placeholder="informe o número de banheiros")

    
valor_predito = 0

st.divider()

clicked = st.button("Executar predição", type="primary")
if clicked:
    
    data = {
        "input_data": {
            "columns": [
                "tipo",
                "area",
                "quartos",
                "vagas",
                "suites",
                "banheiros",
                "regiao"
            ],
            "index": [0],
            "data": [[tipo_imovel, area, quartos, vagas, suites, banheiros, regiao]]
        }
    }

    body = str.encode(json.dumps(data))

    # print(body)

    url = '[URL DO SERVIÇO DE PREDIÇÃO]'
    api_key = '[PRIMARY KEY]'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': ('Bearer ' + api_key)
    }

    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        # print(type(result))
        valor_predito = float(result.replace('[','').replace(']',''))
    except urllib.error.HTTPError as e:
        print("A requisição falhou: " + str(e.code))
        print(e.info())
        print(e.read().decode('utf-8', 'ignore'))

    # valor_predito = 100
    
with right_column:
    st.write(f"O valor predito para o imóvel na Região {regiao} é: {valor_predito:9.2f}")
