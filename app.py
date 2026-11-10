from flask import Flask, request, redirect, session, send_file
import os

# =========================================================
# APPLICATION SETUP
# =========================================================

app = Flask(__name__)
app.secret_key = "elevate_x_secret"

# logo path
LOGO_PATH = os.path.join(app.root_path, "static", "Logo.jpeg")


# =========================================================
# SAMPLE DATA
# =========================================================

users = [
    {
        "name": "Admin",
        "email": "admin@gmail.com",
        "password": "admin123",
        "role": "Admin"
    },
    {
        "name": "Aniket",
        "email": "trainee@gmail.com",
        "password": "1234",
        "role": "Trainee"
    },
    {
        "name": "Mokshika",
        "email": "trainer@gmail.com",
        "password": "1234",
        "role": "Trainer"
    },
    {
        "name": "Tripti",
        "email": "tripti@gmail.com",
        "password": "1234",
        "role": "Trainee"
    },
    {
        "name": "Soumya Yadav",
        "email": "soumya@gmail.com",
        "password": "1234",
        "role": "Trainee"
    }
]


courses = [
    {
        "id": 1,
        "name": "Cybersecurity Fundamentals",
        "skill": "Cybersecurity",
        "trainer": "Mokshika",
        "level": "Beginner"
    },
    {
        "id": 2,
        "name": "Python for Data Science",
        "skill": "Python",
        "trainer": "Mokshika",
        "level": "Intermediate"
    },
    {
        "id": 3,
        "name": "Leadership Skills",
        "skill": "Leadership",
        "trainer": "Mokshika",
        "level": "Beginner"
    }
]


competencies = {
    "Cybersecurity": 42,
    "Python": 82,
    "Data Analytics": 68,
    "Leadership": 55
}


questions = [
    {
        "question": "Which of these is used to protect a network?",
        "options": ["Firewall", "Compiler", "Keyboard", "Printer"],
        "answer": "Firewall"
    },
    {
        "question": "Which one is a strong password?",
        "options": ["123456", "password", "A@r9#kL2", "abcdef"],
        "answer": "A@r9#kL2"
    },
    {
        "question": "What does HTTPS provide?",
        "options": [
            "Secure communication",
            "Faster CPU",
            "More RAM",
            "File compression"
        ],
        "answer": "Secure communication"
    }
]


# =========================================================
# LOGO ROUTE
# =========================================================

@app.route("/logo")
def logo():
    """
    Serves the Elevate X logo from your Windows folder.
    """
    if os.path.exists(LOGO_PATH):
        return send_file(LOGO_PATH)

    return "Logo file not found. Please check the LOGO_PATH.", 404


# =========================================================
# COMMON STYLE
# =========================================================

