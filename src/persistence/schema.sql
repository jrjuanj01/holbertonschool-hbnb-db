-- DATABASE CREATION
CREATE DATABASE IF NOT EXISTS hbnb_db;
-- User table
CREATE TABLE IF NOT EXISTS hbnb_db.User (
    id VARCHAR(36) PRIMARY KEY,
    first_name VARCHAR(120) NOT NULL,
    last_name VARCHAR(120) NOT NULL,
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
    city_id VARCHAR(36) FOREIGN KEY (city_id) REFERENCES hbnb_db.City (id),
    host_id VARCHAR(36) FOREIGN KEY (host_id) REFERENCES hbnb_db.User (id),
    description TEXT,
    number_of_guests INT NOT NULL,
    number_of_rooms INT NOT NULL,
    number_of_bathrooms INT NOT NULL,
    price_per_night INT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
-- Review Table 
CREATE TABLE IF NOT EXISTS hbnb_db.Review (
    id VARCHAR(36) PRIMARY KEY,
    place_id VARCHAR(36) FOREIGN KEY (place_id) REFERENCES hbnb_db.Place (id),
    user_id VARCHAR(36) FOREIGN KEY (user_id) REFERENCES hbnb_db.User (id),
    rating INT NOT NULL CHECK (
        rating >= 1
        AND rating <= 5
    ),
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
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
    amenity_id VARCHAR(120) FOREIGN KEY (amenity_id) REFERENCES hbnb_db.Amenity (id),
    place_id VARCHAR(36) FOREIGN KEY (place_id) REFERENCES hbnb_db.Place (id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
-- City Table 
CREATE TABLE IF NOT EXISTS hbnb_db.City (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    country_code VARCHAR(2) FOREIGN KEY (country_code) REFERENCES hbnb_db.Country (code),
    places (
        SELECT Place.name
        FROM Place
        WHERE Place.city_id = City.id
        ORDER BY Place.name ASC
    ),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
--Country Table
CREATE TABLE IF NOT EXISTS hbnb_db.Country (
    code VARCHAR(2) PRIMARY KEY,
    name VARCHAR(120) NOT NULL
);