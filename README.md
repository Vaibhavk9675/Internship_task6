# My Portfolio Website (Flask)

A personal portfolio website built using **Flask**, HTML, CSS, and JavaScript.  
The site showcases personal information, projects, education, and includes a **contact form** that saves user submissions into a text file (`contacts.txt`).

---

## 🚀 Features
- Responsive design for desktop and mobile.
- Navigation bar with smooth scrolling to sections.
- About, Education, and Projects sections.
- Contact form with:
  - Name, Email, Phone Number, and Message fields.
  - Data saved to a text file on the server.
- Modern gradient-based theme.

---

## 📂 Project Structure
project/
│
├── static/
│ ├── style.css # Website styling
│ ├── bg.png # Background image
│ └── project1-screenshot.png # Example project image
│
├── templates/
│ ├── layout.html # Base layout with navbar & footer
│ ├── index.html # Home page content
│ └── contact.html # Contact page content
│
├── app.py # Flask application
├── contacts.txt # Stores form submissions
└── README.md # Project documentation


---

##  Requirements
- Python 3.7+
- Flask

Install dependencies:
```bash
pip install -r requirements.txt


