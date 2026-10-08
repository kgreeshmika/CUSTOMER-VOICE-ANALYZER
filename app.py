from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    polarity = None
    subjectivity = None
    feedback = ""
    error = None

    if request.method == "POST":
        feedback = request.form.get("feedback", "").strip()

        if not feedback:
            error = "Please enter some customer feedback before analyzing."

        elif len(feedback) < 3:
            error = "Please enter a little more feedback for a meaningful analysis."

        else:
            analysis = TextBlob(feedback)

            polarity = round(analysis.sentiment.polarity, 2)
            subjectivity = round(analysis.sentiment.subjectivity, 2)

            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

    return render_template(
        "index.html",
        feedback=feedback,
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)