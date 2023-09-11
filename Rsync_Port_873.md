
# Rsync (Port 873)

## Overview

- rsync is a remote synchronization tool used for transferring and synchronizing files between two systems efficiently.
- It is often used for backup and mirroring purposes.

### Basic Usage

The basic syntax for rsync is as follows:
```bash
rsync [options] source destination
```
Example:
```bash
rsync -avz /local/directory/ user@remote:/remote/directory/
```
<br>
<br>

## Manual Enumeration

**1. Use nc or telnet to connect.**

  ```bash
    nc [IP] [port]
  ```

**2. List the available rsync modules by entering the following command:**

  ```bash
    @RSYNCD: 31.0    
    #list          
  ```
  - Replace 31.0 with the version numbers obtained from the banner.

_**This command should list the available modules on the rsync server.**_

**3. See the contents of an rsync module**
  ```bash
    rsync --list-only rsync://<target>::<module_name>
  ```

## Exploitation

- **If no Authentication is required**
  - Try to read files.
  - Try to upload ssh files.
