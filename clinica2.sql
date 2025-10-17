CREATE DATABASE clinica1;
USE clinica1;

CREATE TABLE pacientes (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    genero VARCHAR(10),
    diagnostico VARCHAR(150)
);

INSERT INTO pacientes(nombre, edad, genero, diagnostico)
VALUES ('Fabian', 20, 'Masculino', 'Ninguna');

SELECT * FROM pacientes;

UPDATE pacientes 
SET diagnostico = 'Anemia' 
WHERE id_paciente = 1;

SELECT * FROM pacientes;

DELETE FROM pacientes WHERE id_paciente=1;

CREATE TABLE doctor(
    id_doctor INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    CI VARCHAR(10),
    Correo VARCHAR(50),
    Fecha_ingreso DATE
);
INSERT INTO doctor (Nombre, CI, Correo, Fecha_ingreso) VALUES 
('Santiago', '12570024', 'santi034@gmail.com', '2020-03-15');
INSERT INTO doctor (Nombre, CI, Correo, Fecha_ingreso) VALUES('Natalia', '12570025', 'nati045@gmail.com', '2022-04-20'),
('Valeria', '10570054', 'vele123@gmail.com', '2021-02-10'),
('Yuliana', '22570024', 'yuli222@gmail.com', '2019-01-25'),
('Sofia', '32579023', 'sofffvvv@gmail.com', '2023-10-05'),
('Javier', '12570027', 'javicho@gmail.com', '2020-11-25'),
('Felipe', '20571124', 'feliponn@gmail.com', '2021-06-12'),
('Benjamin', '14470026', 'bemja543@gmail.com', '2020-11-23'),
('Geovany', '12570024', 'geovanyyy@gmail.com', '2018-09-05'),
('Jimena', '12345679', 'jimmenaa@gmail.com', '2024-07-27');

DELETE FROM doctor
WHERE id_doctor = 3;
UPDATE doctor
SET Fecha_ingreso = CURDATE()
WHERE id_doctor = 5;

