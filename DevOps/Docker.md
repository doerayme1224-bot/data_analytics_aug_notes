docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 3021:5432 postgres:alpine

- `docker run` : tells docker to run something (Like an image)

- image: image of an operating system (Like a snapshot of hte OS) That we can build apps on top of

-- name: giving a name to an application

-e : Tells app we want to use enviorment variables

in this case, POSTGRES_PASSWORD-(my_password)

-d : detach: tells docker not to tak eover the terminal. run it on the side (detached form the terminal)

`postgres` : in this case, this is the hte image we are telling docker to run

-p : tells docker which port to use (Default for postgres: 5432)

alpine: Very small version of linux

