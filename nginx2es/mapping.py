DEFAULT_TEMPLATE = {
  "version": 2,
  "index_patterns": [
    "nginx2es-*"
  ],
  "settings": {
      "index": {
        "refresh_interval": "10s",
        "mapping": {
          "total_fields": {
            "limit": "5000"
          }
        },
        "merge": {
          "policy": {
            "max_merged_segment": "5g"
          }
        },
        "unassigned": {
          "node_left": {
            "delayed_timeout": "5m"
          }
        },
        "codec": "best_compression",
        "number_of_replicas": "1",
        "number_of_shards": "5"
      }
  },
  "mappings": {
    "_source": {
      "enabled": True,
      "includes": [],
      "excludes": []
    },
    "_meta": {},
    "_routing": {
      "required": False
    },
    "dynamic": True,
    "numeric_detection": False,
    "date_detection": False,
    "dynamic_templates": [
      {
        "long_fields": {
          "match": "*",
          "match_mapping_type": "long",
          "mapping": {
            "type": "long"
          }
        }
      },
      {
        "string_fields": {
          "mapping": {
            "type": "keyword",
            "norms": False
          },
          "match_mapping_type": "string",
          "match": "*"
        }
      }
    ],
    "properties": {
      "@timestamp": {
        "type": "date",
        "index": True,
        "ignore_malformed": False,
        "doc_values": True,
        "store": False,
        "format": "date_optional_time"
      },
      "geoip": {
        "type": "geo_point"
      },
      "query_geo": {
        "type": "geo_point"
      },
      "remote_addr": {
        "type": "ip"
      },
      "request": {
        "type": "text",
        "index": True,
        "eager_global_ordinals": False,
        "index_phrases": False,
        "norms": False,
        "fielddata": False,
        "store": False,
        "index_options": "positions",
        "fields": {
          "raw": {
            "type": "keyword",
            "norms": False
          }
        }
      },
      "request_path": {
        "type": "text",
        "index": True,
        "eager_global_ordinals": False,
        "index_phrases": False,
        "norms": False,
        "fielddata": False,
        "store": False,
        "index_options": "positions",
        "fields": {
          "raw": {
            "type": "keyword",
            "norms": False
          }
        }
      },
      "request_qs": {
        "type": "text",
        "index": True,
        "eager_global_ordinals": False,
        "index_phrases": False,
        "norms": False,
        "fielddata": False,
        "store": False,
        "index_options": "positions",
        "fields": {
          "raw": {
            "type": "keyword",
            "norms": False
          }
        }
      },
      "status": {
        "type": "long"
      }
    }
  }
}
