A collection of self dev library.

## Build
```shell
rm -fr dist
python -m build
python -m twine upload dist/*
```

## Functional

```python
from xh_functional import Scope, Stream

Scope(1)\
.apply(lambda x: x + 1)\
.verify(lambda x: x == 2, msg=lambda x: f"Exception: {x}")\
.map(lambda x: f"Some number: {x}")\
.get()

# output
# Some number: 2

Stream([1, 2, 3, 4])\
.map(lambda x: x * x)\
.filter(lambda x: x % 2 == 0)\
.get()

# output
# Some number: [2, 4, 16]
```

    

```

## File Utils
```python
from xh_file_utils import FileUtils

FileUtils.check_file("file path", check_is_file=True, check_is_dir=False)

# The read_file_lines will return a generator, which is more memory efficient
for line in FileUtils.read_file_lines("file path"):
    print(line)


# file content
text = FileUtils.read_file("file path")

```

## Ini Modifier
Modify openssl.cnf with yaml configuration.

```yaml
- type: ca
  name: ca
  openssl_cnf:
    - { type: value, section: req, key: prompt, value: "no", state: present }
    - { type: value, section: req_distinguished_name, key: localityName_default, state: remove }
    - { type: value, section: req_distinguished_name, key: countryName, value: HK, state: present }
    - { type: value, section: server_cert, key: alt_names, value: ca.kafka.examplecom, state: present }
    - { type: alt_names, section: alt_names, key: dns, value: localhost, state: present }
    - { type: alt_names, section: alt_names, key: dns, value: node-1.kafka.example.com, state: present }
    - { type: alt_names, section: alt_names, key: ip, value: 127.0.0.1, state: present }
    - { type: alt_names, section: alt_names, key: ip, value: 192.168.8.1, state: present }
- type: ca
  name: ca1
  done: True
  openssl_cnf: []

```

```python
from xh_ini_modifier import IniFile, OpenSSLConfigLoader, OpenSSLConfigMeta, OpenSSLConfigMetaRow
config = [
    config
    for config in OpenSSLConfigLoader.load(".config.yaml")
    if not config.done and config.name == "ca"][0]
print(IniFile.modify("openssl.cnf", config))

OpenSSLConfigLoader.load_as_list(".config.yaml") # return list of OpenSSLConfigMeta
OpenSSLConfigLoader.load_as_stream(".config.yaml") # return stream of OpenSSLConfigMeta
```

## Script writer
A simple script writer function to write script file with executable permission.

```python
from xh_utils_script_file_writer import ScriptWriter
ScriptWriter.write_script("test.sh",lambda f: f.write("hello world"), executable=True)
ScriptWriter.write_script_text("test.sh","hello world", executable=True)
```

## xh_utils_file_changes

In case we have log file from apache web server, the log file name is "access.log", the log will be renamed to "access.log-{YYYYmmdd}" daily. \
The configuration can be done as below to capture the all the log file content even after renamed to new file name.

```python
import xh_utils_file_changes as fc
import datetime as dt

fileName = "access.log"

# Please see the RenameHandler source code for detail
# The return value for getFunction() is callable for f"{fileName}{separator}{date}"
renameStrategy = fc.RenameHandler(date=dt.date.today(), separator="-")

fpu = fc.FileProgressUtils()  # create the file progress utils
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

## xh_utils_ip

IPv4 string handling utils

```python
import xh_utils_ip as ipu

# convert string "192.168.8.1/16" to ipu.Ip object
ip = ipu.Ip.from_regular_form("192.168.8.1/16")
print(ip.binary_notation())  # print in binary format

ipResults = [
    print(f"{ipStr}[{pow(2, 32 - ip.ip_seg[4])}] {ip.binary_notation()}")
    for ipStr in
    "10.91.132.0/22\n10.91.136.0/21\n10.91.144.0/20\n10.91.160.0/19\n10.91.196.0/22\n10.91.200.0/21\n10.91.208.0/20\n10.91.224.0/19".split(
        "\n")
    for ip in [ipu.Ip.from_regular_form(ipStr)]
]
```

Find host by ip if applicable
```python
from xh_utils_ip import defaultIpHostFinder as ipHostFinder
ipHostFinder.find("127.0.0.1")
```

## xh_utils_string

```python
import xh_utils_string as su

su.repeat_str()
```

## xh_utils_apache_log

```python
from xh_utils_apache_log import LogLine

with open("{==== apache log =====}", "r") as f:
    loglinesg = [LogLine.read_log_lines(line) for line in f.readlines()]

```

## progress_printer
Progress Printer responsible to produce less screen print to ensure the program running as expected.
Mainly used for dev env.

```python
from xh_utils_progress import ProgressPinger

pinger = ProgressPinger(
    print_every_n_count=100,  # print a progress log every hundred times call ping method
    print_every_n_second=15  # print a progress log every 15 second if not meeting 100 record processing
)

while True:
    pinger.ping()
    pass
```