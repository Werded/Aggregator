# Aggregator

The application requires a PostgreSQL and RABBITMQ services. After that, you need to define the environment variables from the example.env file according to your environment.
To start the project, you need to install dependencies from the requirements.txt file and start the server using the uwsgi --ini uwsgi.ini command or use the Docker image of the application.


1. Get current currencies rate `api/currencies/`
2. Get history currency rate `api/currency_histories/?currency={currency id}`
3. Get history currency rate on custom date `api/currency_histories/?currency={currency id}&date_={custom date}`
4. Get history currency rate on date range `api/currency_histories/?currency={currency id}&date_range_after={custom date}&date_range_before={custom date}`
5. Create User `api/users/`
6. Authenticate `auth/token`
