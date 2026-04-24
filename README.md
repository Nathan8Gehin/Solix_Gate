# Automated Solar Panel system

## Project Goal
This project aims to simplify and automate the retrieval and management of official French administrative documents (such as the *Attestation de droits Ameli* and *Criminal Record Bulletin No. 3*). 

The application provides a centralized interface for users to initiate requests, track administrative processing times, and securely store digital copies of their documents, ensuring they are always up-to-date for employers or educational institutions.

## Technical Context
The system is built to handle asynchronous administrative workflows. It manages the lifecycle of a document request from the initial user input to the final PDF download, specifically addressing the validation delays inherent in government portals.

## Features
- **Automated Workflow:** Streamlined process for requesting official documents.
- **Validity Monitoring:** Automatic tracking of document expiration dates (e.g., the 3-month validity rule for criminal records).
- **Secure File Management:** Local or cloud-based storage of sensitive administrative PDFs.

## Credits & Dependencies
This project utilizes the **Gemkick API** to handle complex document processing and data retrieval within the Google Workspace environment.

* **API Used:** Gemkick Corpus API
* **Source:** [https://github.com/google-gemini/gemkick](https://github.com/google-gemini/gemkick)

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
