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
    user_input = re.sub(r'[^\w\s]', '', user_input)  # remove punctuation

    reply = None  # start with no reply

    # --- 💬 Intelligent keyword-based chatbot ---
    if any(word in user_input for word in ["who is mohit", "about mohit", "mohit sinha"]):
        reply = (
            "👋 Mohit Sinha is a tech enthusiast and the creator of this GKS Chatbot project. "
            "He is passionate about Artificial Intelligence, Data Science, and innovation in education. "
            "He built this chatbot as part of his Global Korea Scholarship (GKS) University Track portfolio. 🌏✨"
        )

    elif any(word in user_input for word in ["education", "study", "academic", "university"]):
        reply = (
            "🎓 Mohit is pursuing a Bachelor of Computer Applications (BCA) at MMDU University, "
            "and the BS in Data Science Foundation Program from IIT Madras. "
            "He’s passionate about AI, data analytics, and global learning."
        )

    elif any(word in user_input for word in ["goal", "future", "dream", "career"]):
        reply = (
            "🚀 Mohit’s goal is to become a leading AI researcher. "
            "He aims to contribute to AI-driven innovation and strengthen tech collaboration between India and Korea."
        )

    elif any(word in user_input for word in ["project", "chatbot", "portfolio", "work"]):
        reply = (
            "🤖 This chatbot project was developed by Mohit to showcase his skills in AI, Python (Flask), "
            "and web development. It represents his ability to create smart and interactive web-based tools."
        )

    elif any(word in user_input for word in ["gks", "scholarship", "korea", "global korea"]):
        reply = (
            "🎓 The Global Korea Scholarship (GKS) is a fully-funded program by the Korean government "
            "that offers international students a chance to study in Korea with tuition, airfare, stipend, and insurance covered."
        )

    elif any(word in user_input for word in ["achievement", "certificate", "award", "accomplishment"]):
        reply = (
            "🏅 Mohit has completed certifications in AI & Tableau (IIT Roorkee), "
            "Business Analytics (Coursera), and Web Design (IIT Madras). "
            "He’s also received recognition for innovation and academic excellence."
        )

    elif any(word in user_input for word in ["language", "korean", "hangul", "topik"]):
        reply = (
            "🗣️ Mohit plans to learn the Korean language (Hangul) and aims to achieve TOPIK Level 3 "
            "within his first year in Korea."
        )

    elif any(word in user_input for word in ["motivation", "why", "reason", "interest"]):
        reply = (
            "💡 Mohit’s motivation for applying to GKS comes from Korea’s innovation-driven education system "
            "and strong AI research culture. He believes studying in Korea will enhance his global perspective."
        )

    elif any(word in user_input for word in ["contact", "email", "reach", "gmail", "connect"]):
        reply = (
            "📩 You can reach Mohit at **sinhamohit9870@gmail.com** for academic or professional inquiries. "
            "He’s always open to collaboration and research discussions."
        )

    elif any(word in user_input for word in ["age", "birth", "dob", "old"]):
        reply = (
            "🧾 Mohit is currently 18 years old, born on **11 July 2007**. "
            "He represents the new generation of global innovators in AI and technology."
        )

    elif any(word in user_input for word in ["thanks", "thank", "appreciate", "great"]):
        reply = "😊 You’re very welcome! I’m always here to help."

    # --- 💡 Fallback intelligent responses ---
    else:
        intelligent_replies = [
            "🤖 That’s a thoughtful question! Mohit’s focus is on AI, data science, and innovation 🌍.",
            "💬 Mohit enjoys building AI projects and exploring technology. You can ask about his Education, Goals, or Projects!",
            "✨ Interesting! While I don’t have that detail yet, Mohit is always expanding his knowledge and skills.",
            "🧠 Mohit keeps updating this chatbot — your question might appear in the next version!",
            "📘 Try asking about his GKS journey, education, achievements, or future plans!"
        ]
        reply = random.choice(intelligent_replies)

    return jsonify({"answer": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)











