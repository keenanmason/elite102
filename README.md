# Python SQLite Project

This project is a simple Python application that interacts with an SQLite database. It serves as a demonstration of how to set up a Python project with SQLite and includes basic functionality for database operations.

## Project Structure

```
python-sqlite-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── database
│   │   └── db_setup.py  # Database setup and initialization
│   └── models
│       └── __init__.py  # Data models for the application
├── requirements.txt      # Project dependencies
├── .devcontainer
│   ├── devcontainer.json # Development container configuration
│   └── Dockerfile        # Docker image setup
├── .vscode
│   └── settings.json     # VS Code settings
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-sqlite-project
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can start the application by running:
   ```
   python src/main.py
   ```

## Usage

- The application initializes a connection to the SQLite database and allows for basic CRUD operations.
- Modify the `src/database/db_setup.py` file to customize the database schema and initial data.

## Development

This project is set up to be used with a development container. You can open it in a containerized environment by using the `.devcontainer` configuration.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.