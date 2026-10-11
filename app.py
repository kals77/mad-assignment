from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_plan(form):
    name = form.get("name", "").strip()
    subject = form.get("subject", "").strip()
    exam_date_raw = form.get("exam_date", "").strip()

    if not name or not subject or not exam_date_raw:
        raise ValueError("Please complete your name, subject and exam date.")

    try:
        total_topics = int(form.get("total_topics", ""))
        completed_topics = int(form.get("completed_topics", ""))
        hours_per_day = float(form.get("hours_per_day", ""))
        exam_date = date.fromisoformat(exam_date_raw)
    except (TypeError, ValueError):
        raise ValueError("Please enter valid numbers and choose a valid exam date.")

    if total_topics < 1:
        raise ValueError("Total topics must be at least 1.")
    if completed_topics < 0 or completed_topics > total_topics:
        raise ValueError("Completed topics must be between 0 and total topics.")
    if hours_per_day <= 0 or hours_per_day > 24:
        raise ValueError("Study hours must be more than 0 and no more than 24.")

    today = date.today()
    days_left = (exam_date - today).days
    if days_left < 0:
        raise ValueError("Exam date cannot be in the past.")

    remaining = total_topics - completed_topics
    progress = round((completed_topics / total_topics) * 100)
    days_available = max(days_left, 1)
    topics_per_day = remaining / days_available if remaining else 0

    if remaining == 0:
        advice, status = "All topics are completed. Use your time for revision and practice questions.", "Ready for revision"
    elif days_left == 0:
        advice, status = "Your exam is today. Focus on important topics and quick revision.", "Exam day"
    elif topics_per_day <= 2:
        advice, status = "Your plan looks manageable. Try to finish the daily target and revise briefly.", "On track"
    else:
        advice, status = "You have many topics left for the time available. Prioritise difficult and important topics.", "Needs focus"

    return {
        "name": name, "subject": subject, "exam_date": exam_date.strftime("%d %b %Y"),
        "days_left": days_left, "total_topics": total_topics, "completed_topics": completed_topics,
        "remaining": remaining, "progress": progress, "hours_per_day": hours_per_day,
        "topics_per_day": round(topics_per_day, 1), "status": status, "advice": advice
    }

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    if request.method == "POST":
        try:
            result = calculate_plan(request.form)
        except ValueError as exc:
            error = str(exc)
    return render_template("index.html", result=result, error=error, today=date.today().isoformat())

@app.get("/health")
def health():
    return {"status": "ok", "app": "StudySprint"}

if __name__ == "__main__":
    app.run(debug=True)
