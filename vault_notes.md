# Vault notes

## Vault initialization

Once vault has been created via docker or k8s it needs to be initialized and unsealed in order for it to be
used

First create a variable for vault location:
`export VAULT_ADDR='http://<address>:<port>'`  

Then it needs to be initialized:
`vault operator init`
This will return several values which need to be save somewhere:
```
Unseal Key 1: SEle9/GDl700ApQfFtHN0CFCguQnkdCoX6/JiXeKyVn3
Unseal Key 2: cjAmS8uRC3bbqIB8/962WzGyY3uCb/OqNVMGSacnGnbc
Unseal Key 3: n32S9X5Zgb5/oIU2FIcq76EYy/sJrpUtg4biNEzJpkYO
Unseal Key 4: awTjRkaMlRiQlEJjefeKs6l0NqERJLDB97IArGP9ZjDP
Unseal Key 5: zdXRdZhvxoDi0ckVymb8rUu1+xkUnEONATVWb6qZoCWD

Initial Root Token: s.ZrdkHC4Ng2o0lFkQ1nZTKuH
```
These values will be used to unseal or log in to the vault
In order to unseal this command needs to be ran at least 3 times:
`vault opearator unseal`

## Vault login

If Vault is running locally, or in K8s, the best way is to export local address to `VAULT_ADDR` variable  
`export VAULT_ADDR='http://<address>:<port>'`  

Next run `vault login` and insert vault token when prompted

## Default settings

`vault read sys/mounts/auth/token/tune` check default token lease duration
`vault write sys/mounts/auth/token/tune default_lease_ttl=6m max_lease_ttl=24h` change default token lease duration

## Secret engines

`vault secrets enable -path=<key_value_store_name/ kv` create new key value store
`vault secrets enable -path=bk-store/ kv`
`vault secrets disable <key_value_store_name>/` disable/delete existing key value store
`vault secrets disable -path=bk-store/ kv`
`vault secrets list` show exising key value stores

### Key value stores

`vault kv put <key_value_store_name>/<secret_name> foo=bar` add foo secret with value bar to a key value store
`vault kv put bk-store/bk-secret foo=bar` 
`vault kv get <key_value_store_name>/<secret_name>` return value of the key-value pair stored in the secret
`vault kv get bk-store/bk-secret`
`vault kv delete <key_value_store_name>/<secret_name>` delete existng secret
`vault kv delete bk-store/bk-secret`

## App roles

Approle login method first needs to be enabled in order for it to be used  
`vault auth enable approle` enable approle
`vault write -f auth/approle/role/<app_role_name>` create new approle with 0 values as `-f` is used
`vault write -f auth/approle/role/bk-role`
`vault read auth/approle/role/<app_role_name>/` get some data about the desired role
`vault read auth/approle/role/bk-role/`
`vault read auth/approle/role/<app_role_name>/role-id` read role_id value for desired role
`vault read auth/approle/role/bk-role/role-id`
`vault write -f auth/approle/role/<app_role_name>/secret-id` crete new secret for the desired role
`vault write -f auth/approle/role/bk-role/secret-id`
`vault write auth/approle/login role_id="<role_id" secret_id="<secret_id"` to log in as specific vault role
Output of this should be several things but the most important one is `token`
`vault write auth/approle/login role_id="b401918b-cee6-c822-8efe-36ea1bb9766a" secret_id="2509c8c2-e60b-cd63-3184-a59b33cfd33f"`
`VAULT_TOKEN=<token> <command>` to execute any command as that user
`VAULT_TOKEN=s.3C2epEb7Jv4gWFtG0P5T0DAA vault kv list bk-store`


## Running vault via helm

`helm install --name vault hashicorp/vault --namespace <namespace>` Install vault to desired namespace
This will create desired services, deployment, pods.... but pod will be stuck in a pending state because of
persistentVolumeclame which won't have a necessary volume attached to it.
For this volume needs to be created:
```
kind: PersistentVolume
apiVersion: v1
metadata:
  name: vault-vol
  labels:
    type:
      local
spec:
  storageClassName: localstorage
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/vault-vol"
```
Also existing PVC will need to be edited, `spec` part of it:
```
  spec:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 10Gi
    storageClassName: localstorage
    volumeMode: Filesystem
    volumeName: vault-vol
```
And also on a node on which this volume is located, permissions of that mounted drive will need to be changed.
To locate which node it is run:
`k -n vualt describe pod vault-0 | grep Node`
On the node change permisisons of the volume to 777 with `sudo chmod 777 /mnt/vault-vol`

## Vault via https

If vault is set to run via `https` by having option `tlsDisable` set to `false` when you try to log on to it from the
local computer it will always return an error for the certificate e.g. `x509: certificate signed by unknown authority`  
In order to get rid of this error there are few options:  
1. on each command add `-tls-skip-verify`
2. set variable `VAULT_SKIP_VERIFY=1`
3. add CA of the k8s host where the vault is hosted to CAs on machine from which `vault cli` is being used:  
```
kubectl config view --raw --minify --flatten -o jsonpath='{.clusters[].cluster.certificate-authority-data}' | base64 -d
> /tmp/vault.ca
```

