"""
Redis Client to Store key-value messages
"""
import json
from typing import Any, Dict, List

import redis

from helpers import logger

r = redis.Redis.from_url("redis://default:redispw@localhost:49153")


class RedisClient:
    def store_messages(self, mandrill_events: List[Dict[str, Any]]):
        try:
            st = {m_e["_id"]: json.dumps(m_e) for m_e in mandrill_events}
            r.mset(st)
        except Exception as e:
            logger.error(f"An error occured : {e}")
        else:
            logger.info("Mandrills Events successfully stored on Redis")


redis_client = RedisClient()
