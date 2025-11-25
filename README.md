# 🌍 ISS Overhead Notifier

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![Checks Every](https://img.shields.io/badge/Interval-5_minutes-blueviolet.svg)]()
[![Visibility](https://img.shields.io/badge/Condition-Dark%20Only-black.svg)]()
[![Alerts](https://img.shields.io/badge/Email-Enabled-orange.svg)]()
[![ISS Tracker](https://img.shields.io/badge/Feature-ISS_Overhead-red.svg)]()

A simple Python application that emails you whenever the ISS is passing over your location **and** it's dark enough to see it. Runs every 5 minutes and notifies you in real time.

---


## Features

* Tracks the **real-time position** of the International Space Station
* Compares its latitude/longitude to your location
* Checks **sunrise/sunset** to ensure visibility
* Sends an **email alert** when the ISS is within ±5° of your position
* Runs continuously (every 5 minutes)
* Uses environment variables for security
* Lightweight: only two dependencies (`requests`, `python-dotenv`)

---

## 📁 Project Structure

```
iss-overhead/
│
├── main.py              # Main script
├── requirements.txt     # Project dependencies
├── .gitignore           # Ensures .env stays out of GitHub
└── README.md            # You're reading it!
```

> **Note:** Your `.env` file should live alongside `main.py` but will not be committed to Git.

---

## 🔧 Setup

### 1. Clone the repository

```bash
git clone https://github.com/lesliejohnson-io/iss-overhead.git
cd iss-overhead
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file (NOT committed to GitHub)

In the project directory, create a file named `.env`:

```
MY_EMAIL=yourgmail@gmail.com
MY_EMAIL_PASSWORD=your_app_password
SEND_TO_EMAIL=where_to_send_notifications@gmail.com
```

### 4. Generate a Gmail App Password

Gmail requires App Passwords for SMTP.

Steps:

1. Go to **[https://myaccount.google.com/security](https://myaccount.google.com/security)**
2. Enable **2-Step Verification**
3. Open **App Passwords**
4. Choose “Mail” → “Your Device”
5. Copy the 16-character password into your `.env` file

---

## ▶️ Running the Script

Run the script using:

```bash
python main.py
```

The program will:

* Sleep 300 seconds (5 minutes)
* Check ISS position
* Check if it’s dark
* Send an email if both conditions are met

This continues **indefinitely** until you stop it.

---

## 🌓 How it Works

### 1. Check ISS Position

Using the `open-notify` ISS API:

```http
http://api.open-notify.org/iss-now.json
```

### 2. Compare Locations

If ISS latitude/longitude is within **±5°** of your coordinates → overhead.

### 3. Check Nighttime

Uses the Sunrise-Sunset API:

```http
https://api.sunrise-sunset.org/json
```

If current time is **after sunset OR before sunrise**, it's dark enough.

### 4. Send Email

Using Gmail’s SMTP server:

```python
smtplib.SMTP("smtp.gmail.com", port=587)
```

---

## ⏱ Running Automatically (Optional)

### **Mac/Linux (cron job):**

```bash
crontab -e
```

Add:

```
*/5 * * * * /usr/bin/python3 /path/to/main.py
```

### **Windows (Task Scheduler):**

1. Open *Task Scheduler*
2. Create a new task
3. Trigger: **Every 5 minutes**
4. Action: Run `python main.py`

---

## 🛰 APIs Used

| Purpose        | API                                                                                |
| -------------- | ---------------------------------------------------------------------------------- |
| ISS Position   | [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json) |
| Sunrise/Sunset | [https://api.sunrise-sunset.org/json](https://api.sunrise-sunset.org/json)         |

---

## 🛡 Security Notes

* Do **NOT** commit your `.env` file
* Always use a **Gmail App Password**, not your real password
* Your `.gitignore` already prevents `.env` from being pushed

---

## 📬 Email Example

You’ll receive:

```
Subject: ISS Overhead!

Go outside and look up!
```

---

## ⭐ Future Enhancements (Optional Ideas)

* SMS notifications (Twilio)
* Desktop notification
* Push notification to your phone
* GUI dashboard
* Map visualization
* Logging flyovers to a database

---
