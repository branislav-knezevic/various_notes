## Helm

### Structure

Has a clinet side (CLI)
and a server side - Tiller

### Charts

Top level dir is a chart name
`my-chart/`
  `Chart.yaml` # metadata and versioning applicaiton
  `values.yaml` # default configuration values
  `requirements.yaml` # dependencies (mongo, mysql...)
  `charts/` # place where dependency packages are stored
  `templates/` # templates dir where al templates are stored
    # contains normal YAML files + variables and fuctiones
    # values are picked up from `values.yaml`
    # functions are picked up from `_helpers` file

#### Chart.yaml

Must have couple of keys
`apiVersion: v1` # must have version same as yaml file
`name: <app_name>` # must match name of the folder where the app is
`version: 0.1.0` # version of the chart
Optional :
`description: <some_description>`
`appVersion: "1.0"` # this is the version of the app itself

#### requirements.yaml

```
dependencies:
  - name: mongodb # name of the dependency
    repository: https://kubernetes-charts... # url to the online repository
    version: 1.2.3 # what ever version is needed
```
#### templates/

Within this directory create YAML files for deployment, etc... e.g. `application.yaml`
```
kind: Deployment
apiVersion: ...
metadata:
  name: {{ template "<chart-name>.fullname . }}-deployment # this is a variable which is picked up from _helpers.tpl
  file
spec:
  replicas:
  selector:
    matchLabels:
      app: {{ template "<chart-name>.fullname . }}-label
  templates:
    metadata:
      labels:
        app: {{ template "<chart-name>.fullname . }}-label
    spec:
      containers:
        - name:
          image:....
          env:
            - name: MONGO_URL
              value: mongodb://{{ template "mongodb.fullname" . }}.default.svc.cluster.local:27071/{{ .Values.DbName }}
              # template i reference to  a function in _helpers.tpl file
              # .Values looks for that key in the values.yaml file, used for static variables

---
kind: Service
apiVersion:
metadata:
  name: {{ template "<chart-name>.fullname . }}-service
spec:
  type: ...
  selector: ...
    app: {{ template "<chart-name>.fullname . }}-label
  ports:
    - port:
      targetPort:

```

#### _helpers.tpl

Contains templates for variables which can be used, e.g. chart name variable as this will have to be dynamic
templates are referenced via helm templating language
`{{ template "<chart_name>.fullname" . }}`

Example of a custom function:
```
{{- define "mongodb.fullname" -}}
{{- printf "%s-mongodb" .Release.Name | grunc 63 | trimsuffix "-" -}} # this is specific to mongo
{{- end -}}
```

#### values.yaml

Contains variables e.g.
```
DbName: <database_name>
```

### Commands

#### Creating charts

`helm ls` view list of installed charts
`helm create <chart_name>`  crates a folder structure like above
   this creates a lot of files of which some are not necessary and can be deleted - eg `tests/`, `deployment.yaml`,
  `ingress.yaml`...
`helm install --name <some_name> .`  will package up the helm chart and deploy it to a kubernetes cluster. If name isn't
`helm install --values development.yaml --kube-context=development .` example how it can be used to deploy specific
`helm install --set ImageTag=<desired_tag> --namespace <namespace_name> . ` taken from helm advanced talk
values to a desired environment/namespace
specified a random one will be given. `.` is used as this is initiated from the directory where the chart is.  
`--name` option works with helm2, helm3 doesn't have it.
`helm upgrade <app_name> .` upgrades the exisitng chart, for this example `<some_name> == <app_name`
`helm upgrade <app_name> . --set <some_key_from_values.yaml>=<value>` variable values can be added during deployment
`helm upgrade <app_name> . --values <path_to_file_which_contains_values.yaml>` files can also be used to supply values  
`helm rollback <app_name> <revision_number>` revison can be checked when `helm ls` is ran
`helm inspect values .` shows which values can be customized during a deployment
`helm show values <chart_name>`  to see what options are configurable on a chart
`helm dep list`  lists all dependencies, but it has to be ran from the dir where the helm chart is located
`helm dependency update .`  install dependency in the current directory
`helm template .`  will run just the template part but not deploy anything. Great for troubleshooting
`helm delete --purge <app_name>` deletes the deployed app, this works in helm2, not helm3
`helm uninstall <app_name>` deletes the deployed app, this is for helm3
`helm lint`  validate chart formatting
`helm lint . -f test_values.yaml --strict` example how to do it but also supply values to it
If this fails and reports a certain line with error, run `helm install . --name <name> -f test_values.yaml --debug --dry-run` and check the correct line number here
`helm test $(helm last)` runs a test on last deployed helm

#### Packaging and chart repository

`helm package <chart_name>` package the chart, it crates `.tgz`file with version from `Chart.yaml` file
`helm serve --repo-path .` create local chart repo
`helm serve --repo-path . --address "0.0.0.0:<port>"` create a chart repo which is availale to others
`helm repo add <repo_name> http://<ip>:<port>/charts` port should be the same one from above
`helm repo index .` reindex repo after new version of some app has been added
`helm repo update` reload repositories

`helm search <what_application>`  look online for existing helm charts
