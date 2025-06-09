:

🧑‍🏫 Mentor Dashboard for Placement Preparatory Classes
This Streamlit app leverages Groq’s LLaMA3-8B model to automatically generate structured learning materials (Pre-class, In-class, and Post-class) for final-year undergraduate placement preparation sessions.

🔗 Live Demo
👉 Check it out here: https://mentor-dashboard.streamlit.app

✨ Features

🧠 Input any technical topic (e.g., “Dynamic Programming”, “SQL Joins”)

📘 Automatically generates:

Pre-Class Notes (brief overview & objectives)

In-Class Teaching Script (mentor-led flow)

Post-Class Quiz & Summary (MCQs & key takeaways)

📄 Downloadable PDFs for each section

🔐 API key managed securely using Streamlit secrets

⚡ Powered by Groq’s LLaMA3-8B model (fast & accurate inference)

🛠️ Tech Stack

Python 🐍

Streamlit 🌐

LangChain 🧱

Groq (LLaMA3-8B) 🧠

FPDF (for PDF generation)

📦 Installation

Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/mentor-dashboard.git
cd mentor-dashboard
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your Groq API key using Streamlit secrets:

Create a file named .streamlit/secrets.toml in your project root:

arduino
Copy
Edit
mkdir -p .streamlit
Add your API key in the secrets file:

toml
Copy
Edit
# .streamlit/secrets.toml
GROQ_API_KEY = "your_groq_api_key_here"
🚀 Run the App

bash
Copy
Edit
streamlit run app.py
📁 Project Structure

bash
Copy
Edit
.
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .streamlit/
    └── secrets.toml        # API key config
🧠 Sample Topics You Can Try

Dynamic Programming

Operating Systems

SQL Joins

Computer Networks

System Design Basics

📝 License

This project is open-sourced for educational purposes. You're welcome to extend or modify it for your needs.
