## Port Scanning
```bash
sudo nmap -v -T4 -sC -sV -p- --open [IP]

sudo nmap -sU --top-ports 100 [IP]
```
## Web

```bash
feroxbuster -u [URL] 
feroxbuster -u [URL] -w [Wordlist] -x <extensions>
gobuster dir -u [URL] -w [Wordlist] -x <extensions>

nikto -host [IP]

whatweb [URL] -v -a 3

# Subdomain Enueration
wfuzz -c -f sub-fighter -w [WORDLIST] -u [URL] -H "Host:FUZZ.[URL]" -k 
ffuf -w [WORDLIST] -u [URL] -H "Host:FUZZ.[URL]"

# Generate Password list from web
cewl -d 6 [URL]

# CMS
droopescan scan drupal -u <url>
wpscan --url <target> --enumerate p
wpscan --url <target> --enumerate t

```

#### Wordlist 

```bash
big.txt
raft-large-files.txt
raft-large-directories.txt
directory-list-2.3-small.txt

## Use Lowercase Wordlists for Windows Machines
```

## SMB
```bash
enum4linux [IP]
enum4linux -A [IP]
crackmapexec smb [IP] -u '' -p ''
crackmapexec smb [IP] -u 'Guest' -p ''

smbclient -L ////[IP]
 ```

## RPC
```bash
rpcclient -U '%' -N <IP>
rpcclient -U "" <IP>

enumdomusers


```
## LDAP
```bash
ldapsearch -H ldap://[IP] -x -s base namingcontexts
ldapsearch -H ldap://[IP] -x -b " "
```
## NFS
```bash
showmount -e [IP]

mount -t nfs [IP]:<nfs_share> <local_mount_point>  # Ex: mount -t nfs 192.168.1.1:/home /tmp/d2cy
```
## SNMP 
```bash
nmap -p 161,162 --script=snmp* [IP]

snmpbulkwalk -c [COMM_STRING] -v [VERSION] [IP] .
snmpbulkwalk -c public -v2c 10.10.11.136 .

snmpwalk -v <version> -c <community_string> [IP] .1 #Enum all
snmpwalk -v <version> -c <community_string> [IP]
snmpwalk -v <version> -c <community_string> [IP] NET-SNMP-EXTEND-MIB::nsExtendObjects

snmpwalk -v X -c public <IP> NET-SNMP-EXTEND-MIB::nsExtendOutputFull
```
