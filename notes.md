# How to create projects
## The First Project We Did
1. Select dataset 
2. Make repository 
    - add readme file as description
    - create repository
I have to add a description to Tell myself what I want to do with that dataset
I have to copy the ssh url as opposed to the https because the ssh key is already authenticated (the https key isn't)
3. In your Terminal, clone repository
    - default terminal is arch
    - clone name of the repository
4. inside repository folder, create data folder
    - paste data into here
5. sync repo
    - git add .
Stages all changes you made (like waiting for the bus station)
    - git commit -m "commit message"
m : message. Explains what you are pushing to github (like entering the bus)/(Giving yourself a note) 
    - git push 
Pushes changes to github (like riding the bus).
6. create a new project folder in your google drive 
    - create data folder 
    - paste data inside data folder
    - create google colab
i'll Name it main because There will be different colabs, so when I name it main, I'll be able differentiate between them
7. open file that you just created
    - optional: name current file main 
    - mount G drive
    - coding the template  
        - `import pandas as pd`
        - `df = pd.read_csv('file_path')`
        - `df.head()`
8. optional: push colab to github 
In order to push to github, your repository has to be public

## for converting csv file to sqlite database
1. in the terminal, run:
    - navigate to where data is 
    - sqlite3 <NameOfDB.sqlite>
Opens sqlite3 program and opens database (NameofDB is the name I give the database)
        - .mode csv
Tells sqlite3 to work with a csv file
        - .import <NameOfCSV.csv> <NameOfTable>
Takes csv file and makes it a table
        - .quit
 takes you out of sqlite

