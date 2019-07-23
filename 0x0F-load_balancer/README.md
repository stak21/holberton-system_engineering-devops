#0x0F. Load balancer
---
## Description

This project in the low_level_programming series is about:

*  Given 3 servers in total, create a web stack so there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

---
File|Task
---|---
[0-custom_http_response-header ](./0-custom_http_response-header ) | Configure Nginx so it responds with custom headers
[1-install_load_balancer ](./1-install_load_balancer ) | Install HAproxy with the following requirements - HAproxy -ver 1.5+, roundrobin algorithm, HAproxy managed by init script, servers are configured with the right hostnames

## Author
 Shoji Takashima
