import streamlit as st 
import pandas as pd

st.set_page_config(layout='wide',page_title='Numbers')

with st.expander("Result Links"):
    st.info("Links of results [1-1](http://sasi.ac.in/11apr2022/) [1-2](http://sasi.ac.in/btech12sep2022/) [2-1](http://www.sasi.ac.in/btech21regjan2023/) [2-2](https://sasi.ac.in/btech22regsupjuly2023/) [3-1](https://sasi.ac.in/btech31regnov2023/)" )

st.header("Initally Grades are set to F")
st.header("Change them to your awarded Grades by clicking on Grade cells in each semeter Table")

def title():
    st.markdown(f"<h1 style='text-align: center; color: red;'>Do not Select Emtpy option as Grade</h1>", unsafe_allow_html=True)


#title()

points = {"A+": 10,"A": 9,"B": 8,"C": 7,"D": 6,"E": 5,"F": 0}


Subs = {
    "Sem1" : {
        "Technical English" : 3,
        "Engineering Mathematics-I": 3,
        "Basic Electrical Engineering": 3,
        "Programming for Problem Solving": 3,
        "Computer Aided Engineering Graphics": 3,
        "English Communication Skills Lab" : 1.5,
        "Basic Electrical Engineering Lab" : 1.5,
        "Programming for Problem Solving Lab" : 1.5,
        "Environmental Science" : 0,
    },
    "Sem2" : {
        "Engineering Mathematics - II" : 3,
        "Engineering Physics" : 3,
        "Engineering Chemistry" : 3,
        "Python Programming" : 3,
        "Data Structures" : 3,
        "Engineering Physics Lab" : 1.5,
        "Engineering Chemistry Lab" : 1.5,
        "Data Structures Lab" : 1.5,
        "Constitution of India, Professional Ethics & Human Right" : 0,
    },

    "Sem3" : {
        "Probability Distributions & Statistical Methods" : 3,
        "Data Science Using Python" : 2,
        "Data Base Management Systems Lab" : 1.5,
        "Java Programming Lab": 1.5,
        "Analog & Digital Electronics Lab" : 1.5,
        "Data Base Management Systems" : 3.0,
        "Java Programming" : 3.0,
        "Computer Organization": 3.0,
        "Analog & Digital Electronics" : 3.0,
        "Biology for Engineers" : 0,
    },

    "Sem4" : {
        "Discrete Mathematics" : 3,
        "Engineering Economics and Financial Management" : 3,
        "Operating systems" : 3,
        "Design and Analysis of Algorithms" : 3,
        "Software Engineering" : 3,
        "Operating Systems Lab" : 1.5,
        "Design and Analysis of Algorithms Lab" : 1.5,
        "Software Engineering Lab" : 1.5,
        "MEAN stack Technologies" : 2,	
    },

    "Sem5" : {
        "ATCD" : 3,
        "Summer Internship" : 1.5,
        "SSA" : 2.0,
        "DWM Lab" : 1.5,
        "CN Lab" : 1.5,
        "FIC" : 3,
        "SPM" : 3,
        "DWM" : 3,
        "CN" : 3,
        "IPR" : 0,
    },
}

def makedf(sem):
    data = {
        "Subjects" : [],
        "Grade" : [],
        "Credits" : [],
    }

    for sub , cred in Subs[sem].items():
        data["Subjects"].append(sub)
        data["Grade"].append("F")
        data["Credits"].append(round(cred,2))

    return pd.DataFrame(data)

tc = []
def calcPointAvg(df: pd.DataFrame):
    GPoints = df['Grade'].tolist()
    ACredits = df['Credits'].tolist()

    tc.append(sum(ACredits))

    sgp = sum([points[grade] * Credit for grade,Credit in zip(GPoints,ACredits)])

    return round(sgp/sum(ACredits),2)


c = st.columns(2)

gradescol = {
    "Subjects" : "Subjects",
    "Credits" : "Credits",
        "Grade" : st.column_config.SelectboxColumn(
            help = "Click on your Grade from DropDown",
            options = list(points.keys()),
            required=True,
        ),
    }

dcols = ['Subjects','Credits']

sgpa = []
with c[0]:
    st.write("1-1 Marks Table")
    S1 = st.data_editor(
        makedf("Sem1"),
        use_container_width = True,
        hide_index=True,
        column_config = gradescol,
        disabled=dcols,
    )
    s1r = calcPointAvg(S1)
    if calcPointAvg(S1) > 0:
        sgpa.append(s1r)
    st.write(f"Sem 1 SGPA: :green[{calcPointAvg(S1)}]")

    st.write("1-2 Marks Table")
    S2 = st.data_editor(
        makedf("Sem2"),
        use_container_width = True,
        hide_index=True,
        column_config = gradescol,
        disabled=dcols,
    )
    s2r = calcPointAvg(S2)
    if s2r > 0:
        sgpa.append(s2r)
    st.write(f"Sem 2 SGPA: :green[{calcPointAvg(S2)}]")

with c[1]:
    st.write("2-1 Marks Table")
    S3 = st.data_editor(
        makedf("Sem3"),
        use_container_width = True,
        hide_index=True,
        column_config = gradescol,
        disabled = dcols,
    )
    s3r = calcPointAvg(S3)
    if s3r > 0:
        sgpa.append(s3r)

    st.write(f"Sem 3 SGPA: :green[{calcPointAvg(S3)}]")

    st.write("2-2 Marks Table")
    S4 = st.data_editor(
        makedf("Sem4"),
        use_container_width = True,
        hide_index=True,
        column_config = gradescol,
        disabled=dcols,
    )
    s4r = calcPointAvg(S4)
    if s4r > 0:
        sgpa.append(s4r)
    st.write(f"Sem 4 SGPA: :green[{calcPointAvg(S4)}]")

S5 = st.data_editor(
        makedf("Sem5"),
        use_container_width = True,
        hide_index=True,
        column_config = gradescol,
        disabled=dcols,
    )
st.write(f"Sem 5 SGPA: :green[{calcPointAvg(S5)}]")

result_df = pd.concat([S1, S2, S3, S4, S5], axis=0)

st.write(f"Total Credits: {sum(tc)}")
st.toast(f"CGPA : :green[{calcPointAvg(result_df)}]")
st.info(f"CGPA : :green[{calcPointAvg(result_df)}]")
