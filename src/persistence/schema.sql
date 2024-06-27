-- DATABASE CREATION
CREATE DATABASE IF NOT EXISTS hbnb_db;
-- Country Table
CREATE TABLE IF NOT EXISTS hbnb_db.Country (
    code VARCHAR(2) PRIMARY KEY,
    name VARCHAR(120) NOT NULL
);
-- City Table 
CREATE TABLE IF NOT EXISTS hbnb_db.City (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    country_code VARCHAR(2) NOT NULL,
    FOREIGN KEY (country_code) REFERENCES hbnb_db.Country (code)
);
-- User Table
CREATE TABLE IF NOT EXISTS hbnb_db.User (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
-- Place Table 
CREATE TABLE IF NOT EXISTS hbnb_db.Place (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    description TEXT,
    number_of_guests INT NOT NULL,
    number_of_rooms INT NOT NULL,
    number_of_bathrooms INT NOT NULL,
    price_per_night INT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    city_id VARCHAR(36) NOT NULL,
    host_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (city_id) REFERENCES hbnb_db.City (id),
    FOREIGN KEY (host_id) REFERENCES hbnb_db.User (id)
);
-- Review Table 
CREATE TABLE IF NOT EXISTS hbnb_db.Review (
    id VARCHAR(36) PRIMARY KEY,
    rating INT NOT NULL CHECK (
        rating >= 1
        AND rating <= 5
    ),
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    place_id VARCHAR(36) NOT NULL,
    user_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (place_id) REFERENCES hbnb_db.Place (id),
    FOREIGN KEY (user_id) REFERENCES hbnb_db.User (id)
);
-- Amenity Table 
CREATE TABLE IF NOT EXISTS hbnb_db.Amenity (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
-- PlaceAmenity Table 
CREATE TABLE IF NOT EXISTS hbnb_db.PlaceAmenity (
    id VARCHAR(36) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    amenity_id VARCHAR(36) NOT NULL,
    place_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (amenity_id) REFERENCES hbnb_db.Amenity (id),
    FOREIGN KEY (place_id) REFERENCES hbnb_db.Place (id)
);