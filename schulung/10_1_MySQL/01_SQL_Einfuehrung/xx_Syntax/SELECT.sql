-- SELECT allgemeine Syntax
-- ----------------------------------------------------------------------
5) SELECT						-- Spaltendefinition
1) FROM							-- Objektdefinition
2) [WHERE ]						-- Zeilenfilter
3) [GROUP BY ]					-- Gruppierung (Anzahl Mitarbeiter "JE" Projekt)
4) [HAVING ]					-- Zeilenfilter auf das Gruppierungsergebnis
5) [ORDER BY ]					-- Sortierung
6) [LIMIT [start_pos],anzahl]; 	-- nur MySQL

-- SELECT - Syntax
-- ----------------------------------------------------------------------
SELECT [ALL|DISTINCT] {*| {sp_name_1|<ausdruck>} [[AS] "sp_alias_1"] [, ...]}
FROM {tab_name_1|view_name_1} [[AS] tab_alias_1] [, ...]
[WHERE <bedingung(en)>]
[GROUP BY sp_name_1 [,...]]
[HAVING <bedingung(en)>]
[ORDER BY {sp_name_1|<ausdruck>|"sp_alias_1"} [ASC|DESC][, ...]]
[LIMIT [start_pos],anzahl]; -- nur MySQL

<ausdruck> :=
	{'zeichenkette'|'YYYY-MM-DD HH:MI:SS.nnnnnn'|n|<berechnung>|funktions_name([param_1][, ...])}
	
		<berechnung> := {sp_name_1|n} {+|-|*|/} {sp_name_2|n}
						(sp_name + 10) * 2 



<bedingung(en)> := 
		{sp_name_1|<ausdruck>} <arithmOP> {sp_name_2|<ausdruck>}
		
		<arithmOP> := 	<, >, <=, >=, = 
						<>, (!=) -- ungleich
						
		-- besondere Operatoren
		{sp_name_1|<ausdruck>} BETWEEN {sp_name_2|<ausdruck>} AND {sp_name_3|<ausdruck>}
		{sp_name_1|<ausdruck>} IN (wert1 [, ...])
		{sp_name_1|<ausdruck>} LIKE '_A%' -- Alle mit "A" an 2.Stelle
		{sp_name_1|<ausdruck>} IS [NOT] NULL
		
		<bedingung_1> <logOp> <bedingung_2> [<logOp> ...]
		--logische Operator:
		AND, OR, NOT
		(XOR -- nur MySQL)
		
		('Bier' AND NOT 'Wein') OR (NOT 'Bier' AND 'Wein')

-- ANSI-Join-Syntax
-- ================

SELECT ...
FROM {tab_name_1|view_name_1} [[AS] tab_alias_1] 
		{INNER|LEFT OUTER|RIGHT OUTER|FULL OUTER|CROSS} JOIN
	 {tab_name_2|view_name_2} [[AS] tab_alias_2]
		ON <bedingung(en)>
	[   
		{INNER|LEFT OUTER|RIGHT OUTER|FULL OUTER|CROSS} JOIN
	 {tab_name_3|view_name_3} [[AS] tab_alias_3]
		ON <bedingung(en)> 
	...
	]
[WHERE ...]
[GROUP BY ...]
[HAVING ...]
[ORDER BY ...]
[LIMIT ...] -- nur MySQL;		