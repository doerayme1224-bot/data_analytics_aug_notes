CREATE TABLE public.products
(
    product_id integer NOT NULL,
    title character varying(255) COLLATE pg_catalog."default",
    price numeric,
    created_at timestamp with time zone,
    deleted_at timestamp with time zone,
    tags character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT products_pkey PRIMARY KEY (product_id)
);





