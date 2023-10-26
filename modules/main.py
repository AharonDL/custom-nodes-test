import dtlpy as dl
import random
import datetime
import json
import logging

logging.basicConfig(level=logging.INFO)


class ServiceRunner(dl.BaseServiceRunner):

    @staticmethod
    def one(item: dl.Item) -> dl.Item:
        logging.info(f"Running service one on item: {item.id}")
        item.metadata['service_one'] = 'service one v4'
        return item.update()

    @staticmethod
    def two(item: dl.Item) -> dl.Item:
        logging.info(f"Running service two on item: {item.id}")
        item.metadata['service_two'] = 'service two v4'
        return item.update()

