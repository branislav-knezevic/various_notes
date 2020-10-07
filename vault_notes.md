# Vault notes

If Vault is running locally, or in K8s, the best way is to export local address to `VAULT_ADDR` variable  
`export VAULT_ADDR='http://<address>:<port>'`  

Next run `vault login` and insert vault token when prompted

## Key value stores

`vault secrets enable -path=<key_value_store_name/ kv` create new key value store
`vault secrets disable <key_value_store_name>/` disable/delete existing key value store
`vault secrets list` show exising key value stores
`vault kv put <key_value_store_name>/<secret_name> foo=bar` add foo secret with value bar to a key value store
`vault kv get <key_value_store_name>/<secret_name>` return value of the secret
`vault kv delete <key_value_store_name>/<secret_name>` delete existng secret

## App roles

`vault write -f auth/approle/role/<app_role_name>` create new approle with 0 values as `-f` is used
`vault read auth/approle/role<app_role_name>/role-id` read role_id value for desired role
`vault write -f auth/approle/role<app_role_name>/secret-id` crete new secret for the desired role
