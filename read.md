# 🚀 AI-Powered Selenium Automation Framework

A scalable Selenium-Python automation framework built using **PyTest**, **Page Object Model (POM)**, **Docker**, **Selenium Grid**, **REST API Testing**, and **AI-assisted Locator Healing**.

The framework is designed to automate both **UI** and **API** testing while maintaining high scalability, maintainability, and reusability.

---

# 📌 Project Overview

This framework was developed as an enterprise-style QA Automation framework rather than a collection of Selenium scripts.

It focuses on:

- Scalable Page Object Model architecture
- Cross-browser execution
- Parallel execution using Selenium Grid
- API + UI validation
- AI-assisted Locator Healing
- Dockerized test execution
- Allure Reporting
- Logging
- Reusable utilities

---

# ✨ Key Features

## UI Automation

- Selenium WebDriver
- Page Object Model
- Explicit Waits
- Reusable Base Page
- Driver Factory
- Cross Browser Support

---

## API Automation

- REST API Validation
- CRUD Operations
- Response Validation
- Status Code Validation
- Response Time Verification

---

## Reporting

- Allure Reports
- Screenshot Capture on Failure
- HTML Capture on Failure
- Framework Logs

---

## AI Assisted Automation

The framework includes an AI-assisted Locator Healing module.

When Selenium fails to locate an element:

```
Failed Locator
        ↓
Capture DOM
        ↓
Extract Important Elements
        ↓
Generate AI Prompt
        ↓
OpenAI Suggests New Locator
        ↓
Framework Validates Locator
        ↓
Retry Execution
```

> **Note:** This module is currently implemented as an experimental feature and is intended to demonstrate AI-assisted automation concepts.

---

# 🏗 Framework Architecture

> 📷 **Insert Architecture Diagram Here**

```
+----------------------------------------------------+
|                Test Cases (PyTest)                 |
+----------------------------------------------------+
                     |
                     ▼
+----------------------------------------------------+
|                 Page Objects (POM)                 |
+----------------------------------------------------+
                     |
                     ▼
+----------------------------------------------------+
|                   Base Page                        |
+----------------------------------------------------+
                     |
                     ▼
+----------------------------------------------------+
|               Driver Factory                       |
+----------------------------------------------------+
                     |
                     ▼
+----------------------------------------------------+
|      Selenium Grid / Local Browser Execution       |
+----------------------------------------------------+
```

---

# 📁 Project Structure

```text
project
│
├── ai/
├── api/
├── config/
├── fixtures/
├── pages/
├── tests/
├── utilities/
├── reports/
├── logs/
├── screenshots/
├── docker/
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| UI Automation | Selenium WebDriver |
| Test Framework | PyTest |
| Design Pattern | Page Object Model |
| API Testing | Requests |
| Reporting | Allure |
| Containerization | Docker |
| Parallel Execution | Selenium Grid |
| AI | OpenAI API |
| Version Control | Git / GitHub |

---

# ⚙️ Framework Flow

```
Test

↓

Page Object

↓

Base Page

↓

Driver Factory

↓

Browser

↓

Assertion

↓

Logs

↓

Allure Report
```

---

# 📸 Screenshots

## Project Structure

> 📷 Insert Screenshot

---

## Test Execution

> 📷 Insert Screenshot

---

## Allure Report

> 📷 Insert Screenshot

---

## Selenium Grid

> 📷 Insert Screenshot

---

## AI Locator Healing

> 📷 Insert Screenshot

---

# 🚀 Installation

Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running Tests

Run Complete Suite

```bash
pytest
```

Smoke Tests

```bash
pytest -m smoke
```

Regression

```bash
pytest -m regression
```

Parallel Execution

```bash
pytest -n auto
```

---

# 🐳 Docker Execution

Start Selenium Grid

```bash
docker-compose up -d
```

Run Tests

```bash
pytest
```

---

# 📈 Logging

The framework captures:

- Framework Logs
- Test Execution Logs
- Failure Logs
- API Logs
- Screenshot Paths
- HTML Capture
- Execution Time

Logs are automatically attached to the generated reports for easier debugging.

---

# 🤖 AI Locator Healing

The AI Locator Healing module is designed to reduce maintenance caused by UI locator changes.

Workflow:

```
Locator Failure

↓

Extract DOM

↓

AI Suggests Locator

↓

Validation

↓

Retry

↓

Execution Continues
```

---

# 🔮 Future Improvements

- Playwright Integration
- AI Generated Test Cases
- AI Bug Report Generator
- Cloud Execution
- Self-Healing Test Data
- Advanced Dashboard
- GitHub Actions

---

# 👨‍💻 Author

**Sapelly Sai Vivek**

QA Automation Engineer

GitHub:

LinkedIn:

Email:

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.