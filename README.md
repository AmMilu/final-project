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
impact = 25 x merged pull requests number / all repo pull requests number +
         15 x assigned pull requests number / all repo pull requests number +

         20 x issues closed number / issues assigned number +
         15 x assigned issues number / total issues number +
         15 x issues create number / total issues number +

         10 x commits number / total commits number 

impact = 1000 x impact (some of the results are really small, this is to make the number clearer)
