#!/usr/bin/env python3
""" 12. Log stats
"""


from pymongo import MongoClient


def log_stats():
    """ log_stats.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students
    total = students_collection.count_documents({})
    get = students_collection.count_documents({"method": "GET"})
    post = students_collection.count_documents({"method": "POST"})
    put = students_collection.count_documents({"method": "PUT"})
    patch = students_collection.count_documents({"method": "PATCH"})
    delete = students_collection.count_documents({"method": "DELETE"})
    path = students_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
