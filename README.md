# Phishing Simulation Project

This project is a phishing awareness training simulation built with Flask and hosted on Render. It presents users with a simulated Outlook-style inbox containing **three realistic, malicious emails** designed to mimic different types of phishing attacks.

🔗 **Live Demo:** [https://phishing-simulation-5xzp.onrender.com](https://phishing-simulation-5xzp.onrender.com)

## 🛡️ Purpose

The goal of this simulation is to help users identify and understand different forms of phishing attacks in a safe environment. This is especially useful for cybersecurity awareness training, education, and demonstration purposes.

## 📧 Email Scenarios

1. **Spear Phishing:**  
   Appears to come from the CEO, requesting an urgent wire transfer to a fraudulent account.

2. **Whaling:**  
   A fake legal notice urging the user to open a link to view a document regarding a supposed data breach.

3. **Social Engineering:**  
   A spoofed security alert that tricks users into "unlocking" their account via a phishing link.

Clicking any of these links leads to a failure page explaining the specific phishing tactic and why the email was malicious.

## 🛠️ Features

- Realistic inbox interface styled after Microsoft Outlook
- Interactive email views with simulated phishing links
- Custom failure pages with educational explanations
- Deployed and accessible publicly via Render

## 🚀 Running Locally

To run this simulation locally:

```bash
git clone https://github.com/AdamVahanvaty/phishing-simulation.git
cd phishing-simulation
pip install flask
python phishing_simulation.py
```
Open your browser and navigate to http://localhost:5000
