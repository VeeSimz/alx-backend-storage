#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx

    docs_num = nginx_logs.count_documents({})
    get_num = nginx_logs.count_documents({'method': 'GET'})
    post_num = nginx_logs.count_documents({'method': 'POST'})
    put_num = nginx_logs.count_documents({'method': 'PUT'})
    patch_num = nginx_logs.count_documents({'method': 'PATCH'})
    delete_num = nginx_logs.count_documents({'method': 'DELETE'})
    get_status = nginx_logs.count_documents({'method': 'GET',
                                             'path': '/status'})
    IPs_count = nginx_logs.aggregate([
        {
            '$group': {
              '_id': "$ip",
              'count': {'$sum': 1}
            }
        },
        {
            "$sort": {"count": -1}
        }
    ])
    print("{} logs".format(docs_num))
    print("Methods:")
    print("\tmethod GET: {}".format(get_num))
    print("\tmethod POST: {}".format(post_num))
    print("\tmethod PUT: {}".format(put_num))
    print("\tmethod PATCH: {}".format(patch_num))
    print("\tmethod DELETE: {}".format(delete_num))
    print("{} status check".format(get_status))
    print("IPs:")
    x = 0
    for i in IPs_count:
        print("\t{}: {}".format(i.get('_id'), i.get('count')))
        x += 1
        if x > 9:
            break
