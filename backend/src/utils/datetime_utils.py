import datetime


def format_timestamp_iso(timestamp) -> str:
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat()


def format_date(timestamp: datetime) -> str:
    return timestamp.strftime("%Y-%m-%d")


def format_timestamp(timestamp: datetime) -> str:
    return timestamp.strftime("%Y-%m-%d_%H-%M-%S")