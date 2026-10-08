# Customer Voice Analyzer

## Overview

Customer Voice Analyzer is a Flask-based web application developed using Python and TextBlob for analyzing customer feedback.

The application accepts customer feedback through a web interface and performs sentiment analysis to classify the feedback as Positive, Negative, or Neutral. It also displays polarity and subjectivity scores to provide additional information about the feedback.

This project was developed as part of the QSkill Python Development Internship.

## Features

- Customer feedback input through a web interface
- Sentiment analysis using TextBlob
- Classification into Positive, Negative, or Neutral
- Polarity score display
- Subjectivity score display
- Empty-input validation
- Short-input validation
- Flask-based web interface
- Simple and user-friendly interface
- Error handling for invalid feedback

## Technologies Used

- Python
- Flask
- TextBlob
- HTML
- CSS

## Project Structure

```text
CUSTOMER_VOICE_ANALYZER_PROJECT/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```
## How It Works

The application is built using Flask and uses TextBlob to analyze the sentiment of customer feedback.

When a user submits feedback:

1. The feedback is received by the Flask application.
2. The input is checked for empty or very short text.
3. TextBlob analyzes the feedback.
4. The polarity and subjectivity scores are calculated.
5. The polarity score is used to classify the sentiment.
6. The sentiment, polarity, and subjectivity are displayed on the web page.

## Sentiment Analysis

The application uses TextBlob sentiment analysis to determine the emotional characteristics of the submitted feedback.

### Polarity

Polarity indicates whether the feedback is positive or negative.

The polarity value ranges from -1.0 to 1.0.

The application classifies sentiment as follows:

- Polarity greater than 0 → Positive
- Polarity less than 0 → Negative
- Polarity equal to 0 → Neutral

### Subjectivity

Subjectivity indicates whether the feedback is more objective or opinion-based.

The subjectivity value ranges from 0.0 to 1.0.

A lower value generally indicates more objective content, while a higher value indicates more subjective content.

## Example

### Positive Feedback

Input:

The product quality is excellent and I am very happy with the service.

Expected result:

Sentiment: Positive

### Negative Feedback

Input:

The service was very poor and I am disappointed with the experience.

Expected result:

Sentiment: Negative

### Neutral Feedback

Input:

The package was delivered yesterday.

Expected result:

Sentiment: Neutral

The application also displays the corresponding polarity and subjectivity scores for the submitted feedback.

## Input Validation

The application includes validation to prevent empty or extremely short feedback from being analyzed.

### Empty Input

If the user submits the form without entering any feedback, the application displays an error message asking the user to enter customer feedback.

### Very Short Input

If the submitted feedback contains fewer than three characters, the application displays an error message asking the user to enter more feedback for meaningful analysis.

This validation helps ensure that the application receives sufficient text for sentiment analysis.

## Application Workflow

The application follows the following workflow:

1. User enters customer feedback.
2. Flask receives the submitted feedback.
3. The input is validated.
4. TextBlob performs sentiment analysis.
5. Polarity and subjectivity scores are calculated.
6. The sentiment is classified as Positive, Negative, or Neutral.
7. The analysis results are displayed on the web page.

## Environment Setup

### 1. Create a Virtual Environment

Open a terminal in the project directory and run:
python -m venv venv

### 2. Activate the Virtual Environment

#### Windows PowerShell:

.\venv\Scripts\Activate.ps1

If PowerShell blocks script execution for the current terminal session, use:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1


### 3. Install Dependencies

Install the required packages using:
pip install -r requirements.txt

## Running the Application

After activating the virtual environment and installing the dependencies, run:
python app.py

The Flask development server will start locally.

Open the application in a browser at:
[http://127.0.0.1:5000/]

## Requirements

The project requires Python and the packages listed in `requirements.txt`.

The main dependencies are:
Flask
TextBlob

## Use Cases

Customer Voice Analyzer can be used for:

- Customer feedback analysis
- Product review analysis
- Service review analysis
- User opinion analysis
- Basic Natural Language Processing applications
- Demonstrating sentiment analysis using Python

## Error Handling

The application handles the following situations:

- Empty customer feedback
- Very short customer feedback
- Invalid form input
- Sentiment analysis processing errors

The application provides appropriate messages when the submitted feedback does not meet the minimum input requirements.

## Limitations

The application uses TextBlob's general-purpose sentiment analysis and is intended as a basic sentiment analysis demonstration.

Sentiment classification may vary depending on the wording, context, sarcasm, language, and complexity of the feedback.

## Future Enhancements

Possible future improvements include:

- Storing customer feedback in a database
- Adding feedback history
- Adding sentiment analysis charts
- Supporting multiple languages
- Adding user authentication
- Using advanced NLP or machine learning models
- Deploying the application to a cloud platform

## Internship Task

This project was developed as one of the selected tasks for the **QSkill Python Development Internship** under the **Python Development** domain.

The project demonstrates:

- Python development
- Flask web application development
- TextBlob sentiment analysis
- Natural Language Processing
- Customer feedback analysis
- Input validation
- Error handling
- Web application development

## Author

**Kondabathula Greeshmika**

## License

This project was developed for educational and internship purposes.
