# 
1. Containerized a postgres database with docker
    - docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 3021:5432 postgres:alpine (this command created the Container)
    - docker ps (Showed me if it was created and running)
    - 
2. I made a connection Using Dbeaver to that postgres  (This is a containerized database)
    - 
    - 
    - 
    - 
    - 
3. With that connection we created tables by running scripts
    - The order at which you run them matters
    - ran them after with ctrl + enter
    - Right clicked on the postgres elephant, and pressed refresh to see if that table was created
     