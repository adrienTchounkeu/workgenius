from collections import defaultdict
from enum import Enum
from typing import Dict


class EventType(str, Enum):
    SEND = "send"
    DEFERRAL = "deferral"
    HARD_BOUNCE = "hard_bounce"
    SOFT_BOUNCE = "soft_bounce"
    DELIVERED = "delivered"
    OPEN = "open"
    CLICK = "click"
    SPAM = "spam"
    UNSUB = "unsub"
    REJECT = "reject"

    @classmethod
    def values(cls):
        return {c for c in EventType}


def count_messages_by_event(mandrill_events: list) -> Dict[str, int]:
    """
    Counts messages by event
    [ {event1}, {event2}, {event1} ]
    => { event1: 2, event2: 1 }
    """
    d: Dict[str, int] = defaultdict(int)

    for m_e in mandrill_events:
        ev = m_e.get("event", None)
        # check if the event is among message event types
        if ev in EventType.values():
            d[ev] += 1
    return d
