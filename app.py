import streamlit as st
import numpy as np
import pandas as pd 

dados = []

def main():
    dados = []
    linhas = st.number_input("Nº de linhas: ", value = 1) 
    
    b1, b2 = st.beta_columns(2)
    col1, col2, col3 = st.beta_columns(3)

    botao = b1.button("Calcular média")

    dados = []

    for i in range(0,int(linhas)):
        dados.append([
            col1.number_input(f"Valor do inicio do intervalo: ", key=f"in{i}"),
            col2.number_input(f"Valor do final do intervalo: ", key=f"fm{i}"),
            col3.number_input(f"Valor da frequência: ", key=f"fq{i}"),
            'Nan'
        ])
    
    if botao:
        df = pd.DataFrame(dados,columns=["Inicio do intervalo", "Final do intervalo", "Frequência", 'media'])
        df['media'] = df.apply(lambda x: ((x["Inicio do intervalo"]+x["Final do intervalo"])/2)*x["Frequência"], axis=1)
        try: 
            resultado = df['media'].sum()/df['Frequência'].sum()
            b2.markdown(f"Média Aritmética dos Intervalos: **{resultado}**")
            st.markdown(f"Média Aritmética dos Intervalos: **{resultado}**")
        except:
            b2.markdown("Há algo errado com seus dados!")


if __name__ == "__main__":
    main()