STYLE = """
<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f4f6fb;
    color: #172554;
}

/* ---------------- NAVBAR ---------------- */

.navbar {
    background: #172554;
    color: white;
    padding: 14px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 3px 12px rgba(0,0,0,0.12);
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.brand img {
    width: 48px;
    height: 48px;
    object-fit: contain;
    background: white;
    border-radius: 10px;
    padding: 3px;
}

.brand-name {
    font-size: 22px;
    font-weight: bold;
    letter-spacing: 0.5px;
}

.brand-subtitle {
    font-size: 11px;
    color: #c7d2fe;
    margin-top: 3px;
    letter-spacing: 1px;
}

.navbar a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    margin-left: 20px;
}

.navbar a:hover {
    color: #93c5fd;
}

/* ---------------- CONTAINER ---------------- */

.container {
    width: 90%;
    max-width: 1100px;
    margin: 30px auto;
}

/* ---------------- LOGIN ---------------- */

.login-wrapper {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px;
    background:
        radial-gradient(circle at top right, #dbeafe, transparent 35%),
        #f4f6fb;
}

.login-card {
    background: white;
    width: 100%;
    max-width: 470px;
    padding: 38px;
    border-radius: 20px;
    box-shadow: 0 12px 40px rgba(23,37,84,0.12);
    text-align: center;
}

.login-logo {
    width: 150px;
    height: 150px;
    object-fit: contain;
    margin-bottom: 12px;
}

.login-card h1 {
    margin: 8px 0;
    color: #172554;
}

.login-card h3 {
    color: #64748b;
    font-weight: normal;
    margin-bottom: 28px;
}

.login-card input[type="email"],
.login-card input[type="password"] {
    padding: 14px;
    width: 100%;
    margin: 8px 0;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 15px;
}

.login-card input:focus {
    outline: none;
    border-color: #2563eb;
}

.login-card button {
    width: 100%;
    margin-top: 12px;
}

/* ---------------- CARDS ---------------- */

.card {
    background: white;
    padding: 24px;
    margin: 18px 0;
    border-radius: 14px;
    box-shadow: 0 4px 16px rgba(23,37,84,0.07);
}

.card h2 {
    margin-top: 0;
    color: #172554;
}

.card h3 {
    color: #1e3a8a;
}

/* ---------------- GRID ---------------- */

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}

/* ---------------- STAT BOXES ---------------- */

.stat {
    background: white;
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 4px 16px rgba(23,37,84,0.07);
    border-top: 4px solid #2563eb;
}

.stat h2 {
    color: #172554;
    font-size: 30px;
    margin: 5px 0 10px;
}

.stat p {
    color: #64748b;
    margin: 0;
}

/* ---------------- BUTTONS ---------------- */

button {
    background: linear-gradient(135deg, #172554, #2563eb);
    color: white;
    border: none;
    padding: 11px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    transition: 0.2s;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 12px rgba(37,99,235,0.25);
}

/* ---------------- LINKS ---------------- */

a {
    color: #2563eb;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* ---------------- PROGRESS ---------------- */

.progress {
    background: #e2e8f0;
    height: 14px;
    border-radius: 10px;
    overflow: hidden;
}

.progress-bar {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    height: 14px;
    border-radius: 10px;
    transition: width 0.5s;
}

/* ---------------- COURSE ITEMS ---------------- */

.course-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    padding: 15px 0;
    border-bottom: 1px solid #e2e8f0;
}

.course-item:last-child {
    border-bottom: none;
}

.course-info b {
    font-size: 16px;
}

.course-info span {
    color: #64748b;
    font-size: 14px;
}

/* ---------------- QUIZ ---------------- */

.quiz-option {
    display: block;
    margin: 14px 0;
    padding: 12px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    cursor: pointer;
}

.quiz-option:hover {
    background: #eff6ff;
    border-color: #93c5fd;
}

.quiz-option input {
    margin-right: 10px;
}

/* ---------------- FOOTER ---------------- */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    padding: 25px;
}

/* ---------------- RESPONSIVE ---------------- */

@media (max-width: 600px) {

    .navbar {
        padding: 14px 20px;
    }

    .brand-name {
        font-size: 18px;
    }

    .container {
        width: 94%;
    }

    .login-card {
        padding: 25px;
    }

    .course-item {
        flex-direction: column;
        align-items: flex-start;
    }

}

</style>
"""


# =========================================================
# COMMON NAVBAR
# =========================================================

def navbar(title="Elevate X"):
    return f"""
    <div class="navbar">

        <div class="brand">
            <img src="/logo" alt="Elevate X Logo">

            <div>
                <div class="brand-name">{title}</div>
                <div class="brand-subtitle">LEARN • BUILD • GROW</div>
            </div>
        </div>

        <div>
            <a href="/dashboard">Dashboard</a>
            <a href="/logout">Logout</a>
        </div>

    </div>
    """


# =========================================================
# LOGIN
# =========================================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        for user in users:

            if user["email"] == email and user["password"] == password:

                session["user"] = user

                return redirect("/dashboard")

        return STYLE + """
        <div class="login-wrapper">
            <div class="login-card">
                <h2>Invalid email or password!</h2>
                <p>Please try again.</p>
                <a href="/">
                    <button>Back to Login</button>
                </a>
            </div>
        </div>
        """

    return STYLE + """

    <div class="login-wrapper">

        <div class="login-card">

            <img src="/logo" class="login-logo" alt="Elevate X Logo">

            <h1>Elevate X</h1>

            <h3>Digital Capacity Building Platform</h3>

            <form method="POST">

                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    required>

                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    required>

                <button type="submit">
                    Login
                </button>

            </form>

            <hr>

            <p><b>Demo Accounts</b></p>

            <p>Admin: admin@gmail.com / admin123</p>

            <p>Aniket: trainee@gmail.com / 1234</p>

            <p>Mokshika: trainer@gmail.com / 1234</p>

            <p>Tripti: tripti@gmail.com / 1234</p>

            <p>Soumya Yadav: soumya@gmail.com / 1234</p>

        </div>

    </div>

    """


