# ATS Resume Matching System

## Overview

The **ATS Resume Matching System** is an AI-powered tool designed to streamline the recruitment process by evaluating and ranking resumes against a job description. Leveraging advanced algorithms, this system ensures that recruiters can quickly identify the best candidates for a given job, optimizing the efficiency of the Applicant Tracking System (ATS).

## Features

- **Job Description Analysis**: Input a job description to analyze the required skills and qualifications.
- **Resume Evaluation**: Upload multiple resumes in PDF format for automated evaluation.
- **Top Matches**: Display the top matches based on the percentage of relevance to the job description.
- **Image Conversion**: Convert PDF resumes to images for detailed content extraction.
- **User-Friendly Interface**: Intuitive and easy-to-use interface built with Streamlit.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- Streamlit
- Other required libraries (listed in `requirements.txt`)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ats-resume-matching-system.git
    cd ats-resume-matching-system
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2. **Open your web browser and navigate to:**
    ```
    http://localhost:8501
    ```

3. **Input the job description:**
    - Paste the job description in the provided text area.

4. **Upload resumes:**
    - Upload the resumes in PDF format.

5. **View results:**
    - The top matching resumes will be displayed along with their relevance percentages.

## Project Structure

- `app.py`: Main application file containing the Streamlit interface.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Project documentation.


