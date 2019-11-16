# final-project
The final project of software engineering

# requirement
pip install PyGithub

# description
This project is to compare each contributor's impact on a specific repo. An equation is created to measure the impact.

# data collection
Data collected for a specific repo:
    contributors' names
    the total pull requests number
    the total issues number
    the total commits number

Data collected for each contributors:
    the pull requests number
    the open pull requests number
    the closed pull requests number
    the merged pull requests number
    the total assigned issue number (this contributor is the assignee of the issue)
    the open assigned issue number
    the closed assigned issue number
    the commit number on this repo

# the impact calculation equation for each contributor
impact = 30 x total pull requests number/all pull requests number for repo +
         25 x closed pull requests number/total pull requests number +
         25 x issue closed number/issue assigned number +
         20 x commits number/total commits number 
