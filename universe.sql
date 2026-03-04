psql --username=freecodecamp --dbname=postgres
\c universe 
CREATE TABLE galaxy (
  galaxy_id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  description TEXT NOT NULL,
  age_in_millions_of_years INT NOT NULL,
  galaxy_type VARCHAR(50) NOT NULL,
  has_life BOOLEAN NOT NULL
);

CREATE TABLE star (
  star_id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  galaxy_id INT NOT NULL,
  age_in_millions_of_years INT NOT NULL,
  is_spherical BOOLEAN NOT NULL,
  mass NUMERIC(10,2) NOT NULL,
  CONSTRAINT fk_galaxy
    FOREIGN KEY(galaxy_id)
    REFERENCES galaxy(galaxy_id)
);

CREATE TABLE planet (
  planet_id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  star_id INT NOT NULL,
  age_in_millions_of_years INT NOT NULL,
  planet_type VARCHAR(50) NOT NULL,
  has_life BOOLEAN NOT NULL,
  distance_from_star NUMERIC(10,2) NOT NULL,
  CONSTRAINT fk_star
    FOREIGN KEY(star_id)
    REFERENCES star(star_id)
);

CREATE TABLE moon (
  moon_id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  planet_id INT NOT NULL,
  is_spherical BOOLEAN NOT NULL,
  age_in_millions_of_years INT NOT NULL,
  diameter_km INT NOT NULL,
  CONSTRAINT fk_planet
    FOREIGN KEY(planet_id)
    REFERENCES planet(planet_id)
);

CREATE TABLE comet (
  comet_id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  orbit_period_years INT NOT NULL,
  is_periodic BOOLEAN NOT NULL,
  description TEXT NOT NULL
);

INSERT INTO galaxy (name, description, age_in_millions_of_years, galaxy_type, has_life) VALUES
('Milky Way', 'Our home galaxy', 13600, 'Spiral', true),
('Andromeda', 'Nearest major galaxy', 10000, 'Spiral', false),
('Triangulum', 'Small spiral galaxy', 8000, 'Spiral', false),
('Whirlpool', 'Interacting galaxy', 9000, 'Spiral', false),
('Sombrero', 'Bright nucleus galaxy', 11000, 'Elliptical', false),
('Cartwheel', 'Ring galaxy', 5000, 'Lenticular', false);

INSERT INTO star (name, galaxy_id, age_in_millions_of_years, is_spherical, mass) VALUES
('Sun', 1, 4600, true, 1.00),
('Proxima Centauri', 1, 4500, true, 0.12),
('Sirius', 1, 300, true, 2.02),
('Alpha Andromedae', 2, 2000, true, 3.80),
('Betelgeuse', 1, 8000, true, 20.00),
('Rigel', 1, 8000, true, 18.00);


INSERT INTO planet (name, star_id, age_in_millions_of_years, planet_type, has_life, distance_from_star) VALUES
('Mercury',1,4500,'Rocky',false,57.9),
('Venus',1,4500,'Rocky',false,108.2),
('Earth',1,4500,'Rocky',true,149.6),
('Mars',1,4500,'Rocky',false,227.9),
('Jupiter',1,4500,'Gas Giant',false,778.5),
('Saturn',1,4500,'Gas Giant',false,1434),
('Uranus',1,4500,'Ice Giant',false,2871),
('Neptune',1,4500,'Ice Giant',false,4495),
('Proxima b',2,4000,'Exoplanet',false,7.5),
('Sirius b1',3,200,'Exoplanet',false,20.5),
('Andro Planet 1',4,1000,'Rocky',false,150),
('Rigel X',6,7000,'Gas Giant',false,500);

INSERT INTO moon (name, planet_id, is_spherical, age_in_millions_of_years, diameter_km) VALUES
('Moon',3,true,4500,3474),
('Phobos',4,false,4500,22),
('Deimos',4,false,4500,12),
('Io',5,true,4500,3643),
('Europa',5,true,4500,3122),
('Ganymede',5,true,4500,5268),
('Callisto',5,true,4500,4820),
('Titan',6,true,4500,5150),
('Rhea',6,true,4500,1527),
('Iapetus',6,true,4500,1469),
('Dione',6,true,4500,1123),
('Tethys',6,true,4500,1062),
('Miranda',7,true,4500,472),
('Ariel',7,true,4500,1158),
('Umbriel',7,true,4500,1169),
('Triton',8,true,4500,2706),
('Nereid',8,false,4500,340),
('Proteus',8,false,4500,420),
('ExoMoon1',9,true,3000,2000),
('ExoMoon2',10,true,100,1500);

INSERT INTO comet (name, orbit_period_years, is_periodic, description) VALUES
('Halley',76,true,'Famous periodic comet'),
('Hale-Bopp',2533,true,'Bright comet of 1997'),
('NEOWISE',6800,false,'Recently observed comet');
