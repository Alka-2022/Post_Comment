# Post-Comments Service

## Overview
The Post-Comments Service is a web application built with Flask that enables users to create posts and add comments to existing posts. It offers a user-friendly interface for managing posts and comments stored in a database.

## Architecture
The application follows a client-server architecture:
- **Client Side**: Utilizes HTML, CSS, and JavaScript to create the user interface.
- **Server Side**: Implemented with Python and Flask to handle HTTP requests and interact with the database.

## Features
- Create new posts with custom text.
- Add comments to existing posts.
- Supports basic text formatting (bold, italics, hyperlinks) in comments.

## Setup and Run
To set up and run the application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd post-comments-service
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. Initialize the Database:
   Execute the create_tables() function in app.py to create the necessary database tables.

4. **Run the Application**:
   ```
   python app.py
   ```
   
5. Access the Application:
   Open your web browser and navigate to http://127.0.0.1:5000 to access the application.


## Special Instructions
- Ensure Python is installed on your system.
- The application utilizes an SQLite database, eliminating the need for additional database setup.
- JavaScript enhances the user interface and provides dynamic functionality.

  
## Dependencies
- Python (3.x recommended)
- Flask
- Flask-SQLAlchemy
