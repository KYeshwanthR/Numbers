import streamlit as st 
import pandas as pd
import re, json

st.set_page_config(layout='wide',page_title='Numbers')

with st.expander("Result Links"):
    st.info("Links of results [1-1](http://sasi.ac.in/11apr2022/) [1-2](http://sasi.ac.in/btech12sep2022/) [2-1](http://www.sasi.ac.in/btech21regjan2023/) [2-2](https://sasi.ac.in/btech22regsupjuly2023/) [3-1](https://sasi.ac.in/btech31regnov2023/)" )

st.header("Initally Grades are set to F")
st.header("Enter Grades for each sem in relative order of subjects without any spaces")

points = {"A+": 10,"A": 9,"B": 8,"C": 7,"D": 6,"E": 5,"F": 0}

with open('data.json','r') as d:
    Subs = json.load(d)


def makedf(subs,creds,grads):
    data = {
        "Subjects" : subs,
        "Grade" : grads,
        "Credits" : creds,
    }

    return pd.DataFrame(data)

tc = []
def calcPointAvg(df: pd.DataFrame):
    GPoints = df['Grade'].tolist()
    ACredits = df['Credits'].tolist()

    tc.append(sum(ACredits))

    sgp = sum([points[grade] * Credit for grade,Credit in zip(GPoints,ACredits)])

    return round(sgp/sum(ACredits),2)

def is_valid_input(input_string):
    # Regular expression pattern with case-insensitivity
    pattern = r'^(a\+|[abcdef])+$'
    return bool(re.match(pattern, input_string, re.IGNORECASE))

def convert_to_list(input_string):
    # Regular expression to find 'A+' and individual characters
    pattern = r'a\+|[abcdef]'
    return re.findall(pattern, input_string, re.IGNORECASE)

semresults = []
for n in Subs:
    allowed_grades = ['A+', 'A', 'B', 'C', 'D', 'E', 'F']
    default = 'F'

    st.divider()
    cols = st.columns(2)
    gradesinput = st.text_input("Enter Grades",max_chars=len(Subs[n])*2,help=f"{allowed_grades}",key=n)
    st.info("Enter Grades in order of Subjects")
    if is_valid_input(gradesinput):
        gradesinput = [n.upper() for n in convert_to_list(gradesinput)]
    else:
        st.error(f"allowed grades are {allowed_grades}")
    res = makedf(list(Subs[n].keys()),list(Subs[n].values()),(list(gradesinput) + ['F']*(len(Subs[n]) - len(gradesinput)))[:len(Subs[n])])
    st.dataframe(res,use_container_width=True,hide_index=True)
    semresults.append(res)

    st.success(f"Sem-{n[-1]} SGPA: :green[{calcPointAvg(res)}]" )

result_df = pd.concat(semresults, axis=0)

st.write(f"Total Credits: {sum(tc)}")
st.toast(f"CGPA : :green[{calcPointAvg(result_df)}]")
st.info(f"CGPA : :green[{calcPointAvg(result_df)}]")