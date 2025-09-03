CREATE TABLE public.purchases
(
    purchase_id integer NOT NULL,
    created_at timestamp with time zone,
    name character varying(255) COLLATE pg_catalog."default",
    address character varying(255) COLLATE pg_catalog."default",
    state character varying(2) COLLATE pg_catalog."default",
    zipcode integer,
    user_id integer,
    CONSTRAINT purchases_pkey PRIMARY KEY (purchase_id),
    CONSTRAINT purchases_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);