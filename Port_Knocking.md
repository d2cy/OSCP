# Port Knocking
 **Port knocking**  is a security technique used to enhance the security of a network by hiding open ports from potential attackers. It involves a sequence of connection attempts (knocks) to a set of **closed ports** in a **specific order**. When the correct sequence of knocks is detected by the server or firewall, it dynamically opens a previously closed port, allowing the legitimate user to access a service.


**knockd.conf** :

```ini

[openSSH]
    sequence    = 7000,8000,9000
    seq_timeout = 10
    tcpflags    = syn
    command     = /usr/sbin/iptables -A INPUT -s %IP% -j ACCEPT
[closeSSH]
    sequence    = 9000,8000,7000
    seq_timeout = 10
    tcpflags    = syn
    command     = /usr/sbin/iptables -D INPUT -s %IP% -j ACCEPT
```


### Tools to knock ports 

1. knockd 

```bash
knock <target_ip> [PORT1] [PORT2] ...
```

2. nc


```bash
nc <target_ip> [PORT1]
nc <target_ip> [PORT2]
nc <target_ip> [PORT3]
```

3. hping3

```bash
hping3 -S -p [PORT1] <target_ip> && sleep 1
hping3 -S -p [PORT2] <target_ip> && sleep 1
hping3 -S -p [PORT3] <target_ip>
```
