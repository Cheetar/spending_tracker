Spending tracker
===========
Django-based web application for tracking, managing and analysing your expenses

### Technology and features
- Python 3.5.2
- Bootstrap 3.6
- Cookie banner (https://github.com/dobarkod/cookie-banner)

### Installation
- Download this repo `git clone https://github.com/Cheetar/spending_tracker.git`
- Enter project's directory `cd spending_tracker`
- Setup virtual environment `virtualenv venv`
- Activate the virtual environment `source venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Create an .env file with custom settings suiting your needs (you can update .env.example accordingly and save it as .env)
- Migrate data to database `python manage.py migrate`
- Create admin account `python manage.py createsuperuser`
- Start the app `python manage.py runserver`

### Live
- The app runs live here: www.spendalizer.com

### Screenshots

![Dashboard](https://github.com/Cheetar/spending_tracker/blob/master/src_dashboard.png)
