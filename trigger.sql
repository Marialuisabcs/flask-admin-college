drop table if exists matriculadoEm CASCADE;
drop table if exists lacionadoPor CASCADE;
drop table if exists professor CASCADE;
drop table if exists curso CASCADE;
drop table if exists materia CASCADE;
drop table if exists aluno CASCADE;
drop table if exists log CASCADE;

DROP TRIGGER IF EXISTS alunolog ON aluno;
DROP TRIGGER IF EXISTS cursolog ON curso;
DROP TRIGGER IF EXISTS professorlog ON professor;
DROP TRIGGER IF EXISTS materialog ON materia;

drop function alteracaolog();