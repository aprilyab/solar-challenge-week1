Solar Challenge Dashboard
Hi there! 👋
This project is a personal dashboard I developed as part of the Solar Challenge. It’s built using Streamlit and helps visualize clean solar energy data from Benin, Togo, and Sierra Leone. My goal was to create an interactive, user-friendly tool to explore and compare solar trends across these countries.

Why I Built This
As part of my learning and contribution to sustainable development goals, I wanted to:

    Practice working with real-world datasets 📊

    Explore data from multiple African countries 🌍

    Sharpen my Python and data visualization skills using Streamlit 🚀

    Collaborate and deploy a real web app 💻


How I Organized the Project

solar-challenge-week1/
│
├── app/                  # Streamlit app code
│   ├── main.py           # Entry point of the app
│   └── utils.py          # Utility functions
│
├── data/                 # Cleaned CSV data files
│   ├── benin_clean.csv
│   ├── togo_clean.csv
│   └── sierraleone_clean.csv
│
├── scripts/              # Any utility scripts
│
├── src/                  # Notebooks and documentation
│   └── notebooks/
│
├── .gitignore
├── requirements.txt
├── README.md
└── .github/workflows/ci.yml   # Optional GitHub Actions CI


 Development Setup
1. Clone the Repository

    git clone https://github.com/aprilyab/solar-challenge-week1.git
    cd solar-challenge-week1

2. Create and Activate Virtual Environment 

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

    pip install -r requirements.txt

4. Running the Streamlit App Locally

    streamlit run app/main.py

   this will start a local web server, and the dashboard will open in your default browser.

How I Deployed It on Streamlit Cloud
    Made sure the data/*.csv files were tracked in .gitignore.

    Pushed everything to the dashboard-dev branch of my GitHub repo.

    Went to https://streamlit.io/cloud and connected my repo.

    Set the main file path to app/main.py and hit deploy.

     You can check it live here: (https://solar-challenge-week1-iq82tqbznjgncvdnae4gkt.streamlit.app/)


Features I Added
     Clean line graphs for each country’s solar data

     Country selector and interactive filtering

     Easy-to-use UI for comparing time-based trends

     Modular code for easy future improvements

What I Learned
    How to organize a project with both raw data and an app

    How .gitignore behaves with folders and specific files

    How to resolve merge conflicts during collaboration

    Deploying a real Python dashboard to the web!

I’d love feedback or contributions!

    git checkout -b your-feature
    git commit -m "Add something cool"
    git push origin your-feature
    Then open a Pull Request

License
This is an open project — feel free to learn from it, use it, or build on it.
Licensed under MIT.