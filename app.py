from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ------------------------------
# Mohit Sinha – GKS-KOREATECH Application Assistant
# Works fully offline – no API required
# ------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["question"].lower()

    # --- Knowledge base (from your real application) ---
    responses = {
        "who is mohit": """Mohit Sinha is an applicant for the 2026 Global Korea Scholarship (University Track) at KOREATECH – Korea University of Technology and Education. He is from India and aims to pursue a Bachelor’s in Computer Science and Artificial Intelligence. He is currently studying BCA at MMDU University and BS in Data Science and Applications at IIT Madras.""",

        "education": """Mohit completed high school at Vishvas Public School, India (CBSE board), where he excelled in academics and extracurriculars. He is pursuing BCA at MMDU and the BS Data Science Foundation Program from IIT Madras, with an expected graduation in December 2025.""",

        "personal statement": """From a young age, Mohit has been fascinated by how technology can empower societies. His motivation to study at KOREATECH comes from Korea’s innovative ecosystem and its focus on applied engineering. He admires KOREATECH’s hands-on education model that connects academia and industry. Mohit’s vision is to contribute to AI-driven cooperation between Korea and India.""",

        "study plan": """Mohit plans to strengthen his Python and AI fundamentals before arrival. In Year 1, he will study computer fundamentals and join AI clubs. In Year 2, he will explore Deep Learning and NLP. In Year 3, he will conduct supervised research in predictive modeling. In Year 4, he aims to complete a capstone project with industry collaboration and publish his research.""",

        "future plan": """After graduation, Mohit plans to contribute to Korea’s AI and technology ecosystem by developing smart systems in healthcare and sustainable innovation. Long-term, he aims to collaborate on research between KOREATECH and Indian universities, mentoring future engineers and strengthening Korea–India relations.""",

        "certification": """Mohit holds multiple certifications: BS in Data Science (IIT Madras), AI and Tableau (IIT Roorkee), Business Analytics (Coursera), Product Management and Cybersecurity workshops (IIT Roorkee), and Web Designing from IIT Madras.""",

        "achievements": """He ranked 1st in the National Science Olympiad, 3rd in ASSET Test and International Science Olympiad, and earned numerous awards for academic excellence and innovation.""",

        "language plan": """Mohit studied English for 12 years. He plans to study Hangul and Korean grammar before arriving in Korea, and to participate in GKS Korean language classes. His goal is to reach TOPIK Level 3 within one year to fully engage in lectures and research.""",

        "lor": """The Letter of Recommendation from Vishvas Public School describes Mohit as hardworking, responsible, and academically excellent. His teachers highlight his leadership, enthusiasm, and cooperative spirit, recommending him strongly for university study.""",

        "contact": """Email: sinhamohit9870@gmail.com | Phone: +91 82955 52340 | Address: 23/7 Satya Nagar, Shahabad Markanda, Haryana, India – 136135.""",

        "note": """All submitted documents are attested as true copies by the Principal due to time constraints. Mohit has signed every document for verification and commits to submit apostilled originals if selected. He can be contacted anytime for clarification or additional documents.""",

         "age": """17 year.""",
    }

    # --- Response selection logic ---
    reply = "I'm Mohit’s AI Assistant. You can ask about his Study Plan, Personal Statement, Certifications, LOR,CONTACTS or Future Goals. IF YOU NEED ADDITIONAL PEARSONAL DETAIL PLEASE CONTACT WITH MY BOSS EMAIL:- sinhamohit9870@gmail.com"
    for key in responses:
        if key in user_input:
            reply = responses[key]
            break

    return jsonify({"answer": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



