A collection of self dev library.

## file_changes_xh

In case we have log file from apache web server, the log file name is "access.log", the log will be renamed to "access.log-{YYYYmmdd}" daily. \
The configuration can be done as below to capture the all the log file content even after renamed to new file name. 
```python
import file_changes_xh as fc
import datetime as dt

fileName = "access.log"

# Please see the RenameHandler source code for detail
# The return value for getFunction() is callable for f"{fileName}{separator}{date}"
renameStrategy = fc.RenameHandler(date=dt.date.today(), separator="-")

fpu = fc.FileProgressUtils() # create the file progress utils
gen = fpu.checkOnceAndDo(
    fileName, 
    renameStrategy.getFunction()
)
while True:
    try:
        dr = next(gen)
        if dr.deltaType == fc.DeltaType.RENAMED:
            pass
        else:
            # handler that simply print out the data
            # should implement the own handling logic 
            fc.ChangeHandler.print_changes(dr)
    except StopIteration:
        pass
```

## ip_utils_xh

IPv4 string handling utils
```python
import ip_utils_xh as ipu

# convert string "192.168.8.1/16" to ipu.Ip object
ip = ipu.Ip.from_regular_form("192.168.8.1/16")    
print(ip.binary_notation()) # print in binary format

ipResults = [
    print(f"{ipStr}[{pow(2, 32 - ip.ip_seg[4])}] {ip.binary_notation()}")
    for ipStr in
    "10.91.132.0/22\n10.91.136.0/21\n10.91.144.0/20\n10.91.160.0/19\n10.91.196.0/22\n10.91.200.0/21\n10.91.208.0/20\n10.91.224.0/19".split("\n")
    for ip in [ipu.Ip.from_regular_form(ipStr)]
]
```

Find host by ip if applicable
```python
form ip_utils_xh import defaultIpHostFinder as ipHostFinder
ipHostFinder.find("127.0.0.1")
```

## string_utils_xh

```python
import string_utils_xh as su
su.repeat_str()
```