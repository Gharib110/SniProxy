# SniProxy
SniProxy based on dnsmasq and nginx
It works like shecan.ir in Iran

## How to Run ?!
- Install docker and docker-compose
- Run with `` docker-compose up -d ``
- Change docker-compose.yml based on your preferences !
- I try to update the `` dnsmasq/proxy.conf `` file based on the internet status of Iran
- It could be resource intensive task to serve this dns service to many people so bring a powerhouse
- I tested on a 2gigs 2 cpus vps and It is OK for me and my family and friends
- It is not safe to use it as Plain DNS, configure it with DOH. Use `` dnscrypt/doh-proxy ``
- Also try to limit dnsmasq  to `` lo `` interface, localhost
- Put Doh-Proxy behind a reverse proxy
- I wrote a script to add all sanctioned domains in Iran into multiple files
- You can use it to update your domains list

## Thanks !
[v2ray](https://github.com/v2ray/domain-list-community)
[v2fly](https://github.com/v2fly/domain-list-community)
