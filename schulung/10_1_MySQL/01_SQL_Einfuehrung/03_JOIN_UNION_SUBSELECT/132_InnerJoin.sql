SELECT t_ma.vname, t_ma.name, t_ma.abtnr, t_abt.id, t_abt.name 
FROM t_ma INNER JOIN t_abt 
  ON t_ma.abtnr = t_abt.id
-- WHERE t_ma.ort = 'Zürich'
;

-- ODER

SELECT t_ma.vname, t_ma.name, t_ma.abtnr, t_abt.id, t_abt.name
FROM t_ma, t_abt 
WHERE t_ma.abtnr = t_abt.id; 
