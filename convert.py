import csv 
import re 

# Input
log_file_name = "example_access.log" 
# Output
csv_file_name = "convert_result.csv" 
different_format_log = open("different_format.log", "w")

# Regex
parts = [
    r'(?P<ip>.*?)',
    r'(?P<remote_log_name>.*?)',    
    r'(?P<userid>.*?)',
    r'\[(?P<date>.*?)(?= )',
    r'(?P<timezone>.*?)\]',
    r'\"(?P<request_method>.*?)',
    r'(?P<path>.*?)',
    r'(?P<request_version>HTTP/.*)?\"',
    r'(?P<status>.*?)',
    r'(?P<length>.*?)',
    r'\"(?P<referrer>.*?)\"',
    r'\"(?P<user_agent>.*?)\"',
    r'(?P<session_id>.*?)',
    r'(?P<virtual_host>.*)'
] 
 
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
 
file = open(log_file_name)
 
with open(csv_file_name, 'w', newline='') as out: 
    csv_out = csv.writer(out) 
    csv_out.writerow(['ip_address', 'remote_log_name', 'userid', 'date', 'timezone', 'request_method', 'path', 'request_version', 'status', 'length', 'referrer', 'user_agent', 'session_id', 'virtual_host'])
     
    for line in file: 
        m = pattern.match(line)
        try:            
            result = m.groups()
            csv_out.writerow(result)
        except:
            different_format_log.write(line)