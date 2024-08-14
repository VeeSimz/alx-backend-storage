#!/usr/bin/env python3
""" Function that returns the list of school by topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Find by topic """
    return mongo_collection.find({"topics": topic})
