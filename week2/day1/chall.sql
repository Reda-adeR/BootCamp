
CREATE TABLE actors (
    actor_id SERIAL,
    first_name VARCHAR(20) NOT NULL,
    last_name  VARCHAR(20) NOT NULL,
    birth_date DATE NOT NULL,
    num_oscars smallint NOT NULL,
    PRIMARY KEY (actor_id)
);


INSERT INTO menu_tt (itemname, itemprice)
VALUES
('couscous',100),
('pizza', 20),
('burger',  130),
('desert', 50);




SELECT COUNT(*) FROM actors;

INSERT INTO actors (first_name, last_name, birth_date, num_oscars)
VALUES ('', 'tito', '1963-01-15', 2);