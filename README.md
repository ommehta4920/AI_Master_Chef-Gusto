# 🍽️ AI Master Chef - Gusto

**Gusto** is an AI-powered recipe assistant built using **Django**, **LangChain**, and **Google Generative AI (Gemini 2.5 Flash)**. This project provides a simple, intuitive web interface where users can request a food dish recipe, and Gusto generates a complete, step-by-step cooking guide.

> Developed during a learning journey into LLMs, LangChain, and Django.

---

## 🔥 Features

- 💬 Ask for any food recipe in natural language (e.g., *"I need Paneer Butter Masala recipe"*)
- 🧠 AI-generated recipes using **Gemini 2.5 Flash** via **LangChain**
- 📄 Session management: Keeps recipes visible even after a page reload
- 🚫 Graceful fallback for unrelated questions (e.g., *"Who is the Prime Minister of India?"*)
- 🎨 Django-based UI with Forms, Views, HTML & CSS
- 👨‍🍳 AI Chef Persona: **Gusto** (friendly, recipe-focused)

---

## 📸 Screenshots

| Input Form | Recipe Result | Invalid Query | Persistent Recipe |
|------------|----------------|---------------|--------------------|
| ![Screenshot 1](./screenshots/Screenshot%20(104).png) | ![Screenshot 2](./screenshots/Screenshot%20(105).png) | ![Screenshot 3](./screenshots/Screenshot%20(106).png) | ![Screenshot 4](./screenshots/Screenshot%20(107).png) |

> Place all 4 screenshots in a `screenshots/` directory in your repo.

---

## ⚙️ Tech Stack

- **Frontend:** HTML, CSS, Django Templates
- **Backend:** Django (Forms, Views, Sessions)
- **LLM Integration:** LangChain + Google GenAI (Gemini 2.5 Flash)
- **Session Storage:** Django sessions for recipe persistence

---

## 🚀 Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-master-chef.git
cd ai-master-chef
