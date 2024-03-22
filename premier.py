# streamlit run premier.pys
import streamlit as st
import pandas as pd 
import plotly.express as px

@st.cache_data
def load():
    return pd.read_csv('premierleague.csv')

#main code starts here
df =load()


st.image('banner.webp',use_column_width=True)
st.title("Premier League Dashboard")
with st.expander("view raw premier league data"):
     st.dataframe(df.sample(10000))

rows, cols,=df.shape
c1,c2= st.columns(2)
c1.markdown(f'### total records :{rows}')
c2.markdown (f'### total columns :{cols}')

numeric_df = df.select_dtypes(include='number')
cat_df = df.select_dtypes(exclude='number')
with st.expander('column names'):
     st.markdown(f'column with number:{",".join(numeric_df)}')
     st.markdown(f'column without numbers:{",".join(cat_df)}')

# visualization 
     
c1,c2= st.columns([1,3])
xcol= c1.selectbox("choose a column for x-axis", numeric_df.columns)
ycol= c1.selectbox("choose a column for y-axis", numeric_df.columns)
zcol= c1.selectbox("choose a column for z-axis", numeric_df.columns)
color= c1.selectbox("choose a column for color", cat_df.columns)
fig= px.scatter_3d(df, x=xcol, y=ycol, z=zcol, color=color)
c2.plotly_chart(fig, use_container_width=True)
st.title("Whta is Preemier League")
c1,c2 = st.columns(2)
c1.video('https://www.youtube.com/watch?v=t5EhsXZwn4o&pp=ygUacHJlbWllciBsZWFndWUgaGlnaGxpZ2h0cyA%3D')
c2.markdown('The Premier League has a high standard of football and attracts the top football stars from around the world. More fans watch the Premier League in its stadiums than any other league in Europe and the good performance of its clubs in European football means that it is rated as the number one league in Europe. ')

st.title('Premier League Clubs')
clubs =df['HomeTeam'].unique()+ df['AwayTeam'].unique()
clubs = sorted(set(clubs))
st.info(",".join(clubs))