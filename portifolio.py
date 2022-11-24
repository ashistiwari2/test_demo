import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
from datetime import datetime
from PIL import Image
import requests
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from pathlib import Path
import folium
import branca
import folium.plugins
from streamlit_folium import folium_static
import pandas as pd
from branca.element import Figure
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap

st.set_page_config(layout='wide', page_title="Curriculum Vitae Ashis", page_icon="🌎")

over_theme = {
    'txc_inactive': '#D1E1E1',
    'menu_background':'#024949',
    'txc_active':'#024949',
    'option_active':'#D1E1E1'
    }
font_fmt = {
    'font-class':'h2',
'font-size':'150%'
}

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir  / "style" / 'style.css'
resume_file = current_dir / "assets" / "Currículo_Alan.pdf"
profile_pic = Image.open("./assets/image5.png")
image0 = Image.open("./assets/lateral2.png")
pdf_file = current_dir / "assets" / "Currículo_Alan.pdf"


titulo_pagina = 'Curriculum Vitae | Ashis Tiwari'
icone_pagina = ':wave:'
nome = '## Ashis Tiwari'
descricao = '''
**Senior Analyast EY** | 
Investor in crypto \n Holder of UMA,SNX,VIDT DAO| B.tech Graduate in Computer Science and Engineering
'''
idade = '24 anos'
cidade = 'Atualmente em Mogi Guaçu - SP'
email = 'alaneleuteriocg@gmail.com'

PAGE_TITLE = "Curriculum Vitae | Ashis Tiwari"
NAME = '## Ashis Tiwari'
DESCRIPTION = 'Geográfo'
EMAIL = 'alaneleuteriocg@gmail.com'


with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()


col1, col2 = st.columns(2)
with col1:
     st.image(profile_pic, width=400)
with col2:
     st.write(NAME)
     st.write(descricao)
     st.write(cidade)
     st.download_button(
          label= "Download Currículo",
          data= PDFbyte,
          file_name= pdf_file.name,
          mime= 'application/octet-stream')


with st.container ():
    column1, column2, column3, column4 = st.columns(4)
    with column1:
          st.write('[Instagram](https://www.instagram.com/geotif.py)')
    with column2:
         st.write('[Linkedin](https://www.linkedin.com/in/alan-dos-santos-eleuterio)')
    with column3:
         st.write('[Github](https://github.com/alanseleuterio)')
    with column4:
         st.write('[G-mail](https://mailto:alaneleuteriocg@gmail.com)')

    st.write('---')

col11, col22 = st.columns(2)
with col11:
          st.write(':world_map: **SOLUÇÕES EM AMBIENTE SIG**')
          st.write('''
          - Microplanejamento florestal; \n
          - Plano de manejo florestal; \n
          - Macroavaliação de ativos florestais; \n
          - Aplicativos em plataforma Google Earth Engine (javascript); \n
          - Tratamento de dados em python ; \n
          - Levantamentos remotos e/ou in loco; \n
          - Licenciamentos ambiental; \n
          - Laudos ambientais; \n
          - Georreferenciamento de imóveis rurais e urbanos.
          
          ''')
with col22:
          st.write(':file_folder: **EXPERIÊNCIA NOS SOFTWARES**')
          st.write('''
          - QGIS - Avançado; \n
          - ArcGis - Avançado; \n
          - Laudos ambientais; \n
          - Plano de manejo Florestal; \n
          - AutoCAD - Intermediário;; \n
          - Pacote Office (Word, Excel, PowerPoint) - Avançado; \n
          - Spring - Avançado; \n
          - CorelDraw - Avançado.
          ''')


