import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
# Diplay data
st.title("Introduction to streamlit") # title
st.write("Dataframe") # text

df = pd.DataFrame({
    "one" : [1, 2, 3, 4], 
    "two" : [10, 20, 30, 40]
})

st.write(df) # df (Dynamic table)
st.dataframe(df.style.highlight_max(axis = 0)) # dynamic table
st.table(df) # visualize static table

### Ref: Display text
# markdown
"""
# Chapter
## Section
### subsection

```python
# Diplay code
import pandas as pd

```

"""

### Ref : Display chart
df_var = pd.DataFrame(
    np.random.rand(100, 3), 
    columns = ["a", "b", "c"]

)

st.write("Random number")
st.dataframe(df_var)
st.line_chart(df_var)

st.area_chart(df_var)

st.bar_chart(df_var)

# map near Sinjuku
df_map = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70], 
    columns = ["lat", "lon"]
)

st.map(df_map)


st.write("Interactice Widgets")

# Ref : Display interactive widgets
# Interactive
# check bok
if st.checkbox("Show images"):
    
    # Ref : Displat media
    st.write("Display images")

    img = Image.open("/Volumes/GoogleDrive/マイドライブ/Room_of_Oya/SuMiTab/大屋太志_オオヤタイシ.jpg")
    st.image(img, caption="Taishi Oya", use_column_width=True)

# define variable
option = st.selectbox(
    label = "Your favorite number : ", 
    options = list(range(1, 11))
)

" Your favorire number is : " , option
# sidebar
text = st.sidebar.text_input("What is your hobbies")
"Your hobbies is ", text

condition = st.sidebar.slider("How are you today?", 0, 100, 50)
"Your condition level : ", condition

# multicolumns
left, right = st.columns(2)
button = left.button("Display letters in right hand side")
if button :
    right.write("This side is right")
    
# expander
expander_1 = st.expander("お問い合わせ1")
expander_1.write("お問い合わせ1回答")
expander_2 = st.expander("お問い合わせ2")
expander_2.write("お問い合わせ2回答")
expander_3 = st.expander("お問い合わせ3")
expander_3.write("お問い合わせ3回答")

# progress bar
st.write("Diplay progress bar")
"Start !"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done !!"