# =========================================================
# DASHBOARD ROUTE
# =========================================================

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    user = session["user"]

    if user["role"] == "Trainee":
        return trainee_dashboard(user)

    elif user["role"] == "Trainer":
        return trainer_dashboard(user)

    else:
        return admin_dashboard(user)


# =========================================================
# TRAINEE DASHBOARD
# =========================================================

def trainee_dashboard(user):

    cyber = competencies["Cybersecurity"]

    course_html = ""

    for c in courses:

        course_html += f"""
        <div class="course-item">

            <div class="course-info">
                <b>{c["name"]}</b>
                <br>
                <span>{c["skill"]} • {c["level"]}</span>
            </div>

            <a href="/course/{c["id"]}">
                <button>Open Course</button>
            </a>

        </div>
        """

    return STYLE + navbar("Elevate X") + f"""

    <div class="container">

        <div class="card">

            <h1>Welcome, {user["name"]} 👋</h1>

            <p>
                Continue your learning journey and elevate your skills.
            </p>

        </div>

        <div class="grid">

            <div class="stat">
                <h2>4</h2>
                <p>Courses</p>
            </div>

            <div class="stat">
                <h2>2</h2>
                <p>Completed</p>
            </div>

            <div class="stat">
                <h2>3</h2>
                <p>Certificates</p>
            </div>

            <div class="stat">
                <h2>{cyber}%</h2>
                <p>Overall Competency</p>
            </div>

        </div>

        <div class="card">

            <h2>🧠 My Competency</h2>

            <p>
                <b>Cybersecurity</b> — {cyber}%
            </p>

            <div class="progress">
                <div class="progress-bar"
                     style="width:{cyber}%">
                </div>
            </div>

            <p>
                Target: 80%
                <br>
                <b>Skill Gap: {80-cyber}%</b>
            </p>

        </div>

        <div class="card">

            <h2>🎯 Recommended Course</h2>

            <h3>Cybersecurity Fundamentals</h3>

            <p>
                Recommended because your cybersecurity competency
                is below the target level.
            </p>

            <a href="/course/1">
                <button>View Course</button>
            </a>

        </div>

        <div class="card">

            <h2>📚 Available Courses</h2>

            {course_html}

        </div>

    </div>

    <div class="footer">
        Elevate X • Learn • Build • Grow
    </div>

    """


# =========================================================
# COURSE PAGE
# =========================================================

@app.route("/course/<int:course_id>")
def course(course_id):

    course = next(
        (c for c in courses if c["id"] == course_id),
        None
    )

    if not course:
        return "Course not found"

    return STYLE + navbar("Elevate X") + f"""

    <div class="container">

        <div class="card">

            <h1>{course["name"]}</h1>

            <p>
                <b>Skill:</b> {course["skill"]}
            </p>

            <p>
                <b>Trainer:</b> {course["trainer"]}
            </p>

            <p>
                <b>Level:</b> {course["level"]}
            </p>

            <hr>

            <h3>📖 Learning Resources</h3>

            <p>• Introduction to {course["skill"]}</p>
            <p>• Basic concepts</p>
            <p>• Practical examples</p>

            <br>

            <a href="/quiz">
                <button>Attempt Assessment</button>
            </a>

        </div>

    </div>

    <div class="footer">
        Elevate X • Learn • Build • Grow
    </div>

    """


# =========================================================
# QUIZ
# =========================================================