with st.container ():
    st.write('---')
    st.write('#')
    st.write('**HISTÓRICO PROFISSIONAL**')

    st.write(':white_check_mark: **MTL Comercio E Reciclagem De Madeira** ***(06/2022  -  Tempos atuais)*** **| Mogi Guaçu / SP**')
    st.write('''
            - Analista de Geoprocessamento e Controle Florestal \n
            - Avaliação de silvicultura em ambiente SIG, elaboração de microplanejamento florestal e mapas temáticos. Uso de linguagem de programação JavaScript e python aplicado a soluções de plantio e automatização de processos. Uso de ferramentas de gestão de etapas de colheita e transporte florestal.
            ''')

    st.write(':white_check_mark: **Innovatech Gestão** ***(07/2021  -  06/2022)*** **| Campinas / SP**')
    st.write('''
            - Analista de Geoprocessamento \n
            - Gerenciamento e avaliação de silvicultura em ambiente SIG, avaliação de elaboração de mapas temáticos, uso de linguagem de programação JavaScript e python aplicado à soluções de plantio e automatização de processos.
            ''')

    st.write(':white_check_mark: **Deméter Engenharia (DMTR)** ***(07/2020  -  07/2021)*** **| Campo Grande / MS**')
    st.write('''
            - Apoio técnico (Geógrafo) \n
            - Práticas em georreferenciamento, vetorização de matrículas rurais e urbanas, elaboração de cartas temáticas de caráter técnico, Elaboração de planos de gestão de resíduos sólidos e apoio técnico na elaboração e tratamento de dados SIG, planilhas e textos.
            ''')

    st.write(':white_check_mark: **IBGE - Agente de pesquisa da PNAD-Contínua** ***(06/2018  -  06/2020)*** **| Campo Grande / MS**')
    st.write('''
            - Pesquisas de campo em centros urbanos e rurais da Pesquisa Nacional por Amostragem Domiciliar Contínua.
            ''')

    st.write(':white_check_mark: **Deméter Engenharia (DMTR)** ***(02/2014  -  10/2014)*** **| Campo Grande / MS**')
    st.write('''
            - Estágio obrigatório \n
            - Práticas em georreferenciamento, vetorização de matrículas rurais e urbanas, elaboração de cartas temáticas de caráter técnico, apoio técnico na elaboração e tratamento de dados SIG, planilhas e textos.
            ''')

    st.write(':white_check_mark: **Estágio não obrigatório (UFMS)** ***(07/2016  -  12/2016)*** **| Campo Grande / MS**')
    st.write('''
            - Laboratório de Topografia \n
            - Práticas de levantamento topográfico e tratamento de imagens de satélite
            ''')
     

with st.container ():
    def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
            <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="alan-dos-santos-eleuterio" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://br.linkedin.com/in/alan-dos-santos-eleuterio?trk=profile-badge"></a></div>""", 'medium':"""<div style="overflow-y: auto; height:540px;"> <div id="retainable-rss-embed" 
    data-rss="https://medium.com/feed/retainable,https://medium.com/feed/data-science-in-your-pocket"
    <div class="badge-base LI-profile-badge" 
    data-locale="pt_BR" 
    data-size="large" 
    data-theme="light" 
    data-type="HORIZONTAL"
    data-maxcols="3" 
    data-layout="grid"
    data-poststyle="inline" 
    data-readmore="Read the rest" 
    data-buttonclass="btn btn-primary" 
    data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""}
    with st.sidebar:
            components.html(embed_component['linkedin'],height=335)
            st.image(image0)


