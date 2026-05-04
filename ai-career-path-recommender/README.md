# AI Career Path Recommender

A Streamlit app that helps students explore suitable IT and data careers by rating their skills and comparing them to career profiles.

## Features

- Skill sliders for Python, SQL, communication, problem solving, cybersecurity interest, and data visualization
- Career matching using cosine similarity
- Ranked career recommendations
- 30-day action plan based on the best match
- Recommended skills and certifications

## Project structure

```text
.
├── app.py
├── requirements.txt
├── README.md
└── data
    └── career_profiles.csv
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Upload this project to a GitHub repository.
2. Go to Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the repository.
5. Set the main file path to:

```text
app.py
```

6. Click **Deploy**.

## Portfolio description

**AI Career Path Recommender**  
Built a Streamlit app that recommends suitable IT and data career paths by comparing a student's skill profile with career profiles using cosine similarity. The app ranks matches, displays recommended skills and certifications, and provides a 30-day action plan for the best-fit career.
