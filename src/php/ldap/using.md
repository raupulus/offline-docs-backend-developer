---
title: Utilización de las funciones LDAP de PHP
source_url: https://www.php.net/manual/es/ldap.using.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/using.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 72880807a
order: 43630
---

## Utilización de las funciones LDAP de PHP

Antes de utilizar las funciones LDAP, debe conocerse :

- El nombre o la dirección del servidor de directorios que se desea utilizar

- El "base dn" del servidor (la parte del directorio mundial que está disponible en este servidor, lo cual puede ser "o=Mi Compañía,c=FR")

- La posible contraseña de acceso al servidor (muchos servidores proporcionan acceso anónimo en lectura, pero requieren contraseñas para todo lo demás).

La secuencia LDAP típica que se ejecutará será la siguiente :

\
ldap_connect()    // establece una conexión al servidor\
   \|\
ldap_bind()       // conexión anónima o identificada\
   \|\
realización de comandos como búsquedas o modificaciones, luego visualización del resultado.\
   \|\
ldap_close()      // desconexión\
