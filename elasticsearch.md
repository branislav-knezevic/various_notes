# Elasticearch

## Basic terms

*Document* is a JSON string, like a single *raw of data* in a SQL table. This is the smallest unit of information. 
Documents can have different *types* . This corresponds to a *table*.  
*Index* is a collection of a similar documents, it corresponds to a *database*
*Indicies* as just a plural of *index*
Indexes are devided in multiple *Shards* this is done so data is easily searchable
Shards can be stored on a single or multiple nodes (servers)
*Cluster* is a collection of shards
Shards may have replicas which are also stored on the same Nodes
Less shards on a node, the faster the search is
*Mapping* is something like a *schema*
*Post* is something like a *create table* command
*Type* is simply a *type* of data

## Commands

### General health

check elasticearch status
```
curl -X GET <elasticearch_url>/_cluster/health?
```

check detailed cluster status
```
curl -X GET <elasticearch_url>/_cluster/stats
```

get indices info, can be used with or without target parameter
```
curl -X GET <elasticearch_url>/_cat/indices/<target>_all?v=true
```

get detailed info about specific indice
```
curl -X GET <elasticearch_url>/<indice_name>/_stats
```

### Deleting indices

Delete indices from the first 9 days of September
```
curl -XDELETE '<elasticearch_url>/rsyslog-2018.09.0*?pretty'
```

Delete indices from August
```
curl -XDELETE '<elasticearch_url>/rsyslog-2018.08*?pretty'
```

Delete indices from 2017
```
curl -XDELETE '<elasticearch_url>/rsyslog-2017*?pretty'
```

### Searching

The best way is to create a bash script
```bash
curl -X GET "<elasticearch_url>/<index_name>/_search?pretty&size=10000" -H 'Content-Type: application/json' -d '
{
  "query": {
    "match_all": {}
  }
}
'
```
