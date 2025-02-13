# 🔍 About the Project

CodeAnalyzer is a **Django-based** application designed to perform **Static Application Security Testing (SAST)** on public **GitHub** and **GitLab** repositories. Future updates will introduce additional security testing methodologies, such as **Software Composition Analysis (SCA)** and **Dynamic Application Security Testing (DAST)**, along with enhanced security scoring and reporting features.

*🚀 This project has not been publicly deployed yet.*

# ⚙️ Installation Guide

### Default Configuration:

- **Django Server:** `Port 8000`

- **Debugpy:** `Port 5678`

- **PostgreSQL:** `Port 5432`

- **Volume Mapping:** `C:/Projects/CodeAnalizer:/opt (modifiable in docker-compose.yml)`

## 🖥️ Windows Installation

Clone the repository:

###### `git clone https://github.com/Joshbv6/CodeAnalizer.git`
####

Run the installation script by double-clicking *install.bat*.

This will execute Docker commands to set up and launch the application.

## 🐧 Linux Installation

Clone the repository:

###### `git clone https://github.com/Joshbv6/CodeAnalizer.git`
####

Run the installation script:

###### `chmod +x install.sh && ./install.sh`
####

This will execute Docker commands to set up and launch the application.

## 🛠️ Manual Installation

For those preferring manual setup:

Clone the repository:

###### `git clone https://github.com/Joshbv6/CodeAnalizer.git`
####

Navigate to the Docker folder:

###### `cd CodeAnalizer/Docker`
####

Build the Docker image:

###### `docker build -t codeanalizer_image .`
####

Run the container using Docker Compose:

###### `docker-compose -p codeanalizer_project up -d`
####

Once the container is running, open your browser and go to: [http://localhost:8000](http://localhost:8000).

## 🚀 How It Works

Currently, the application supports **Static Application Security Testing (SAST)**:

Users submit a URL (GitHub/GitLab public repositories only).

The system runs a SAST scan and displays the results.

Future updates will expand this functionality.

## 🔮 Roadmap & Planned Features

### ✅ Planned Enhancements:

- Software Composition Analysis (SCA)

- Dynamic Application Security Testing (DAST)

- User authentication & account management

- Queued analysis for better user experience (no waiting for results)

- Database integration for storing past analysis results

- Downloadable reports (JSON, XML, etc.)

- Public API for external system integration

###  🆕 Upcoming Features:

- Security Scoring System

- Assess repositories based on CVSS (Common Vulnerabilities Scoring System) and CVE (Common Vulnerabilities and Exposures).

- Provide an intuitive score to evaluate repository security risks.

- Bug Hunting & Code Smells Analysis (Tentative)

- Penetration Testing (Tentative – requires feasibility evaluation)

- Some of these features may present unforeseen technical challenges, and their implementation will be assessed for feasibility.


## 📬 Contact

For questions or feedback, feel free to reach out via GitHub issues.

*🎯 Stay tuned for updates and security improvements! 🚀*