# Auto Recruit AI

Auto Recruit AI is a conversational chatbot system designed to automate the recruitment process using artificial intelligence. This application allows users to simulate recruitment interviews, providing assistance with resume screening, candidate evaluation, and job-fit matching. It leverages state-of-the-art machine learning models and language processing techniques to facilitate seamless interactions.

## Features

- **Chat Interface**: Engages with candidates through a conversational interface.
- **Resume Analysis**: Parses and analyzes resumes to extract relevant skills, experience, and other important details.
- **Interview Simulation**: Conducts virtual interview sessions to assess candidates.
- **ML Models**: Includes pre-trained machine learning models for natural language processing.
- **Data Storage**: Store and retrieve past interview data for future analysis.
- **Customization**: Flexible system to adapt to different industries and job roles.
- **Deployed on Flask**: Backend built using Flask, providing robust and scalable API endpoints.

## Directory Structure

The project is structured as follows:

```
AutoRecruit/
├── .gitignore                   # Files and folders ignored by Git
├── app.py                       # Main Flask application
├── model/
│   ├── instructions.txt         # Instructions or metadata for the ML models
│   └── model.ipynb              # Jupyter Notebook containing ML model development
├── research/
│   └── trials.ipynb             # Jupyter Notebook for research and experimentation
├── requirements.txt             # Python package dependencies
├── setup.py                     # Setup file for Python packaging
├── src/
│   ├── __init__.py              # Package initialization
│   ├── helper.py                # Helper functions for the application
│   └── prompt.py                # Handles prompts for chatbot interaction
├── static/
│   ├── robot-chat-bot-concept-illustration-vector.jpg  # Illustration for the interface
│   └── style.css                # CSS styling for the front-end
├── store_index.py               # Stores index data or session details
├── template.py                  # Flask template rendering logic
├── templates/
│   └── chat.html                # Front-end chat interface template
└── README.md                    # Project overview and instructions (this file)
```

## Installation and Setup

### Prerequisites

- **Python 3.9+**
- **Flask** (for the web server)
- Other dependencies as listed in `requirements.txt`

### Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Huzaifaaazhar/AutoRecruit.git
cd AutoRecruit
```

### Virtual Environment Setup (Optional)

It is recommended to create a virtual environment:

```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### Install Dependencies

Install all required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Running the Application

Once dependencies are installed, you can run the Flask application:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/` by default.

## Usage

1. **Open the Application**: Once the app is running, open a web browser and navigate to `http://127.0.0.1:5000/`.
2. **Chat Interface**: The main page provides a chat interface where you can interact with the AI chatbot.
3. **Customize Models**: You can adjust the underlying ML models by editing the `model.ipynb` file.
4. **Storage**: Data from conversations and recruitment sessions will be stored and can be retrieved for analysis.

## Customization

To modify or extend the system, you can:

- Update the **ML models** in `model/model.ipynb`.
- Add new **prompts** or interview scenarios by editing `src/prompt.py`.
- Customize the **front-end** by modifying `templates/chat.html` and `static/style.css`.

## Dependencies

This project relies on several key libraries and frameworks. All dependencies are listed in the `requirements.txt` file, and include:

- **Flask**: A lightweight WSGI web application framework.
- **TensorFlow**: Machine learning framework for handling deep learning tasks.
- **Torch**: Another framework used for building and training machine learning models.
- **scikit-learn**: A Python module for machine learning.
- **HuggingFace Transformers**: NLP models and utilities for language processing.
- **Sentence Transformers**: Pre-trained transformers for embeddings and NLP.
- **LangChain**: Framework for working with LLMs (Large Language Models).
- **Pandas**: Data manipulation and analysis tool.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Future Work

- **API Integration**: Add APIs to integrate with third-party HR systems.
- **Advanced ML Models**: Upgrade to more sophisticated models for better accuracy in interviews and analysis.
- **Docker Support**: Provide Docker support for easier deployment.
- **Authentication**: Implement user authentication for secure access to the platform.
