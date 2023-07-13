import pandas as pd
import numpy as np
import streamlit as st
from dice_role import roller
import statistics
import seaborn as sns
import altair as alt

# -- Set page config
apptitle = 'About Page'
st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")

# Title the app
st.title('Dice Roller')

st.markdown(
    """
    This is a Dice Rolling Simulator.
    """
)

dice_roles = st.sidebar.selectbox(
    'Number of dice?',
    (1,2,3,4,5,6,7,8,9,10))

sides_of_dice = st.sidebar.selectbox(
    'Number of sides?',
    (4,6,8,10,12,20))

modifier = st.sidebar.selectbox(
    'Modifiers?',
    (0,1,2,3,4,5,6,7,8,9,10))

simulations = st.sidebar.selectbox(
    'Number of simulations?',
    (10,100,500,1000,2000,5000))

limit = st.sidebar.number_input('Number to beat (Limit)?')

disable_histogram = st.sidebar.checkbox("Disable histogram", key="disable")

enable_normal_dis = st.sidebar.checkbox("Enable noraml distribution", key="noraml")

enable_limit = st.sidebar.checkbox("Enable limit", key="limit")

list_rolls = roller(dice_roles, sides_of_dice, simulations, modifier)

df_rolls = pd.DataFrame(list_rolls, columns =['roll_values'])

above_df_rolls = df_rolls[df_rolls.roll_values > limit]
below_df_rolls = df_rolls[df_rolls.roll_values <= limit]

above_limit_count = above_df_rolls.roll_values.count()
below_limit_count = below_df_rolls.roll_values.count()

win_ratio = above_limit_count / simulations
loose_ratio = below_limit_count / simulations

st.sidebar.markdown(
    f'{dice_roles}d{sides_of_dice} + {modifier}  \n \
    Min: {df_rolls.roll_values.min()}  \n \
    Max: {df_rolls.roll_values.max()}  \n \
    Mean (mu): {df_rolls.roll_values.mean():.3}  \n \
    Stdev (sigma): {df_rolls.roll_values.std():.3}  \n \
    Outcomes Above Limit: {above_limit_count}  \n \
    Outcomes Below Limit: {below_limit_count}  \n \
    Win Percentage: {win_ratio:.3%}  \n \
    Lose Percentage: {loose_ratio:.3%}'
)

bar = alt.Chart(df_rolls).mark_bar().encode(
    x=alt.X("roll_values", bin=alt.Bin(extent=[1, (df_rolls.roll_values.max()+1)], step=1)),
    y='count()',
)

rule = alt.Chart(df_rolls).mark_rule(color='red').encode(
    x='mean(roll_values)'
)

mu = df_rolls.roll_values.mean()
sigma = df_rolls.roll_values.std()
x = np.arange(df_rolls.roll_values.max()+1)

source = pd.DataFrame({
  'x': x,
  'f(x)': 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2)) * simulations
})

norm_dis = alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)',
    color=alt.value("#000000")
)

x = np.arange(limit+1)

source = pd.DataFrame({
  'x': x,
  'f(x)': 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2)) * simulations
})

area_norm_dis_red = alt.Chart(source).mark_area(color = 'red',
                           opacity = 0.5,
                           line = {'color':'darkred'}).encode(
    x='x',
    y='f(x)'
)

if disable_histogram:
    if enable_normal_dis:
        if enable_limit:
            chart = (norm_dis + area_norm_dis_red + rule).properties(width=1200)
        else:
            chart = (norm_dis + rule).properties(width=1200)
    else:
        if enable_limit:
            chart = (area_norm_dis_red + rule).properties(width=1200)
        else:
            chart = (rule).properties(width=1200)
        
else:
    if enable_normal_dis:
        if enable_limit:
            chart = (bar + norm_dis + area_norm_dis_red + rule).properties(width=1200)
        else:
            chart = (bar + norm_dis + rule).properties(width=1200)
    else:
        if enable_limit:
            chart = (bar + area_norm_dis_red + rule).properties(width=1200)
        else:
            chart = (bar + rule).properties(width=1200)

st.altair_chart(chart, theme="streamlit", use_container_width=True)

