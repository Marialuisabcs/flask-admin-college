CREATE FUNCTION alteracaolog() RETURNS TRIGGER AS $$
DECLARE
tabela_alterada varchar(10) = TG_RELNAME;

data_alteracao timestamp = CURRENT_DATE;

operacao char = CASE 
                 WHEN TG_OP = 'UPDATE' THEN 'U'
                 WHEN TG_OP = 'DELETE' THEN 'D'
                 END;

BEGIN
    INSERT INTO logs (tabela_alterada, nome, data_alteracao, operacao) VALUES(tabela_alterada, 
                                                                              old.nome, 
                                                                              data_alteracao,
                                                                              operacao);
return null;

END;
$$ LANGUAGE PLPGSQL;


CREATE TRIGGER alunolog
	BEFORE UPDATE OR DELETE ON aluno FOR EACH ROW
	EXECUTE FUNCTION alteracaolog();

CREATE TRIGGER cursolog
	BEFORE UPDATE OR DELETE ON curso FOR EACH ROW
	EXECUTE FUNCTION alteracaolog();

CREATE TRIGGER professorlog
	BEFORE UPDATE OR DELETE ON professor FOR EACH ROW
	EXECUTE FUNCTION alteracaolog();

CREATE TRIGGER materialog
	BEFORE UPDATE OR DELETE ON materia FOR EACH ROW
	EXECUTE FUNCTION alteracaolog();

ALTER TABLE aluno ENABLE TRIGGER alunolog;

ALTER TABLE curso ENABLE TRIGGER cursolog;

ALTER TABLE professor ENABLE TRIGGER professorlog;

ALTER TABLE materia ENABLE TRIGGER materialog;
