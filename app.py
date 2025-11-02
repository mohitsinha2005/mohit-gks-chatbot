from flask import Flask, render_template, request, jsonify
import random
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question", "").strip().lower()

    # Clean and normalize input (remove punctuation)
    user_input = re.sub(r'[^\w\s]', '', user_input)

    # --- 💬 Intelligent keyword-based chatbot ---
    if "who" in user_input and "mohit" in user_input:
        reply = (
            "👋 Mohit Sinha is a tech enthusiast and the creator of this GKS Chatbot project. "
            "He is passionate about Artificial Intelligence, Data Science, and innovation in education. "
            "He developed this chatbot as part of his Global Korea Scholarship (University Track) portfolio. 🌍"
        )

    elif "education" in user_input or "study" in user_input or "academic" in user_input:
        reply = (
            "🎓 Mohit is pursuing a Bachelor of Computer Applications (BCA) at MMDU University, "
            "and is also enrolled in the BS in Data Science Foundation Program at IIT Madras. "
            "His interests include machine learning, programming, and applied AI research."
        )

    elif "goal" in user_input or "future" in user_input or "dream" in user_input:
        reply = (
            "🚀 Mohit’s long-term goal is to become a global AI researcher and innovator. "
            "He aims to study in Korea through the GKS program and contribute to AI-driven solutions "
            "that strengthen collaboration between India and Korea."
        )

    elif "project" in user_input or "chatbot" in user_input:
        reply = (
            "🤖 This chatbot is part of Mohit’s GKS portfolio. It demonstrates his ability to combine AI concepts "
            "with real-world applications using Python (Flask) and web development. "
            "It allows users to learn about his profile interactively and intelligently."
        )

    elif "gks" in user_input or "scholarship" in user_input or "korea" in user_input:
        reply = (
            "🎓 The Global Korea Scholarship (GKS) is a fully-funded Korean government program "
            "that offers international students a chance to study in Korea. It covers tuition, airfare, stipend, "
            "and health insurance while promoting global academic exchange and friendship."
        )

    elif "achievement" in user_input or "certificate" in user_input or "award" in user_input:
        reply = (
            "🏅 Mohit has completed certifications in AI & Tableau (IIT Roorkee), "
            "Business Analytics (Coursera), and Web Design (IIT Madras). "
            "He has also achieved top ranks in innovation and science contests."
        )

    elif "language" in user_input or "korean" in user_input or "hangul" in user_input:
        reply = (
            "🗣️ Mohit is learning the Korean language (Hangul) and aims to achieve TOPIK Level 3 "
            "within his first year of study in Korea."
        )

    elif "motivation" in user_input or "why" in user_input:
        reply = (
            "💡 Mohit’s motivation for applying to GKS is inspired by Korea’s advanced technology environment "
            "and strong innovation culture. He believes studying there will help him merge AI, creativity, "
            "and global collaboration for real-world impact."
        )

    elif "contact" in user_input or "email" in user_input or "reach" in user_input:
        reply = (
            "📩 You can contact Mohit for academic or professional inquiries via email: "
            "**sinhamohit9870@gmail.com**"
        )

    elif "age" in user_input or "birth" in user_input or "dob" in user_input:
        reply = (
            "🧾 Mohit is 18 years old, born on **11 July 2007**. "
            "He represents the next generation of young innovators in AI and technology."
        )

    elif "thanks" in user_input or "thank" in user_input or "appreciate" in user_input:
        reply = "😊 You’re most welcome! I’m glad I could assist you."

    else:
        # 💬 Intelligent fallback answers (for general or unknown questions)
        intelligent_replies = [
            "🤖 That’s an interesting question! Mohit’s work mainly focuses on AI, Data Science, and innovation 🌍.",
            "💬 Mohit enjoys exploring technology and education. You can ask about his Education, Study Plan, or Achievements!",
            "✨ I’m not sure about that yet, but Mohit’s interests include Machine Learning, Web AI, and cross-cultural learning.",
            "🧠 Mohit continues improving this chatbot — your question might appear in the next version update!",
            "📘 Ask about Mohit’s Education, Projects, or GKS Journey to learn more about him!"
        ]
        reply = random.choice(intelligent_replies)

    return jsonify({"answer": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)









