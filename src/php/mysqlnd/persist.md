---
title: Conexiones persistentes
source_url: https://www.php.net/manual/es/mysqlnd.persist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlnd/persist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlnd
translation_status: ready
translation_revision: 9598935f2
order: 56180
---

## Conexiones persistentes

**Utilizar conexiones persistentes**

Si `mysqli` se utiliza con `mysqlnd`, cuando se crea una conexión persistente, se genera una llamada `COM_CHANGE_USER` (`mysql_change_user()`) en el servidor. Esto asegura que la re-autenticación de la conexión se lleva a cabo.

Dado que hay una cierta sobrecarga asociada con la llamada `COM_CHANGE_USER`, es posible apagar esto en el tiempo de compilado. La reutilización de una conexión persistente entonces generará una llamada `COM_PING` (`mysql_ping`) para simplemente probar si la conexión es reusable.

La generación de `COM_CHANGE_USER` se puede apagar con el marcador de compilación `MYSQLI_NO_CHANGE_USER_ON_PCONNECT`. Por ejemplo:

    shell# CFLAGS="-DMYSQLI_NO_CHANGE_USER_ON_PCONNECT" ./configure --with-mysql=/usr/local/mysql/ --with-mysqli=/usr/local/mysql/bin/mysql_config --with-pdo-mysql=/usr/local/mysql/bin/mysql_config --enable-debug && make clean && make -j6

O, alternativamente:

    shell# export CFLAGS="-DMYSQLI_NO_CHANGE_USER_ON_PCONNECT"
    shell# configure --whatever-option
    shell# make clean
    shell# make

Observe que solamente `mysqli` sobre `mysqlnd` utiliza `COM_CHANGE_USER`. Otra combinación de extensión-controlador emplea `COM_PING` en el uso inicial de una conexión persistente.
