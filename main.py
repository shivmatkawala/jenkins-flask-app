"""Flask app for NovaLearn homepage rendering."""

import os
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Render homepage with dynamic features, metrics, and current year."""
    features = [
        {
            "title": "Personalized Learning",
            "desc": "Adaptive lessons tailored to each student’s pace and interests."
        },
        {
            "title": "World-class Mentors",
            "desc": "On-demand mentoring from industry experts and top educators."
        },
        {
            "title": "Hands-on Projects",
            "desc": "Project-based curriculum that builds real portfolio-ready work."
        },
    ]

    metrics = {
        "students": "1M+",
        "courses": "2K+",
        "countries": "150+",
    }

    current_year = datetime.now().year
    return render_template(
        'index.html',
        features=features,
        metrics=metrics,
        current_year=current_year
    )

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)