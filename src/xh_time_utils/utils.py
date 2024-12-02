import zoneinfo
import datetime as dt

time_format= '%Y-%m-%dT%H:%M:%S%z'
hktz = zoneinfo.ZoneInfo("Asia/Hong_Kong")
def to_time_str(d):
    return d.astimezone(hktz).strftime(time_format)

def from_str_to_time(date_str)->dt.datetime|None:
    return dt.datetime.strptime(date_str.replace(" +","+"), time_format).astimezone(hktz) if date_str is not None else None
