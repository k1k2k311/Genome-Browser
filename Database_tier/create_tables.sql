-- Create summary table:

CREATE TABLE summary
(	GI		VARCHAR(20)	NOT NULL,
	gene		VARCHAR(40)	NULL,
	product		VARCHAR(80)	NULL,
	ACCESSION	VARCHAR(10)	NOT NULL,
	locus		VARCHAR(80)	NULL,
	PRIMARY KEY (GI)
);

-- CREATE INDEX locusX ON summary (locus(12));


-- Bulk load:
LOAD DATA INFILE "/Biocomp2/project/summary_table.dat" INTO TABLE summary
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';
