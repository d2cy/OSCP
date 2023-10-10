
## Steps :

### Host Machine

1. Download the build alpine

```bash
git clone https://github.com/saghul/lxd-alpine-builder.git
```

```bash
cd lxd-alpine-builder
```

```bash
./build-alpine
```

2. Transfer tar file from host to target machine.

### Target Machine


```bash
lxc image import [TAR_FILE] --alias xyz
```

```bash
lxc init xyz ignite -c security.privileged=true
lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
lxc start ignite
lxc exec ignite /bin/sh

```


