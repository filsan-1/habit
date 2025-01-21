Habit Tracker
Habit Tracker is a web application designed to help users track and manage their habits, complete tasks, and monitor their progress toward personal goals. The app visualizes data through streaks and progress percentages, leveraging D3.js to provide dynamic, interactive visualizations of users' consistency and growth over time.

This README outlines the project’s features, installation instructions, and usage guidelines.

Installation
To install and run Habit Tracker locally, follow these steps:

1. Clone the Repository
Clone the project repository to your local machine:

bash
Copy
Edit
git clone https://github.com/filsan-1/habit.git
cd habit
2. Install Dependencies
Install the required Python dependencies using pip:

bash
Copy
Edit
pip install -r requirements.txt
3. Database Configuration (SQLite)
The app uses SQLite by default, so if you have SQLite installed, you're all set! No additional configuration is required for the database.

4. Apply Database Migrations
Run the following command to apply the necessary database migrations:

bash
Copy
Edit
python manage.py migrate
5. Run the Development Server
Start the Django development server:

bash
Copy
Edit
python manage.py runserver
6. Access the Application
Once the server is running, you can access the application in your web browser at:

arduino
Copy
Edit
http://localhost:8000
Features
User Authentication and Registration
Users can create accounts, log in, and track their habits with ease.
Habit Tracking
Add and delete habits easily.
Tasks are automatically generated based on your habit goals, frequency, and time period.
Track streaks for each habit to maintain consistency.
Earn achievements for hitting streak milestones or completing tasks.
Analytics
View detailed analytics on your habit progress, including active habits, streak lengths, and progress toward your goals.
The app visualizes your progress with streaks and percentages, helping you stay motivated and on track.
D3.js powers the visualizations, providing dynamic, interactive, and customizable charts to bring your progress to life.
User Profile
Your personalized profile displays your active habits and key habit-related information.
Usage
Once the application is running, you can perform the following actions:

Register/Login
Create an account or log in to start tracking your habits.
Add Habits
Navigate to the "Add Habit" page and input details about your habit, such as its name, frequency, and goals.
View and Mark Tasks as Completed
On your home page, view tasks due today or in the future.
Mark tasks as completed with a single click.
Monitor Progress
Track your progress via the analytics page, where you can see streak lengths, progress percentages, and achievements.
Visualize your progress using D3.js-powered charts, making it easy to stay motivated.
Habit Manager
The Habit Manager page displays all your tracked habits.
You can view detailed logs of task completion, streak history, and achievements.
You also have the option to delete habits, which will remove the associated tasks, streaks, and achievements.
Data Visualization with D3.js
Streaks and Progress Percentages
Streaks: The app visualizes your progress through streaks, showing how consistent you've been with each habit over time. These visual representations help users stay motivated by providing a clear and engaging way to track progress.

Progress Percentages: Along with streaks, the app displays your progress toward habit goals as percentages. This allows users to see how close they are to achieving their targets, providing an extra push to stay on track.

D3.js Features
By using D3.js, the app offers rich, interactive data visualizations. These streaks are customizable and dynamically updated, allowing users to interact with their progress data in **real-time.**
The visualizations turn habit tracking into an enjoyable experience, not just an informative one.
