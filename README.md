# personal-weather-dashboard_m_vijay


# Personal Weather Dashboard Introduction

A full-stack Django web app that lets users register, log in securely using JWT, set their location, and view real-time weather data powered by the OpenWeatherMap API.

---


## Features

-  **JWT Authentication** (access + refresh)
-  **User Location** stored in profile (used for weather queries)
-  **Weather API Integration** with dynamic dashboard
-  **Frontend Form Handling** with JavaScript for login, registration, and weather rendering
-  **Session Refresh** support using refresh tokens

---

## Project run
you can run the project from the github codespace without setup

# 1. Open your repo in Codespaces Click the green “Code” button in GitHub → “Codespaces” tab → “Create codespace on main”
wait until it install and configures from the terminal.

# 2. run the server
python manage.py runserver

# 3. open the browser and login and test it with superadmin credentials.
username: vijjuvolley1@gmail.com
password: Vijay@1234
# 4. or you can register with new location.


  #  ( OR ) manually setup into local environment and run
## 📁 Project Setup Instructions

1. **Clone the repository from the command line**

git clone https://github.com/yourusername/personal-weather-dashboard_Vijay.git
cd personal-weather-dashboard_Vijay

## 2. Create a virtual environment
python -m venv virt
source virt/bin/activate  # On Windows: virt\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt



# 4. Set/create up .env file (if using) inside paste 
OPENWEATHER_API_KEY=your_api_key_here
DEBUG=True
# 5. Run migrations to create database tables
python manage.py makemigrations
python manage.py migrate
# 6. Create a superuser (for admin access)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
# 8. Access the app at http://127.0.0.1:8000
# 9. Register/login and set your location to view real-time weather data

 # 10 Register a New User
Navigate to: http://127.0.0.1:8000/register/

Enter:

Email

Password & confirmation
country
Location (e.g., Hyderabad or Mumbai)

Submit and you’ll be redirected to login.

# 11 Login
Go to http://127.0.0.1:8000/login/

Enter your credentials

After successful login, you'll be redirected to /dashboard/

