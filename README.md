# StudySprint — Full-stack Study Planner

A college assignment app using HTML, CSS, Python and Flask.

## Inputs (6)
1. Name
2. Subject/course
3. Total topics
4. Topics completed
5. Exam date
6. Study hours per day

The Flask backend validates the inputs and calculates completion percentage, topics remaining, days left, daily topic target and a simple suggestion. The result is returned to the website.

## Run on Windows
1. Install Python 3.10 or newer.
2. Extract the ZIP and open the project folder in VS Code.
3. In the VS Code terminal run:
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python app.py
   ```
   If PowerShell blocks activation, skip the activation command and use `py -m pip install -r requirements.txt`, then `py app.py`.
4. Open `http://127.0.0.1:5000`.

## Check backend
Open `http://127.0.0.1:5000/health`. It should return `{"status":"ok","app":"StudySprint"}`.

## GitHub separate branch
Create an empty repository on GitHub named `studysprint-app`, then run these commands here (replace YOUR_USERNAME):
```bash
git init
git add .
git commit -m "Add StudySprint full-stack app"
git branch -M main
git checkout -b assignment-2
git remote add origin https://github.com/YOUR_USERNAME/studysprint-app.git
git push -u origin assignment-2
```
Share: `https://github.com/YOUR_USERNAME/studysprint-app/tree/assignment-2`

GitHub stores the code but does not run Flask automatically. Deploy separately if a live website URL is required. This demo does not store entries in a database.
