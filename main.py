import streamlit as st
import pandas as pd
import re, json

st.set_page_config(layout='wide', page_title='Numbers')

def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def load_uploaded_csv(file):
    df = pd.read_csv(file)
    pre_filled_grades = {}
    for sem, data in df.groupby('Sem'):
        pre_filled_grades[sem] = list(data['Grade'])
    return pre_filled_grades

linksinfo = "Links of results [1-1](http://sasi.ac.in/results/11apr2022/) [1-2](http://sasi.ac.in/results/btech12sep2022/) [2-1](http://www.sasi.ac.in/results/btech21regjan2023/) [2-2](https://sasi.ac.in/results/btech22regsupjuly2023/) [3-1](https://sasi.ac.in/results/btech31regnov2023/) [3-2](https://www.sasi.ac.in/results/btech32april2024/)"
with st.expander("Result Links"):
    st.info(linksinfo)

st.header("Initially Grades are set to F")
st.header("Enter Grades for each sem in relative order of subjects without any spaces")

points = {"A+": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "F": 0}

w = st.toggle("SGPA's")
st.divider()

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
pre_filled_grades = {}
if uploaded_file:
    pre_filled_grades = load_uploaded_csv(uploaded_file)

if not w:
    with open('data.json', 'r') as d:
        Subs = json.load(d)

    def makedf(subs, creds, grads, sem):
        data = {
            "Sem": [sem] * len(subs),
            "Subjects": subs,
            "Grade": grads,
            "Credits": creds,
        }
        return pd.DataFrame(data)

    tc = []

    def calcPointAvg(df: pd.DataFrame):
        GPoints = df['Grade'].tolist()
        ACredits = df['Credits'].tolist()

        tc.append(sum(ACredits))

        sgp = sum([points[grade] * Credit for grade, Credit in zip(GPoints, ACredits)])

        return round(sgp / sum(ACredits), 2)

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

        cols = st.columns(2)
        with st.expander(f"Sem {n[-1]}: Enter Grades in this order of Subjects"):
            for m in list(Subs[n].keys()):
                st.markdown(f"- {m}")
        gradesinput = st.text_input(
            "Enter Grades",
            max_chars=len(Subs[n]) * 2,
            help=f"{allowed_grades}",
            key=n,
            value=''.join(pre_filled_grades.get(n, []))  # Pre-fill grades if available
        )
        if is_valid_input(gradesinput):
            gradesinput = [n.upper() for n in convert_to_list(gradesinput)]
        else:
            st.error(f"allowed grades are {allowed_grades}")
            gradesinput = ""
        res = makedf(list(Subs[n].keys()), list(Subs[n].values()), (list(gradesinput) + ['F'] * (len(Subs[n]) - len(gradesinput)))[:len(Subs[n])], n)
        semresults.append(res)

        st.success(f"Sem-{n[-1]} SGPA: :green[{calcPointAvg(res)}]")

    result_df = pd.concat(semresults, axis=0)

    st.write(f"Total Credits: {sum(tc)}")
    st.toast(f"CGPA : :green[{calcPointAvg(result_df)}]")
    st.info(f"CGPA : :green[{calcPointAvg(result_df)}]")

    csv = convert_df_to_csv(result_df)
    st.download_button("Download Result as CSV", data=csv, file_name="final_result.csv", mime='text/csv')

if w:
    alls = st.toggle("All")
    sgpas = []
    st.header("Enter SGPA for each sem")
    for n in range(linksinfo.count("[") + (8 - linksinfo.count("[")) if alls else linksinfo.count("[")):
        sgpas.append(st.number_input(f"Sem {n + 1}: ", min_value=0.00, max_value=10.00, key=n))
        st.info(f"CGPA till Sem {n + 1} ➡️ {round(sum(sgpas) / len(sgpas), 2)}")

    st.success(f"CGPA : {round(sum(sgpas) / len(sgpas), 2)}")
