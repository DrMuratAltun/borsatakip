import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
from io import BytesIO


symbol = st.sidebar.text_input('Hisse Senedi Sembolü', value='ASELS')

st.title(symbol + ' Hisse Senedi Grafiği')


start_date = st.sidebar.date_input('Başlangıç Tarihi', value=datetime(2020, 1, 1))
end_date = st.sidebar.date_input('Bitiş Tarihi', value=datetime.now())


df = yf.download(symbol + '.IS', start=start_date, end=end_date)


st.subheader('Hisse Senedi Fiyatları')
st.line_chart(df['Close'])


st.subheader('Hisse Senedi Verileri')
st.write(df)


st.subheader('Veriyi İndir')
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=True, sheet_name='Sheet1')
    writer.close()  
    processed_data = output.getvalue()
    return processed_data

excel_data = to_excel(df)
st.download_button(label='Excel Olarak İndir', data=excel_data, file_name=f'{symbol}_data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
