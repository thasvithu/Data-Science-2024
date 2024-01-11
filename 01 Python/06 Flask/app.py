# Import the Flask class to create web applications
from flask import Flask

# Create a Flask application instance
# __name__ is a special variable that tells Flask where the app is located
app = Flask(__name__)

# Define a route for the root URL (/) using a decorator
@app.route('/')  # This line decorates the 'welcome' function below
def welcome():
    return "Welcome to Flask 2024.01.11"

# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for easier development


"""
1. **Import:**
   - `from flask import Flask`: Imports the Flask class for creating web applications.

2. **Application Creation:**
   - `app = Flask(__name__)`: Creates a Flask application instance named `app`.
    - `__name__` is a special Python variable that ensures the app is configured correctly based on how it's executed.

3. **Route Definition:**
   - `@app.route('/')`: This decorator associates the function `welcome` with the root URL (/) of the application.
    - When a user visits `http://localhost:5000/` (the default address), this function will be called.

4. **Welcome Function:**
   - `def welcome():`: Defines a function named `welcome`.
   - `return "Welcome to Flask 2024.01.11"`: Returns the string "Welcome to Flask 2024.01.11" as the response to the user's request.

5. **Running the Application:**
   - `if __name__ == "__main__":`: Ensures the code only runs when the script is executed directly (not imported as a module).
   - `app.run(debug=True)`: Starts the Flask development server with debug mode enabled.
     - Debug mode provides helpful error messages and automatic code reloading for easier development.

**Key Points:**

- Flask uses a modular approach, where you define routes and their associated functions to handle different URLs.
- The `@app.route()` decorator is a convenient way to link functions to specific URLs.
- The `app.run()` method starts the development server, making your application accessible in a web browser.

I hope this explanation is helpful! Feel free to ask if you have any further questions.

"""
