-- Table: public."Impresora"

-- DROP TABLE public."Impresora";

CREATE TABLE public."Impresora"
(
    modelo character varying(10) COLLATE pg_catalog."default" NOT NULL,
    color integer NOT NULL,
    tipo character varying(2) COLLATE pg_catalog."default" NOT NULL,
    precio integer NOT NULL,
    CONSTRAINT "Impresora_pkey" PRIMARY KEY (modelo)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Impresora"
    OWNER to postgres;


-- Table: public."PC"

-- DROP TABLE public."PC";

CREATE TABLE public."PC"
(
    modelo character varying(10) COLLATE pg_catalog."default" NOT NULL,
    velocidad real NOT NULL,
    ram integer NOT NULL,
    disco_duro integer NOT NULL,
    precio integer NOT NULL,
    CONSTRAINT "PC_pkey" PRIMARY KEY (modelo)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."PC"
    OWNER to postgres;


-- Table: public."Portatil"

-- DROP TABLE public."Portatil";

CREATE TABLE public."Portatil"
(
    modelo character varying(10) COLLATE pg_catalog."default" NOT NULL,
    velocidad real NOT NULL,
    ram integer NOT NULL,
    disco_duro integer NOT NULL,
    pantalla integer NOT NULL,
    precio integer NOT NULL,
    CONSTRAINT "Portatil_pkey" PRIMARY KEY (modelo)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Portatil"
    OWNER to postgres;


-- Table: public."Producto"

-- DROP TABLE public."Producto";

CREATE TABLE public."Producto"
(
    "Fabricante" character varying(30) COLLATE pg_catalog."default" NOT NULL,
    "Modelo" character varying(10) COLLATE pg_catalog."default" NOT NULL,
    "Tipo" integer NOT NULL,
    CONSTRAINT "Producto_pkey" PRIMARY KEY ("Modelo")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Producto"
    OWNER to postgres;