with st.container ():
    html1 = """
        <center><h3 style=font-family:arial; font-size: 5px>MTL COMÉRCIO E RECICLAGEM DE MADEIRA</h3> </center>
        <center><p style=font-family:arial; align=justify>Avaliação de florestas de eucalipto utilizando geoprocessamento, elaboração de microplanejamento florestal e mapas de transporte. Uso de linguagem de programação JavaScript e Python aplicado a soluções de controle e automatização de processos.
        </p></center>
        <center><h4 style="margin-bottom:1"; font-family:arial; width="300px"></h4></center>
        <center><img src=https://media-exp1.licdn.com/dms/image/C4D22AQEWkM7ckCMDTw/feedshare-shrink_480/0/1652443224307?e=1669852800&v=beta&t=v-y1l2UpAnm6ApS1nXa7fqJh9JE2fcrW9RlJ4xO8l7M alt="logo" width=330 height=200 ></center>
        <center><h5 style="margin-bottom:0"; width="100px"></h5></center>
        """
    html2 = """
        <center><h3 style=font-family:arial>INNOVATECH GESTÃO</h3> </center>
        <center><p style=font-family:arial; align=justify>Elaboração de materiais técnicos no setor florestal utilizando geoprocessamento, estudos de prospecção, uso de linguagem de programação JavaScript e Python aplicado à soluções de plantio e automatização de processos.
        </ul> </p></center>
        <center><h4 style="margin-bottom:1"; font-family:arial; width="300px"></h4></center>
        <center><img src=https://innovatechgestao.com.br/wp-content/uploads/2020/06/imagem.png alt="logo" width=330 height=200 ></center>
        <center><h5 style="margin-bottom:0"; width="100px"></h5></center>
        """
    html3 = """
        <center><h3 style=font-family:arial>IBGE</h3> </center>
        <center><p style=font-family:arial; align=justify>Levantamentos de campo em centros urbanos e rurais da Pesquisa Nacional por Amostragem Domiciliar Contínua.
        </ul> </p></center>
        <center><h4 style="margin-bottom:1"; font-family:arial; width="300px"></h4></center>
        <center><img src=https://www.infoescola.com/wp-content/uploads/2008/02/IBGE.png alt="logo" width=350 height=100 ></center>
        <center><h5 style="margin-bottom:0"; width="100px"></h5></center>
        """

    html4 = """
        <center><h3 style=font-family:arial>DEMÉTER ENGENHARIA</h3> </center>
        <center><p style=font-family:arial; align=justify>Práticas em georreferenciamento, vetorização de matrículas rurais e urbanas, cartas temáticas de caráter técnico. Elaboração de planos de gestão de resíduos sólidos e apoio técnico na elaboração e tratamento de dados SIG, planilhas e textos.
        </ul> </p></center>
        <center><h4 style="margin-bottom:1"; font-family:arial; width="250px"></h4></center>
        <center><img src=https://static.wixstatic.com/media/81c949_c34b6cd805c24da0ae52d2141d0901f1~mv2.png/v1/fill/w_240,h_108,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/81c949_c34b6cd805c24da0ae52d2141d0901f1~mv2.png alt="logo" width=280 height=130 ></center>
        <center><h5 style="margin-bottom:0"; width="100px"></h5></center>
        """

    st.write('---')

    st.write(' **MAPA DE HISTÓRICO PROFISSIONAL**')   

    coordinates1 = [
        [-22.3416565,-46.9702272],
        [-22.8194161,-47.0360758],
        [-20.4622047,-54.6150677],
        [-20.4406755,-54.5869773]
    ]

    coordinates = [
        [-22.3416565,-46.9702272],
        [-22.8194161,-47.0360758],
        [-20.4622047,-54.6150677],
        [-20.4406755,-54.5869773]
    ]

    coordinates2 = [
        [-22.3416565,-46.9702272],
        [-22.8192375,-47.035235],
        [-20.462136,-54.6150181],
        [-20.4408588,-54.5869292]
    ]

    m = folium.Map(location=[-21.1663553,-50.0863553], tiles="Cartodb Positron", zoom_start=6,control_scale=True, height=500)

    marker_cluster = MarkerCluster().add_to(m)
    iframe = branca.element.IFrame(html=html1, width=450, height=430)
    popup = folium.Popup(iframe, max_width=440)
    folium.Marker(
        location=[-22.3416565,-46.9702272],
        popup=popup,
        icon=folium.Icon(color="green", icon="ok-sign"),).add_to(marker_cluster)

    iframe1 = branca.element.IFrame(html=html2, width=420, height=400)
    popup1 = folium.Popup(iframe1, max_width=410)    
    folium.Marker(
        location=[-22.8192375,-47.035235],
        popup=popup1,
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(marker_cluster)

    iframe2 = branca.element.IFrame(html=html3, width=420, height=260)
    popup2 = folium.Popup(iframe2, max_width=420)    
    folium.Marker(
        location=[-20.462136,-54.6150181],
        popup=popup2,
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(marker_cluster)

    iframe3 = branca.element.IFrame(html=html4, width=420, height=370)
    popup3 = folium.Popup(iframe3, max_width=420)    
    folium.Marker(
        location=[-20.4408588,-54.5869292], 
        popup=popup3,
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(marker_cluster)


    folium.PolyLine(
        locations=coordinates1,
        color="#BFBFBF",
        weight=3,
        tooltip="Rota",
    ).add_to(m)

    folium.PolyLine(
        locations=coordinates,
        dash_array='5',
        color="#909090",
        weight=1,
        tooltip="Rota",
    ).add_to(m)

    folium_static(m)

with st.container ():
    st.write('---')
    st.write('#')
    st.write('**HISTÓRICO ACADÊMICO**')

    st.write(':trophy: **GEOGRAFIA BACHARELADO (2016 - 2020) | Universidade Federal do Mato Grosso do Sul (UFMS) — Nível Superior completo.**')
    st.write('''
            Geoprocessamento, Sensoriamento Remoto, Estatística e Ciências Sociais.
            ''')

    st.write(':trophy: **PÓS GRADUAÇÃO EM GEOPROCESSAMENTO (2022 - 2023) |** **Unyleya — Graduando**')
    st.write('''
            Geoprocessamento aplicado, banco de dados geográficos, sensoriamento remoto e vants, processamento de dados geográficos.
            ''')
