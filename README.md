<p align="center">
  <img src="https://raw.githubusercontent.com/echechelev/cassandra-framework/main/assets/evknopia-banner.png" alt="Evknopia - Cassandra Framework" width="300">
</p>

<h1 align="center">Cassandra Framework</h1>
<p align="center">
  <strong>QA Automation Framework for Colonization Assessment System</strong><br>
  <em>Built with love by Evgenii Chechelev & his space cat 🐱🚀</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Selene-orange.svg" alt="Selene">
  <img src="https://img.shields.io/badge/Runner-pytest-purple.svg" alt="pytest">
  <img src="https://img.shields.io/badge/Reports-Allure-green.svg" alt="Allure">
</p>

---

## 🌌 About

**Cassandra** is a comprehensive, architecturally sound test automation framework designed for a static web application (Colonization Assessment System). 

This project is a full-cycle demonstration of SDET capabilities: from system analysis and technical specification writing to frontend development, test architecture, and automation. It proves that robust QA engineering can be achieved even in a backend-less, mock-driven environment.

## 🚀 Key Architectural Features

- **Strict Page Object Model (POM)**: Modular design with fluent interface (`return self`), centralized locators, and built-in custom exception handling.
- **Ironclad Locators**: Exclusive use of `data-wm-id` attributes for resilient, DOM-independent UI targeting.
- **12-Factor App Configuration**: Environment-driven `BASE_URL` (local file system or GitHub Pages) via `os.getenv`.
- **AAA Pattern in Tests**: Clear separation of Arrange, Act, and Assert with rich Allure step detailing.
- **Mock-Driven Development**: Fully functional frontend authentication emulated via `localStorage` and `data.js`, eliminating external dependencies.

---

## 📦 Module 1: Login Page (Authorization)

The first completed module of the framework, showcasing end-to-end quality assurance.

### ✨ Features & Advantages

- **Reactive Validation**: The "Establish Connection" button remains `disabled` until strict minimum length requirements are met (Callsign ≥ 3, Access Code ≥ 4).
- **Real-time Input Sanitization**: Cyrillic characters are blocked in Callsign; Access Code strictly accepts only Latin letters, numbers, and underscores.
- **UX/UI State Tracking**: Automated verification of complex state transitions, including a 3-second simulated network delay, button pulsing animations, and dynamic Telemetry color changes (Blue → Green/Red).
- **Security by Obscurity**: Generic error messages prevent user enumeration.
- **Comprehensive Coverage**: 15 distinct CAS (Cassandra Automation Scenarios) covering basic flows, negative validation, edge cases, and basic security payloads.

---

## 🗂️ Project Structure

```
cassandra/
├── app/                        # Static frontend application (HTML/CSS/JS)
├── assets/                     # Global project assets (images, GIFs, banners)
├── data/                       # Frontend mock data (JS/JSON configurations)
├── docs/                       # Project documentation
│   └── login_page/             # Login Page specific documentation
│       ├── assets/             # Images and GIFs for Login Page
│       ├── design/             # Mockups and screenshots for Login Page
│       └── specification/      # Technical Specification for Login Page
├── pages/                      # Page Object Model implementation
│   └── login_page/             # Locators and methods for the Authorization page
── tests/                      # Automated test suites
│   └── test_login/             # Authorization page test modules
│       ├── data/               # Test data (demo credentials, constants)*
│       ├── test_basic.py       # Basic flow and reactivity tests
│       ├── test_edge_cases.py  # Boundary values and security tests
│       └── test_validation.py  # Negative scenarios and length validation
└── README.md

```


*Note: Test credentials are stored in plain text within the tests/test_login/data/ directory. This is an intentional design choice for this educational, backend-less mock project to ensure transparency and ease of demonstration. In a production environment, secrets would be managed via secure vaults.*




## 🔧 Tech Stack

- **Language**: Python 3.11+
- **Test Runner**: pytest
- **Automation Library**: selene (modern Selenium wrapper)
- **Reporting**: allure-pytest
- **Code Quality**: black, isort, flake8
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Hosting**: GitHub Pages (planned)

## 🚧 Status

**Active Development** — Core architecture and Login Page automation (Module 1) are completed and ready for review. Documentation, design assets, and subsequent modules (Registration, Forgot Password, Landing) are actively being structured.

*By Evknopia | QA Automation Engineer | Turning coffee into clean code & reliable tests ☕🛠️*