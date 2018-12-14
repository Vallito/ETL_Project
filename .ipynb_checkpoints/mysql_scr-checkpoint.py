pw = ''
create_db = "DROP DATABASE IF EXISTS tree_db; CREATE DATABASE tree_db;"
            
create_tbl = """
            USE tree_db;
            CREATE TABLE nyc_tree(
                ID INT AUTO_INCREMENT PRIMARY KEY,
                zip_code INT,
                species_nm VARCHAR(255),
                count_tree INT,
                avg_diameter INT
                );
            CREATE TABLE tree_species(
                species_nm VARCHAR(255) NOT NULL PRIMARY KEY,
                img_loc VARCHAR(255),
                web_common_nm VARCHAR(255),
                habitat VARCHAR(255),
                growth_habit VARCHAR(255),
                bloom_time VARCHAR(255),
                longevity VARCHAR(255)
                );            
            """
            