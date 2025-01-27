# SniProxy
SniProxy based on dnsmasq and nginx
It works like shecan.ir in Iran

## How to Run ?!
- Install docker and docker-compose
- Run with `` docker-compose up -d ``
- Change docker-compose.yml based on your preferences !
- I try to update the `` dnsmasq/proxy.conf `` file based on the internet status of Iran
- It could be resource intensive task to serve this dns service to many people so bring a powerhouse
- I tested on a 2gigs 2 cpus vps and It is OK for me, my family, and friends
- Also dnsmasq is limited to `` lo `` interface, localhost
- Use AdGuard Home to deploy DOT, DOH, and use it with SniProxy
- I wrote a script to add all sanctioned domains in Iran into multiple files
- You can use it to update your domains list
- I have added a hosts file which helps you to block (Ads, Malwares, Porn, Fakenews and Gambling Websites), like pi-hole but along with SniProxy Capability
- Also you can check Steven Black github repo to change the hosts file based on your preferences
- You can deploy a wiregaurd VPN on Iran VPS and set its DNS to the ip address of your SNI-PROXY
## Thanks !
[v2ray](https://github.com/v2ray/domain-list-community)
[v2fly](https://github.com/v2fly/domain-list-community)
[Steven Black](https://github.com/StevenBlack/hosts)
