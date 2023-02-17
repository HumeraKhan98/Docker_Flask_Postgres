# Docker_Flask_Postgres

####################################################################
To launch the application
-------------------------
1. In VSC, setup the virtual environment:
 => py -3 -m venv .venv
Go to view -> command palette -> Python: select interpretor -> choose .env path

2. run the following commands to setup flask:
 => python -m pip install --upgrade pip
 => python -m pip install flask
 => pip install Flask psycopg2-binary
 
3. run the docker compose file:
 => docker-compose up
 
4. browse http://localhost:5000 to view the application

######################################################################
To login to the postgres container
----------------------------------

=> docker exec -it container-name bash (example: docker exec -it postgrescontainer bash)
=> psql -d db_name -U user_name (example, psql -d flask_db -U sammy)

######################################################################
Reference Postgres commands
---------------------------
=> GRANT ALL PRIVILEGES ON DATABASE flask_db TO sammy;
=> GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sammy;
=> select current_user, session_user;
=> set role sammy; (switch role to user sammy)
=> \l (list databases)
=> \du (list of users)
=> \dt (list of tables)
=> \c database_name (change database)
=> \q (to quit)


######################################################################
Reference links:
----------------
1. https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application
2. https://medium.com/free-code-camp/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a
