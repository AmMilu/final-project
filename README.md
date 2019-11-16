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

    total pull requests number
    closed pull requests number
    assigned pull requests number
    
    assigned issues number  (contributor is not author)
    closed issues number    (contributor is not author)
    created issue number    (contributor is author)

    the commit number on this repo

# the impact calculation equation for each contributor
impact = 20 x total pull requests number / all pull requests number for repo +
         15 x closed pull requests number / total pull requests number +
         15 x assigned pull requests number / total pull requests number +

         15 x issues closed number / issues assigned number +
         15 x assigned issues number / total issues number +
         15 x issues create number / total issues number +

         10 x commits number / total commits number 
