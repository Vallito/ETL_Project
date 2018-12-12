
DROP DATABASE IF EXISTS trees_db;

CREATE DATABASE trees_db;

USE trees_db;

CREATE TABLE nyc_trees(
	ID INT AUTO_INCREMENT PRIMARY KEY,
    zip_code INT,
    species_nm VARCHAR(255),
    count_tree INT,
    avg_diameter INT,
    tree_species_id INT NOT NULL
	);
    
    
CREATE TABLE tree_species(
	ID INT PRIMARY KEY,
    species_nm VARCHAR(255),
    img_loc VARCHAR(255),
    web_common_nm VARCHAR(255),
    latin_nm VARCHAR(255),
    habitat VARCHAR(255),
    growth_habit VARCHAR(255),
    bloom_time VARCHAR(255),
    longevity VARCHAR(255)
	);
    
    
    
