CREATE TABLE public.roles (
	id serial4 NOT NULL,
	"name" varchar(30) NOT NULL,
	CONSTRAINT roles_pkey PRIMARY KEY (id),
	CONSTRAINT roles_un UNIQUE (name)
);


CREATE TABLE public.features (
	id serial4 NOT NULL,
	parent_id int8 NULL,
	"name" varchar(30) NOT NULL,
	field_name varchar(100) NOT NULL,
	CONSTRAINT features_pk PRIMARY KEY (id),
	CONSTRAINT features_fk FOREIGN KEY (parent_id) REFERENCES public.features(id) ON DELETE SET NULL
);


CREATE TABLE public.users (
	id serial4 NOT NULL,
	tenant_id int8 NOT NULL,
	external_user_id int8 NOT NULL,
	role_id int8 NULL,
	CONSTRAINT users_pk PRIMARY KEY (id),
	CONSTRAINT users_fk FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE SET NULL
);
CREATE UNIQUE INDEX users_tenant_id_idx ON public.users USING btree (tenant_id, external_user_id);


CREATE TABLE public.role_permissions (
	id serial4 NOT NULL,
	role_id int8 NOT NULL,
	feature_id int8 NOT NULL,
	"action" public.action_enum NOT NULL,
	permitted bool NOT NULL,
	CONSTRAINT role_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT role_permissions_un UNIQUE (role_id, feature_id, action),
	CONSTRAINT role_permissions_role_fk FOREIGN KEY (role_id) REFERENCES public.roles(id),
	CONSTRAINT role_permissions_feature_fk FOREIGN KEY (feature_id) REFERENCES public.features(id)
);


CREATE TABLE public.user_permissions (
	id serial4 NOT NULL,
	user_id int8 NOT NULL,
	feature_id int8 NOT NULL,
	"action" public.action_enum NOT NULL,
	permitted bool NOT NULL,
	CONSTRAINT user_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT user_permissions_un UNIQUE (user_id, feature_id, action),
	CONSTRAINT user_permissions_user_fk FOREIGN KEY (user_id) REFERENCES public.users(id),
	CONSTRAINT user_permissions_feature_fk FOREIGN KEY (feature_id) REFERENCES public.features(id)
);


CREATE TABLE public.feature_actions (
	id serial4 NOT NULL,
	feature_id int8 NOT NULL,
	"action" public.action_enum NOT NULL,
	CONSTRAINT feature_actions_un UNIQUE (feature_id, action),
	CONSTRAINT feature_actions_fk FOREIGN KEY (feature_id) REFERENCES public.features(id)
);
