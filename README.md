## How to run

1. make compose-bash
2. cd /app
3. pip install -r requirements.txt
4. python main.py

Take attention to owner_id param value

### Example log
```
2024-09-09 14:51:08,315 INFO sqlalchemy.engine.Engine select pg_catalog.version()
2024-09-09 14:51:08,315 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-09-09 14:51:08,316 INFO sqlalchemy.engine.Engine select current_schema()
2024-09-09 14:51:08,316 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-09-09 14:51:08,316 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2024-09-09 14:51:08,316 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-09-09 14:51:08,318 INFO sqlalchemy.engine.Engine BEGIN (implicit; DBAPI should not BEGIN due to autocommit mode)
2024-09-09 14:51:08,319 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace
WHERE pg_catalog.pg_class.relname = %(table_name)s::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s::VARCHAR, %(param_2)s::VARCHAR, %(param_3)s::VARCHAR, %(param_4)s::VARCHAR, %(param_5)s::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s::VARCHAR
2024-09-09 14:51:08,319 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {'table_name': 'user_account', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2024-09-09 14:51:08,320 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace
WHERE pg_catalog.pg_class.relname = %(table_name)s::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s::VARCHAR, %(param_2)s::VARCHAR, %(param_3)s::VARCHAR, %(param_4)s::VARCHAR, %(param_5)s::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s::VARCHAR
2024-09-09 14:51:08,320 INFO sqlalchemy.engine.Engine [cached since 0.001233s ago] {'table_name': 'address', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2024-09-09 14:51:08,321 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace
WHERE pg_catalog.pg_class.relname = %(table_name)s::VARCHAR AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s::VARCHAR, %(param_2)s::VARCHAR, %(param_3)s::VARCHAR, %(param_4)s::VARCHAR, %(param_5)s::VARCHAR]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s::VARCHAR
2024-09-09 14:51:08,321 INFO sqlalchemy.engine.Engine [cached since 0.001686s ago] {'table_name': 'email', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2024-09-09 14:51:08,321 INFO sqlalchemy.engine.Engine COMMIT using DBAPI connection.commit(), DBAPI should ignore due to autocommit mode
2024-09-09 14:51:08,324 INFO sqlalchemy.engine.Engine BEGIN (implicit; DBAPI should not BEGIN due to autocommit mode)
2024-09-09 14:51:08,324 INFO sqlalchemy.engine.Engine INSERT INTO user_account (id) VALUES (DEFAULT), (DEFAULT) RETURNING user_account.id, user_account.id AS id__1
2024-09-09 14:51:08,324 INFO sqlalchemy.engine.Engine [generated in 0.00004s (insertmanyvalues) 1/1 (ordered)] {}
WARNING:root:=====================================   USER_ID 27 ==========================
2024-09-09 14:51:08,327 INFO sqlalchemy.engine.Engine INSERT INTO address (email_address, user_id) VALUES (%(email_address)s::VARCHAR, %(param_1)s::INTEGER) RETURNING address.id, address.email_address, address.user_id
INFO:sqlalchemy.engine.Engine:INSERT INTO address (email_address, user_id) VALUES (%(email_address)s::VARCHAR, %(param_1)s::INTEGER) RETURNING address.id, address.email_address, address.user_id
2024-09-09 14:51:08,327 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {'email_address': 'test', 'param_1': 27}
INFO:sqlalchemy.engine.Engine:[generated in 0.00010s] {'email_address': 'test', 'param_1': 27}
2024-09-09 14:51:08,330 INFO sqlalchemy.engine.Engine SELECT user_account.id AS user_account_id, email_1.id AS email_1_id, email_1.value AS email_1_value, email_1.owner_id AS email_1_owner_id
FROM user_account LEFT OUTER JOIN email AS email_1 ON user_account.id = email_1.owner_id AND email_1.owner_id = %(owner_id_1)s::INTEGER
WHERE user_account.id IN (%(primary_keys_1)s::INTEGER)
INFO:sqlalchemy.engine.Engine:SELECT user_account.id AS user_account_id, email_1.id AS email_1_id, email_1.value AS email_1_value, email_1.owner_id AS email_1_owner_id
FROM user_account LEFT OUTER JOIN email AS email_1 ON user_account.id = email_1.owner_id AND email_1.owner_id = %(owner_id_1)s::INTEGER
WHERE user_account.id IN (%(primary_keys_1)s::INTEGER)
2024-09-09 14:51:08,330 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {'owner_id_1': 27, 'primary_keys_1': 27}
INFO:sqlalchemy.engine.Engine:[generated in 0.00013s] {'owner_id_1': 27, 'primary_keys_1': 27}
WARNING:root:=====================================   USER_ID 28 ==========================
2024-09-09 14:51:08,332 INFO sqlalchemy.engine.Engine INSERT INTO address (email_address, user_id) VALUES (%(email_address)s::VARCHAR, %(param_1)s::INTEGER) RETURNING address.id, address.email_address, address.user_id
INFO:sqlalchemy.engine.Engine:INSERT INTO address (email_address, user_id) VALUES (%(email_address)s::VARCHAR, %(param_1)s::INTEGER) RETURNING address.id, address.email_address, address.user_id
2024-09-09 14:51:08,332 INFO sqlalchemy.engine.Engine [cached since 0.004972s ago] {'email_address': 'test', 'param_1': 28}
INFO:sqlalchemy.engine.Engine:[cached since 0.004972s ago] {'email_address': 'test', 'param_1': 28}
2024-09-09 14:51:08,333 INFO sqlalchemy.engine.Engine SELECT user_account.id AS user_account_id, email_1.id AS email_1_id, email_1.value AS email_1_value, email_1.owner_id AS email_1_owner_id
FROM user_account LEFT OUTER JOIN email AS email_1 ON user_account.id = email_1.owner_id AND email_1.owner_id = %(owner_id_1)s::INTEGER
WHERE user_account.id IN (%(primary_keys_1)s::INTEGER)
INFO:sqlalchemy.engine.Engine:SELECT user_account.id AS user_account_id, email_1.id AS email_1_id, email_1.value AS email_1_value, email_1.owner_id AS email_1_owner_id
FROM user_account LEFT OUTER JOIN email AS email_1 ON user_account.id = email_1.owner_id AND email_1.owner_id = %(owner_id_1)s::INTEGER
WHERE user_account.id IN (%(primary_keys_1)s::INTEGER)
2024-09-09 14:51:08,333 INFO sqlalchemy.engine.Engine [cached since 0.003383s ago] {'owner_id_1': 27, 'primary_keys_1': 28}
INFO:sqlalchemy.engine.Engine:[cached since 0.003383s ago] {'owner_id_1': 27, 'primary_keys_1': 28}
2024-09-09 14:51:08,334 INFO sqlalchemy.engine.Engine ROLLBACK using DBAPI connection.rollback(), DBAPI should ignore due to autocommit mode
INFO:sqlalchemy.engine.Engine:ROLLBACK using DBAPI connection.rollback(), DBAPI should ignore due to autocommit mode
root@c2824f3d09c0:/app#
```
