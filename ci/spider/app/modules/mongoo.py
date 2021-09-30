#!/usr/bin/env python3
import os

import pymongo

###
# Configuration
# Mongo client and DB
client = \
    pymongo.MongoClient(
        f"mongodb://root:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOST')}:27017/?authSource=admin"
    )
