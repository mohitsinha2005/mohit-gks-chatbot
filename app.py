from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["question"].lower().strip()

    # --- 💬 Intelligent keyword-based chatbot ---
    if "who"or"WHO" in user_input and "mohit" in user_input:
        reply = (
            "👋 Mohit Sinha is a tech enthusiast and the creator of this GKS Chatbot project. "
            "He is passionate about Artificial Intelligence, Data Science, and innovation in education. "
            "He built this chatbot as part of his Global Korea Scholarship (GKS) University Track portfolio. 🌍"
        )

    elif "education"or "EDUCATION" in user_input or "study" in user_input:
        reply = (
            "🎓 Mohit is pursuing a Bachelor of Computer Applications (BCA) at MMDU University "
            "and also enrolled in the BS in Data Science Foundation Program at IIT Madras. "
            "He is focused on AI, machine learning, and data analytics research."
        )

    elif "goal"or "GOAL"in user_input or "future" in user_input or "dream" in user_input:
        reply = (
            "🚀 Mohit’s goal is to study Artificial Intelligence in South Korea through the GKS program "
            "and contribute to sustainable global technology collaboration between India and Korea."
        )

    elif "project"or"PROJECT" in user_input or "chatbot" in user_input:
        reply = (
            "🤖 This chatbot was developed by Mohit as part of his GKS application portfolio. "
            "It demonstrates his skills in Python (Flask), Web Development, and AI integration. "
            "It allows anyone to learn about his background and motivations interactively."
        )

    elif "gks"or"GKS" in user_input or "scholarship" in user_input:
        reply = (
            "🎓 The Global Korea Scholarship (GKS) is a prestigious, fully-funded program offered by the Korean government. "
            "It supports talented international students for undergraduate and graduate studies in Korea, "
            "covering tuition, airfare, stipend, and health insurance."
        )

    elif "achieve"or"ACHIEVE" in user_input or "certificate" in user_input or "award" in user_input:
        reply = (
            "🏅 Mohit has completed certifications in AI & Tableau (IIT Roorkee), "
            "Business Analytics (Coursera), and Web Design (IIT Madras). "
            "He has also achieved top ranks in science innovation contests and academic projects."
        )

    elif "language"or"LANGUAGE" in user_input or "korean" in user_input:
        reply = (
            "🗣️ Mohit plans to study the Korean language (Hangul) before arriving in Korea, "
            "and aims to achieve TOPIK Level 3 within his first year of study."
        )

    elif "motivation"or"MOTIVATION" in user_input or "why" in user_input:
        reply = (
            "💡 Mohit’s motivation for applying to GKS stems from Korea’s strong focus on innovation, "
            "engineering excellence, and cultural diversity. "
            "He believes that studying in Korea will help him bridge global AI innovation with real-world impact."
        )

    elif "contact"or"CONTACT" in user_input or "email" in user_input:
        reply = (
            "📩 You can reach Mohit directly at **sinhamohit9870@gmail.com** "
            "for academic or professional inquiries related to this project or scholarship."
        )

    elif "thanks" in user_input or "thank" in user_input:
        reply = "😊 You're very welcome! I’m glad I could assist you."

    else:
        # 💬 Intelligent fallback responses (for unknown or general queries)
        intelligent_replies = [
            "🤖 That’s an interesting question! Mohit’s focus is mainly on AI, Data Science, and educational innovation.please use small lettter alphbat ",
            "💬 Mohit loves exploring technology and cross-cultural learning. You can ask me about his Study Plan or Future Goals!,please use small lettter alphbat",
            "✨ I’m not sure about that, but Mohit’s research interests include Machine Learning, Web AI, and global collaboration.",
            "🧠 Mohit continues updating this chatbot — your question might be added in the next version!",
            "📘 You can learn more about Mohit’s education, goals, or achievements — just ask me!"
        ]
        reply = random.choice(intelligent_replies)

    return jsonify({"answer": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)