@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    if "user" not in session:
        return redirect("/")

    if request.method == "POST":

        score = 0

        for i, q in enumerate(questions):

            answer = request.form.get(f"q{i}")

            if answer == q["answer"]:
                score += 1

        percentage = int(
            (score / len(questions)) * 100
        )

        # Update competency
        old_score = competencies["Cybersecurity"]

        new_score = min(
            100,
            old_score + int(percentage * 0.25)
        )

        competencies["Cybersecurity"] = new_score

        return STYLE + navbar("Elevate X") + f"""

        <div class="container">

            <div class="card">

                <h1>🎉 Assessment Completed</h1>

                <h2>
                    Score: {score}/{len(questions)}
                </h2>

                <h2>
                    Percentage: {percentage}%
                </h2>

                <hr>

                <h3>
                    Cybersecurity Competency Updated
                </h3>

                <p>
                    Previous Score:
                    {old_score}%
                </p>

                <p>
                    New Score:
                    <b>{new_score}%</b>
                </p>

                <a href="/dashboard">
                    <button>
                        Back to Dashboard
                    </button>
                </a>

            </div>

        </div>

        <div class="footer">
            Elevate X • Learn • Build • Grow
        </div>

        """

    question_html = ""

    for i, q in enumerate(questions):

        question_html += f"""

        <div class="card">

            <h3>
                Q{i+1}. {q["question"]}
            </h3>

        """

        for option in q["options"]:

            question_html += f"""

            <label class="quiz-option">

                <input
                    type="radio"
                    name="q{i}"
                    value="{option}"
                    required>

                {option}

            </label>

            """

        question_html += "</div>"

    return STYLE + navbar("Elevate X Assessment") + f"""

    <div class="container">

        <form method="POST">

            {question_html}

            <button type="submit">
                Submit Assessment
            </button>

        </form>

    </div>

    <div class="footer">
        Elevate X • Learn • Build • Grow
    </div>

    """


# =========================================================
# TRAINER DASHBOARD
# =========================================================

def trainer_dashboard(user):

    course_html = ""

    for c in courses:

        course_html += f"""
        <div class="course-item">

            <div class="course-info">
                <b>{c["name"]}</b>
                <br>
                <span>Skill: {c["skill"]}</span>
            </div>

        </div>
        """

    return STYLE + navbar("Elevate X • Trainer") + f"""

    <div class="container">

        <div class="card">

            <h1>Welcome Trainer, {user["name"]} 👨‍🏫</h1>

            <p>
                Manage courses and track trainee performance.
            </p>

        </div>

        <div class="grid">

            <div class="stat">
                <h2>3</h2>
                <p>My Courses</p>
            </div>

            <div class="stat">
                <h2>42</h2>
                <p>Trainees</p>
            </div>

            <div class="stat">
                <h2>86%</h2>
                <p>Average Performance</p>
            </div>

        </div>

        <div class="card">

            <h2>📚 My Courses</h2>

            {course_html}

        </div>

        <div class="card">

            <h2>📊 Trainee Performance</h2>

            <p>Aniket — 82%</p>
            <p>Soumya Yadav — 76%</p>
            <p>Tripti — 91%</p>

        </div>

    </div>

    <div class="footer">
        Elevate X • Learn • Build • Grow
    </div>

    """


# =========================================================
# ADMIN DASHBOARD
# =========================================================

def admin_dashboard(user):

    user_html = ""

    for u in users:

        user_html += f"""
        <p>
            <b>{u["name"]}</b>
            —
            {u["role"]}
            —
            {u["email"]}
        </p>
        """

    return STYLE + navbar("Elevate X • Admin") + f"""

    <div class="container">

        <div class="card">

            <h1>Admin Dashboard 🧑‍💼</h1>

            <p>
                Monitor organizational learning and competency.
            </p>

        </div>

        <div class="grid">

            <div class="stat">
                <h2>{len(users)}</h2>
                <p>Total Users</p>
            </div>

            <div class="stat">
                <h2>2</h2>
                <p>Trainees</p>
            </div>

            <div class="stat">
                <h2>1</h2>
                <p>Trainers</p>
            </div>

            <div class="stat">
                <h2>{len(courses)}</h2>
                <p>Courses</p>
            </div>

        </div>

        <div class="card">

            <h2>📊 Organizational Competency</h2>

            <p>
                Cybersecurity:
                <b>{competencies["Cybersecurity"]}%</b>
            </p>

            <div class="progress">
                <div class="progress-bar"
                     style="width:{competencies["Cybersecurity"]}%">
                </div>
            </div>

            <p>
                Target: 80%
            </p>

            <hr>

            <p>
                Python:
                <b>{competencies["Python"]}%</b>
            </p>

            <p>
                Data Analytics:
                <b>{competencies["Data Analytics"]}%</b>
            </p>

            <p>
                Leadership:
                <b>{competencies["Leadership"]}%</b>
            </p>

        </div>

        <div class="card">

            <h2>👥 User Management</h2>

            {user_html}

        </div>

        <div class="card">

            <h2>📢 Announcements</h2>

            <p>
                New Cybersecurity training available!
            </p>

            <p>
                Python assessment scheduled for Friday.
            </p>

        </div>

    </div>

    <div class="footer">
        Elevate X • Learn • Build • Grow
    </div>

    """


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(debug=False)