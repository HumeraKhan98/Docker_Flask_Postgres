# Docker_Flask_Postgres

#######################################################################
To launch the application
-------------------------
1. In VSC, setup the virtual environment:
 => py -3 -m venv .venv
Go to view -> command palette -> Python: select interpretor -> choose .env path

2. run the following commands to setup flask:
 a. python -m pip install --upgrade pip
 b. python -m pip install flask
 c. pip install Flask psycopg2-binary
 
3. run the docker compose file:
 => docker-compose up
 
4. browse http://localhost:5000 to view the application

######################################################################
To login to the postgres container
----------------------------------

1. docker exec -it container-name bash (example: docker exec -it postgrescontainer bash)
2. psql -d db_name -U user_name (example, psql -d flask_db -U sammy)

######################################################################
Reference Postgres commands
---------------------------
1. GRANT ALL PRIVILEGES ON DATABASE flask_db TO sammy;
2. GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sammy;
3. select current_user, session_user;
4. set role sammy; (switch role to user sammy)
5. \l (list databases)
6. \du (list of users)
7. \dt (list of tables)
8. \c database_name (change database)
9. \q (to quit)


######################################################################
Reference links:
----------------
1. https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application
2. https://medium.com/free-code-camp/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a
