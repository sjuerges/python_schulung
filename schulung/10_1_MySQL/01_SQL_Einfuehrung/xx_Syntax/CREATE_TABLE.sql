CREATE TABLE tab_name(
	sp_name_1 <datentyp> [DEFAULT wert_1] [NULL|NOT NULL]
	[, ...]
	[, [CONSTRAINT  constr_name] PRIMARY KEY (sp_name_1[, ...])]
	[, [CONSTRAINT  constr_name] FOREIGN KEY (sp_name_1[, ...]) 
				REFERENCE ref_tab_name (sp_name_1[, ...])]
	[, [CONSTRAINT  constr_name] CHECK(<bedingung(en)>)]
);

<datentyp> 		:= -- siehe aktuelle SQL-Reference
				   -- Zahl
					INTEGER
					DECIMAL(gesamt_stallen_anzahl,komma_stellen)
					FLOAT(n)
				   -- Zeichenketten
					CHAR(n)
					VARCHAR(n)
					TEXT
				  -- DATUM & ZEIT
					DATE
					DATETIME
					TIME
					'YYYY-MM-DD HH:MI:SS.nnnnnn'

<bedingung(en)> := -- siehe SELECT.sql

ALTER TABLE tab_name
	{ADD|MODIFY|DROP}
;

DROP TABLE tab_name;