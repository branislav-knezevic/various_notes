# Prometheus notes

taken from: https://www.youtube.com/watch?v=h4Sl21AKiDg

## What is prometheus

Monitoring tool, has multiple components, great for monitoring microservices but can be used to monitor monolith
applications as well

## Architecture

Main component is *Prometheus Server
It consists of three components
  storage (time series DB)
    stores metrics data
  data retreival worker
    responsible for pulling data from targets and pushing them into DB
  webserver
    accepts queries and displays them

What can be monitored a.k.a Targets
  Server (Win/Lin)
  Single application
  Service (DB, Apache, proxy...)

Each target has units that can be monitored and those vary of the target itself, if it is server then units are CPU,
RAM, HDD status...  
Each unit that is monitored is called `metric` and metrics get saved into prometheus DB  
Metric data has TYPE and HELP attributes
type - for metric type
  counter type - how many times has something happened
  gauge - what is the current value of X
  histogram - how long something took, how big the request was
help - to explain what kind of metric it is

Prometheus PULLS data from targets over HTTP, so no agents need to be installed
For services which are short lived such as batch jobs, `pushgateway` is available so those services would PUSH the data
to prometheus server
Metrics must be exposed on targets on `/metrics` endpoint
Exposed metrics must be in the correct format

For services which don't export prometheus compatible metrics by default, `exporter` is used 
All exporters can be found on Prometheus site
e.g. 
for a Linux server, download a tar and execute, it will convert and export metrics for it 
for k8s microservices, sidecar containter with exporter can be deployed on the same pod as the service which needs to be
monitored

## Configuring Prometheus

Main configuration is done in `prometheus.yaml` file
Configure which targets and in what intreval 
Config example:
```
global: 
  scrape_interval:     15s # define how often targets will be scraped
  evaluation_interval: 15s

rule_files: # rules for alerts or agretaging metrics values
  - first.rules
  - second.rules

scrape_configs: # 
  - job_name: prometheus
    static_configs:
      - targets: ['hostname:port']
  - job_name: some_app
    scrape_interval: 1s # this settings will overrite the global setting
    static_configs:
      - targets: ['hostname:port']
```

## Alert Manager

Component used to trigger alerts to various palces - slack, pagerduty, email...

## Prometheus data storage

Stored in time series DB, uses `PrompQL` query language
Query can be used from prometheus dashborad or from other tools such as Grafana
