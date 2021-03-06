Usage
=====

```
domain-connect-dyndns [-h] [--config CONFIG] (--domain DOMAIN | --all) {setup,update,status,remove}
```

Positional arguments:
- {setup,update,status,remove} --- action on domain

Optional arguments:
- --config CONFIG --- config file path
- --domain DOMAIN --- domain to keep up to date
- --all --- update all domains in config
- --backup-file --- file path for backup domains before remove
- -h --- display help and exit


Installation
============

```   
    pip install domain-connect-dyndns
```

Examples
========
```
    domain-connect-dyndns --domain [domain] setup
    domain-connect-dyndns --domain [domain] update
    domain-connect-dyndns --domain [domain] status
    domain-connect-dyndns --domain [domain] remove
    
    domain-connect-dyndns --all update
    domain-connect-dyndns --all status
    domain-connect-dyndns --all remove
```

Installation issues
===================

- On some systems there might be no binary distribution of `cryptography` package. Additional installation stepsmay be necessary to build this package from the source code. Please refer to the package documentation: https://cryptography.io/en/latest/installation/
