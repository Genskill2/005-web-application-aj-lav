DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS tags_pets;
DROP TABLE IF EXISTS animal;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS pet;


CREATE TABLE animal (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT UNIQUE NOT NULL
       );


CREATE TABLE tag (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT UNIQUE NOT NULL
       );    
       

CREATE TABLE pet (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       bought DATE,
       sold DATE,
       description TEXT,
       species INTEGER,
       FOREIGN KEY (species) references animal(id) ON DELETE CASCADE
);      
       

CREATE TABLE tags_pets (
       pet INTEGER,
       tag INTEGER,
       FOREIGN KEY (pet) references pet(id) ON DELETE CASCADE,
       FOREIGN KEY (tag) references tag(id) ON DELETE CASCADE
);

       
