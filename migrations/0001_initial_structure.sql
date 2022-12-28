-- public.feature_groups definition

-- Drop table

-- DROP TABLE public.feature_groups;

CREATE TABLE public.feature_groups (
	id serial4 NOT NULL,
	"name" varchar(30) NOT NULL,
	field_name varchar(30) NOT NULL,
	CONSTRAINT feature_groups_pk PRIMARY KEY (id),
	CONSTRAINT feature_groups_un UNIQUE (name)
);


-- public.roles definition

-- Drop table

-- DROP TABLE public.roles;

CREATE TABLE public.roles (
	id serial4 NOT NULL,
	"name" varchar(30) NOT NULL,
	CONSTRAINT roles_pkey PRIMARY KEY (id),
	CONSTRAINT roles_un UNIQUE (name)
);


-- public.features definition

-- Drop table

-- DROP TABLE public.features;

CREATE TABLE public.features (
	id serial4 NOT NULL,
	"name" varchar(30) NOT NULL,
	feature_group_id int8 NULL,
	field_name varchar(30) NOT NULL,
	CONSTRAINT features_pk PRIMARY KEY (id),
	CONSTRAINT features_fk FOREIGN KEY (feature_group_id) REFERENCES public.feature_groups(id) ON DELETE SET NULL
);


-- public.role_permissions definition

-- Drop table

-- DROP TABLE public.role_permissions;

CREATE TABLE public.role_permissions (
	id serial4 NOT NULL,
	feature_id int8 NOT NULL,
	"action" public.action_enum NOT NULL,
	permitted bool NOT NULL,
	CONSTRAINT role_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT role_permissions_un UNIQUE (feature_id, action),
	CONSTRAINT role_permissions_fk FOREIGN KEY (feature_id) REFERENCES public.features(id)
);


-- public.user_permissions definition

-- Drop table

-- DROP TABLE public.user_permissions;

CREATE TABLE public.user_permissions (
	id serial4 NOT NULL,
	feature_id int8 NOT NULL,
	"action" int8 NOT NULL,
	permitted bool NOT NULL,
	CONSTRAINT user_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT user_permissions_un UNIQUE (feature_id, action),
	CONSTRAINT user_permissions_fk FOREIGN KEY (feature_id) REFERENCES public.features(id)
);


-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	tenant_id int8 NOT NULL,
	user_id int8 NOT NULL,
	role_id int8 NULL,
	CONSTRAINT users_fk FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE SET NULL
);
CREATE UNIQUE INDEX users_tenant_id_idx ON public.users USING btree (tenant_id, user_id);


-- public.feature_actions definition

-- Drop table

-- DROP TABLE public.feature_actions;

CREATE TABLE public.feature_actions (
	id serial4 NOT NULL,
	feature_id int8 NOT NULL,
	"action" public.action_enum NOT NULL,
	CONSTRAINT feature_actions_un UNIQUE (feature_id, action),
	CONSTRAINT feature_actions_fk FOREIGN KEY (feature_id) REFERENCES public.features(id)
);