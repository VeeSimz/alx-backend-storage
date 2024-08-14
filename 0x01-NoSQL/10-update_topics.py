#!/usr/bin/env python3
""" Function that changes all topics of a document based on the name """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ update topics based on the name """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
