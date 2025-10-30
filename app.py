from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["question"].lower()

    responses = {
        "who is mohit": (
            "👋 Mohit Sinha is a student from India and the creator of this GKS Chatbot project. "
            "He developed it as part of his application for the Global Korea Scholarship (University Track). "
            "He aims to pursue a degree in Computer Science and Artificial Intelligence at KOREATECH, "
            "focusing on AI innovation and international collaboration. 🌏"
        ),

        "education": (
            "🎓 Mohit is currently studying Bachelor of Computer Applications at MMDU University "
            "and pursuing the BS in Data Science Foundation Program from IIT Madras. "
            "He has a strong academic record and an interest in applied AI research."
        ),

        "personal statement" or "PEASONAL STATEMENT"or"Pearsonal statement": (
            "🧠 From an early age, Mohit has been fascinated by how technology can solve global problems. "
            "His motivation for studying in Korea comes from the country’s innovation-driven environment "
            "and focus on practical engineering education. He hopes to build bridges between Korean and Indian tech ecosystems."
        ),

        "study plan"or"Study plan"or"STUDY PLAN": (
            "📘 Mohit’s study plan includes mastering Python, machine learning, and data analysis in the first year, "
            "then specializing in AI-based research and real-world projects during his later years at KOREATECH."
        ),

        "future plan"or"FUTURE PLAN"or"Future plan": (
            "🚀 After graduation, Mohit hopes to contribute to Korea’s AI and technology ecosystem, "
            "working on sustainable innovation projects and fostering collaboration between Korean and Indian researchers."
        ),

        "certification"or"CERTIFICATION"or"Certification": (
            "📜 He has completed multiple online programs including AI & Tableau from IIT Roorkee, "
            "Business Analytics from Coursera, and Web Design training from IIT Madras."
        ),

        "achievements"or"ACHIEVEMENTS"or"Achivements": (
            "🏅 Mohit has received top ranks in science olympiads and innovation contests, "
            "reflecting his dedication to both academics and creative problem-solving."
        ),

        "language plan"or"LANGUAGE PLAN"or"Language plan": (
            "🗣️ Mohit plans to study Hangul before arriving in Korea and aims to achieve TOPIK Level 3 within his first year."
        ),

        "lor"or"LOR"or"Lor": (
            "📝 Mohit’s Letter of Recommendation highlights his leadership, discipline, and teamwork — "
            "qualities that make him an ideal candidate for international study."
        ),

        "contact"or"CONTACT"or"Contact": (
            "📩 For official or academic inquiries, please reach out through the project portfolio or the chatbot contact form. "
            "This version does not share personal details publicly for safety reasons.PEASE CONTACT THIS EMAIL-SINHAMOHIT9870@GMAIL.COM"
        ),

        "age"or"AGE"or"Age": "🧾 Mohit is currently 18 years old. date of birth (11-07-2007)"
    }

    reply = (
        "🤖 I’m Mohit’s AI Assistant! You can ask about his Study Plan, Education, Certifications, "
        "Achievements, or age,contact,Future Goals,related to the GKS Scholarship."
    )

    for key in responses:
        if key in user_input:
            reply = responses[key]
            break

    return jsonify({"answer": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)







