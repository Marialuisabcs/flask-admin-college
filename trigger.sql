CREATE OR REPLACE FUNCTION alteracaolog() RETURNS TRIGGER AS $$
    DECLARE
        op char = CASE
                         WHEN TG_OP = 'UPDATE' THEN 'U'
                         WHEN TG_OP = 'DELETE' THEN 'D'
                         END;

    BEGIN
        INSERT INTO log (tabela_alterada, nome, data_alteracao, operacao) VALUES(TG_RELNAME, old.nome, CURRENT_DATE, op);
        RETURN NULL;
END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER alunolog
	AFTER UPDATE OR DELETE ON aluno FOR EACH ROW
	EXECUTE FUNCTION alteracaolog();

CREATE TRIGGER cursolog
	AFTER UPDATE OR DELETE ON curso FOR EACH ROW
	EXECUTE FUNCTION alteracaolog();

CREATE TRIGGER professorlog
	AFTER UPDATE OR DELETE ON professor FOR EACH ROW
	EXECUTE FUNCTION alteracaolog();

CREATE TRIGGER materialog
	AFTER UPDATE OR DELETE ON materia FOR EACH ROW
	EXECUTE FUNCTION alteracaolog();