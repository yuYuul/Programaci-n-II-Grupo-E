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
VALUES ('Carlos', 25, 'Maculino', 'Asma
');

SELECT * FROM pacientes;