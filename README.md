# TAMUSA-ACM Website Repository

## Overview

Welcome to the official repository for the Texas A&M University-San Antonio ACM (Association for Computing Machinery) chapter website. This project is built using the Flask micro-framework, leveraging Bootstrap for responsive design and custom CSS to create a dynamic and engaging user interface. The website is designed to be a resource and community hub for web development and design enthusiasts at TAMUSA.

### Project Structure

The project is structured as follows:

- `app/`: Contains the Flask application and the routing logic.
- `templates/`: Holds the HTML files which are rendered by the Flask app.
- `static/`: Stores static files like CSS, JS, and images used in the web application.
- `config.py`: Configuration file for the Flask app.
- `run.py`: The entry point for the Flask application.

## Setup and Installation

To get this website running locally on your machine, you will need Python installed along with the Flask framework and other dependencies.

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/tamusa_acm_org.git
    cd tamusa_acm_org
    ```

2. **Setup a Virtual Environment** (Optional but recommended)

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**

    ```bash
    python run.py
    ```

    Visit `http://127.0.0.1:5000/` in your web browser to view the app.

## Usage

After installation, the web application will be accessible locally. You can navigate through various sections designed to provide information and resources related to web design and development. The UI is responsive, making it accessible on a variety of devices.

## Contributing

Contributions to the TAMUSA-ACM website are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.

### Contribution Guidelines

- **Code Style**: Follow the existing code style in the project. Use descriptive variable names and keep the code clean and well-commented.
- **Commit Messages**: Write meaningful commit messages that clearly explain the changes you have made.
- **Pull Requests**: Provide a description of the changes in the pull request. Link to any relevant issues addressed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

---

By contributing to the TAMUSA-ACM website repository, you agree to adhere to its code of conduct and the terms of its license. For any questions or to get more involved with the TAMUSA ACM chapter, please reach out via our official channels.