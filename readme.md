# Reference

- https://regex101.com/r/xDfSqj/2
- https://www.22nds.com/access-log-apache-parsing/

# How to use

```
python convert.py
```

# Header

- ip_address
- remote_log_name
- userid
- date
- timezone
- request_method
- path
- request_version
- status
- length
- referrer
- user_agent
- session_id
- virtual_host

# Example Log

```
- 103.4.167.101 - - [08/Mar/2021:06:25:07 +0700] "HEAD / HTTP/1.0" 200 0 "-" "-" "-" -
- 40.77.167.6 - - [08/Mar/2021:06:25:28 +0700] "GET /index.php/article/81/378 HTTP/1.1" 200 737361 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-" 172.17.0.11:443
- 66.249.71.69 - - [08/Mar/2021:06:25:31 +0700] "GET /robots.txt HTTP/1.1" 404 152 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "-" -
```

# Example Result CSV

- From

```
40.77.167.6 - - [08/Mar/2021:06:25:28 +0700] "GET /index.php/article/81/378 HTTP/1.1" 200 737361 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-" 172.17.0.11:443
```

- To
  Header | Log
  --- | ---
  ip_address | 40.77.167.6  
  remote_log_name | -
  userid | -
  date | [08/Mar/2021:06:25:28
  timezone | +0700]
  request_method | "GET
  path | /index.php/article/81/378
  request_version | HTTP/1.1"
  status | 200
  length | 737361
  referrer | "-"
  user_agent | "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
  session_id | "-"
  virtual_host | 172.17.0.11:443

# Example Different Format Log

```
192.241.226.104 - - [08/Mar/2021:07:49:35 +0700] "\x16\x03\x01\x00\x8D\x01\x00\x00\x89\x03\x03\x80Q\xA5\xF2\xE8\xB8\xBE" 400 182 "-" "-" "-" -
89.248.172.90 - - [08/Mar/2021:12:26:05 +0700] "\x04\x01\x00P3OU\xBE0\x00" 400 182 "-" "-" "-" -
89.248.172.90 - - [08/Mar/2021:12:26:06 +0700] "\x05\x01\x00" 400 182 "-" "-" "-" -
```
