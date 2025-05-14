
CREATE TABLE actors (
    actor_id SERIAL,
    first_name VARCHAR(20) NOT NULL,
    last_name  VARCHAR(20) NOT NULL,
    birth_date DATE NOT NULL,
    num_oscars smallint NOT NULL,
    PRIMARY KEY (actor_id)
);


INSERT INTO actors (first_name, last_name, birth_date, num_oscars)
VALUES
('Angelina', 'Jolie', '1975-06-04', 1),
('George', 'Clooney', '1961-06-05', 2),
('Jennifer', 'Aniston', '1969-02-11', 0),
('Matt', 'Damon', '1970-08-10', 5);




SELECT COUNT(*) FROM actors;

INSERT INTO actors (first_name, last_name, birth_date, num_oscars)
VALUES ('', 'tito', '1963-01-15', 2);