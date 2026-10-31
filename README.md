# Education Portal

A comprehensive tutor management and online learning platform for students, parents, tutors, and corporate clients.

## Features

- **Tutor Management:** Registration, verification, subject & availability, ratings
- **Student & Parent Portal:** Tutor search, AI recommendations, demo booking, progress tracking
- **Corporate Portal:** Company profile, employee & training management, invoicing
- **Booking & Scheduling:** Calendar integration, reminders, attendance
- **Online Learning:** Live class (Zoom/Meet), whiteboard, recording, file sharing
- **Assignment Help:** Submission, tutor allocation, delivery
- **Payments:** Secure payments, wallet, tutor payouts, coupons
- **Communication:** Messaging, Email/SMS/Push, WhatsApp API
- **AI Powered:** Tutor-student matching, recommendations, chatbot, reporting

## Tech Stack

- Backend: Django / Python
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Database: SQLite (dev) / PostgreSQL (prod)
- AI: OpenAI / Azure AI

## How to Run Locally

```bash
# 1. Clone
git clone https://github.com/zahanarakhatun/education_portal.git
cd education_portal

# 2. Create venv
python -m venv env
env\Scripts\activate  # Windows
# source env/bin/activate  # Mac/Linux

# 3. Install
pip install -r requirements.txt

# 4. Migrate & Run
python manage.py migrate
python manage.py runserver
