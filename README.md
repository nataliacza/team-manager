# SAR Team Manager

Since 2015 I'm member of OSP Gdansk :fire_engine: (Ochotnicza Straz Pozarna / Volunteer Fire Department). Our specialization is 
search for missing persons using trained and certified dogs :service_dog: . Each formalized group struggles with the same issues - 
a lot of members, numerous deadlines, plenty of data that you need to store somewhere, not to mention how to manage
all those things together.

Why not to create some tool, which could manage everything in one place?

Main goal of this project is to create all-in-one tool, that would help to manage small organizations.

_**SAR** stands for Search and Rescue._

### Concept and functionalities

Application would be available only for limited users, which are involved in team management (chief or manager).

Features:
- Member list with basic information.
- Member detail page.
- Dog list with details.
- Equipment list with useful information.
- CRUD for above-mentioned.


### Run project

1. Clone the repository: `git clone https://github.com/nataliacza/team-manager`.
2. Create new file `.env` in main directory and fill with variables as per `env.example` file.
3. Create virtual environment using `poetry` and install all dependencies.
4. Run migrations `python manage.py migrate`.
5. Create superuser `python manage.py createsuperuser`, provide at least username and password.
6. Run server `python manage.py runserver`.
7. Add some members or dogs via endpoints or admin panel.
