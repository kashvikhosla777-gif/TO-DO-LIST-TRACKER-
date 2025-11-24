# TO-DO-LIST-TRACKER-
A simple, Python-based Task Management System allowing users to add tasks, edit them, delete, and set due dates, categories, and priorities. It includes reminders, which also provide updates on task status, summaries, and the saving of files for persistence. Ideal for those learning the basics of Python.

TO DO LIST TRACKER 

Overview
This project constitutes a menu-driven Task Management and Reminder System developed in Python, which provides the necessary facilities to users for creating, viewing, updating, and deleting tasks in an organized manner. Each task will be associated with due dates, categories, and priority levels for efficient work management.
This program stores tasks in a list and provides many useful functions for marking tasks as completed, reviewing tasks that are overdue, and displaying a summary of all tasks. For added continuity, the tasks can also be saved to a file that can be later loaded into the program. This project has the purpose of assisting users to be organized, boost their productivity, and never miss any important deadlines using simple and user-friendly ways.


Features  
1.	Add New Tasks
Users can create a new task by filling in the details like task name, due date, category, and priority level. This helps in organizing tasks based on their importance and deadline.
2.	View Task List
The system outlines all tasks saved in a structured numbered format, making it easy to review what a user may have pending or even what they have completed.
3.	Edit Existing Tasks
Users can modify previously saved task details if there is any change in schedule or priority, thus ensuring flexibility and accuracy.
4.	Delete Tasks
Tasks that are unwanted or completed can be permanently removed from the list, thus keeping the record of tasks neat and current.
5.	Mark Tasks as Completed
The system allows users to change the task status from "not done" to "done" once it is finished, making the tracking of progress easier.
6.	Check Reminders for Due or Overdue Tasks
The system will compare due dates to the current date and will highlight tasks that need immediate attention.
7.	Task Count Summary
Displays the total number of tasks along with the count of completed and pending tasks, giving a quick overview of the user's productivity.
8.	Save Tasks to File
All tasks can be saved to a text file so the data remains available even after the program has been closed.


Tools and Techniques used
Menu-driven programming: This programming style offered the user the navigation to move back and forth between the different features.
 String Manipulation: String manipulation was a simple approach to keep the task information organized in a single string for the task details.
Input checking: Input checking was implemented for checking whether the user provided all the information required and if the data was in the accepted range.
 Modular Programming: Each of the three features, were coded as their module to keep a simpler clean module.
 Testing: Some tests were done manually to run the required feature, run per the length of data to check edge cases. mapping Test to output to 
reliability.


Steps to install and Run the program 
1.	Install Python
o	Download and install Python from the official website (python.org) and ensure “Add Python to PATH” is enabled.
2.	Save the Program File
o	Copy the code into a text editor or IDE and save it with a .py extension (e.g., todo.py).
3.	Open the Program Directory
o	Go to the folder where the file is saved.
4.	Run the Program
o	Open a terminal or command prompt and type:
o	python todo.py
o	Or run directly using IDLE, VS Code, or PyCharm.
5.	Use the Menu
o	Follow on-screen menu options to add, edit, delete, view, or save tasks.


     Instructions for Testing 
1.	Run the program and check if the main menu displays correctly.
2.	Add a few tasks and verify they appear in the task list.
3.	Edit a task and confirm the changes are correctly updated.
4.	Delete a task and check if it is removed from the list.
5.	Mark a task as completed and ensure its status updates.
6.	Use the reminder option to check due or overdue tasks.
7.	Check task summary to confirm counts for total, completed, and pending tasks.
8.	Save and exit, then verify that the tasks.txt file is created and contains the correct data.

