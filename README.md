Compound Interest Calculator

Project Overview

The Compound Interest Calculator is a web-based application that calculates compound interest and visualizes the growth of investments over time. Users can input initial deposit, interest rate, periodic contributions, compounding frequency, and time period to receive detailed results, including:

Final amount with interest.

Difference from contributions without interest.

Growth comparison chart over time.

This project is built using Python and Flask for the backend, with HTML, CSS, and Matplotlib for the frontend and data visualization.

Features

Interactive Form: Users can input investment details and instantly see calculated results.

Dynamic Visualization: A comparison chart displays growth with and without compound interest.

User-Friendly Interface: Clean and responsive design for seamless user experience.

Custom Styling: Designed with CSS for an intuitive and visually appealing layout.

Folder Structure

current/
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── index.html
│   └── result.html
├── app.py

File Descriptions

app.py: Main application logic, handles user input, performs compound interest calculations, and generates dynamic charts.

static/css/style.css: Contains CSS styles for the application interface.

templates/index.html: Input form for user data.

templates/result.html: Displays the calculation results and growth chart.

Setup Instructions

Clone the Repository:

git clone repository-url>](https://github.com/sunnyaquostic/Finance-Visualizer
cd current

Set Up Virtual Environment (Optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install Dependencies:

pip install flask matplotlib

Run the Application:

python app.py

Access the Application:
Open your web browser and go to http://127.0.0.1:5000.

How to Use

Navigate to the home page.

Fill out the input form with:

Initial Deposit

Interest Rate

Contribution Amount

Compounding Frequency (Monthly/Annually)

Time Period (Years)

Click the Calculate button.

View the calculated results and growth chart on the results page.

Technologies Used

Backend: Python, Flask

Frontend: HTML, CSS

Data Visualization: Matplotlib

Future Enhancements

Add support for additional currencies and localization.

Include more compounding frequency options (e.g., weekly, daily).

Save user input and results for future reference.

Implement user authentication for personalized dashboards.

Acknowledgements

Special thanks to the open-source community for tools and libraries that made this project possible. If you have feedback or suggestions, feel free to reach out!

License

This project is licensed under the MIT License. Feel free to use, modify, and share!

