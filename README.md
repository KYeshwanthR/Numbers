# [Numbers](https://numbers.streamlit.app/) 
## Overview
This Streamlit-based web application calculates academic grades.The application allows users to input grades for various courses and calculates both Semester Grade Point Average (SGPA) and Cumulative Grade Point Average (CGPA). 

## Features
- **Grade Input**: Enter grades for each semester's courses.
   - **SGPA Calculation**: Calculates the SGPA for each semester based on the provided grades.
- **SGPA Input**: Enter SGPA's for each semester.
- **CGPA Calculation**: Offers a cumulative view of academic performance over semesters.
- **Result Links**: Original result links are provided under results dropdown.

## Installation

To get started with this project, you'll need to have Python installed on your system. The application relies on Streamlit and Pandas, which can be installed using the following steps:

1. **Clone the Repository**
   ```
   git clone [https://github.com/KYeshwanthR/Numbers.git]
   cd [Numbers]
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

## Usage

After installation, run the application using Streamlit:

```
streamlit run main.py
```

Navigate through the application:

1. **Enter Grades**: Input the grades for each course in the provided fields.
   1. **View SGPA**: Each semester's SGPA is displayed upon entering the grades.
2. **Enter SGPAs**: Input SGPAs for each semester.
3. **Calculate CGPA**: Your CGPA is automatically calculated based on the SGPAs.