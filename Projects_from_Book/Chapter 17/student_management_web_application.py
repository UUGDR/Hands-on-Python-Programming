"""Chapter 17 project: Student Management Web Application.
Reconstructed from manuscript project descriptions; not a verbatim screenshot transcription.
"""

import os
from flask import Flask, request, redirect, url_for, jsonify, render_template_string

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "development-only-not-for-production")
students = []
PAGE = """<h1>Student Management</h1><form method="post" action="/add">
<input name="name" placeholder="Student name" required>
<input name="mark" type="number" min="0" max="100" required>
<button>Add</button></form><ul>
{% for s in students %}<li>{{ s.name }}: {{ s.mark }}</li>{% endfor %}
</ul><a href="/stats">Statistics</a>"""

@app.get("/")
def home():
    return render_template_string(PAGE, students=students)

@app.post("/add")
def add():
    name = request.form.get("name", "").strip()
    try:
        mark = float(request.form.get("mark", ""))
    except ValueError:
        return "Invalid mark", 400
    if not name or not 0 <= mark <= 100:
        return "Invalid student details", 400
    students.append({"name": name, "mark": mark})
    return redirect(url_for("home"))

@app.get("/stats")
def stats():
    return jsonify({"count": len(students),
                    "average": sum(s["mark"] for s in students)/len(students) if students else 0})

if __name__ == "__main__":
    app.run(debug=False)
