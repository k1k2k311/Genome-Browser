-- Create summary table:

CREATE TABLE summary
(       gene            VARCHAR(40)     NULL,
        product         VARCHAR(80)     NULL,
        accession       VARCHAR(10)     NOT NULL,
        locus           VARCHAR(80)     NULL,
        PRIMARY KEY (accession)
);

-- CREATE INDEX locusX ON summary (locus(12));


-- Create coding_sequence table:

CREATE TABLE coding_sequence
(       accession       VARCHAR(10)     NOT NULL,
	coding_seq	MEDIUMTEXT	NOT NULL,
        FOREIGN KEY (accession) REFERENCES summary(accesison)
);


-- Create full_sequence table:

CREATE TABLE full_sequence
(       accession       	VARCHAR(10)     NOT NULL,
	full_seq		MEDIUMTEXT	NOT NULL,
	coding_start		INT		NOT NULL,
	coding_end		INT		NOT NULL,
	partial_5		CHAR(3)		NOT NULL,
	partial_3		CHAR(3)		NOT NULL,
	full_coordinates	VARCHAR(200)	NOT NULL,
	translation		MEDIUMTEXT	NOT NULL,
        FOREIGN KEY (accession) REFERENCES summary(accesison)
);

-- POPULATE TABLES:

-- summary data:
LOAD DATA INFILE "/d/user6/lg001/Biocomp2/project/summary_table.dat" INTO TABLE summary
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

-- coding_sequence data:
LOAD DATA INFILE "/d/user6/lg001/Biocomp2/project/seq_table.dat" INTO TABLE coding_sequence
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';

-- full_sequence data:
LOAD DATA INFILE "/d/user6/lg001/Biocomp2/project/full_seq_table.dat" INTO TABLE full_sequence
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';


