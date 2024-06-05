\c postgres

--CREATE DATABASE climate_db;

\c climate_db

CREATE USER climate_user WITH PASSWORD 'climate_user';

CREATE SCHEMA weather;

CREATE TABLE weather.us_locations (
    location VARCHAR(30) NOT NULL,
    date_time TIMESTAMP NOT NULL,
    temperature_c DOUBLE PRECISION,
    humidity_pct DOUBLE PRECISION,
    precipitation_mm DOUBLE PRECISION,
    wind_speed_kmh DOUBLE PRECISION,
    PRIMARY KEY(location, date_time)
);

GRANT ALL PRIVILEGES ON DATABASE climate_db TO climate_user;
GRANT ALL PRIVILEGES ON SCHEMA weather TO climate_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA weather TO climate_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA weather TO climate_user;

