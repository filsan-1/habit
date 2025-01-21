# Habit Tracker

**Habit Tracker** is a web application designed to help you build, track, and maintain habits while achieving personal goals. The app makes habit tracking fun and engaging by visualizing your progress with interactive streaks and progress bars powered by **D3.js**. It’s perfect for anyone looking to stay consistent, monitor their growth, and celebrate milestones.
### Monitor Streaks and Progress Bars
**Important:** To use streaks and progress bars, you must create a task for the current day, complete it, and then revisit your analytics page. Only then will your streaks and progress start appearing.


log in using 
k - username 
CgrF6WJ9WBAY26i- password 
for better data visualisation or you can create new account
---

## 🚀 Features

### 🔒 User Authentication and Personalization
- Create an account or log in to start tracking your habits.
- Access a personalized dashboard with all your active habits and progress.

### 📋 Habit Tracking Made Simple
- Add habits effortlessly by specifying goals, frequency, and timeframes.
- Automatically generated tasks help you stay on top of your habits.
- Track streaks and consistency for each habit.
- Delete habits when they’re no longer relevant (removing related data automatically).

### 🎯 Motivation Through Analytics
- See detailed stats like active habits, streak lengths, and goal completion percentages.
- Earn badges and achievements for hitting streak milestones or completing tasks.
- Keep track of your progress with beautifully crafted, interactive charts powered by **D3.js**.

### 📊 Data Visualization with D3.js
- **Streaks**: Visualize your consistency over time with dynamic streak charts that update in real time.
- **Progress Percentages**: See how close you are to achieving your habit goals at a glance.
- **Interactive Visualizations**: Turn habit tracking into an enjoyable, interactive experience.

### 👤 User Profile
- View a snapshot of your progress, including active habits, streaks, and achievements.

---
run using docker and the commands or
## 📦 Installation

### 1. Clone the Repository
Download the project to your local machine:
```bash
git clone https://github.com/filsan-1/habit.git
cd habit
```

### 2. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Configure the Database
cp local_settings.example.py local_settings.py**SQLite**,

### 4. Apply Migrations
Prepare the database:
```bash
python manage.py migrate
```

### 5. Run the Development Server
Start the app locally:
```bash
python manage.py runserver
```

### 6. Access the Application
Open your browser and go to:
```plaintext
http://localhost:8000
```

---

## 🌟 How to Use

### Register or Log In
- Sign up or log in to create a personalized space for tracking your habits.

### Add and Manage Habits
- Go to the **Add Habit** page to create new habits by specifying details like name, frequency, and goals.
- Use the **Habit Manager** to view, edit, or delete existing habits.

### Track Tasks and Mark as Complete
- View your tasks for today or the future on the home page.
- Mark tasks as completed with a single click.

### Monitor Streaks and Progress Bars
**Important:** To use streaks and progress bars, you must create a task for the current day, complete it, and then revisit your analytics page. Only then will your streaks and progress start appearing.

---

## 🎉 Why Choose Habit Tracker?

Habit Tracker isn’t just a tool; it’s a motivational companion that helps you stay consistent and achieve your goals. With interactive charts, detailed analytics, and a focus on user experience, tracking your habits has never been easier—or more fun. Start building habits today, and let Habit Tracker help you make them stick! 🚀

--
