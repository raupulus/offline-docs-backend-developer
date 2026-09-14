---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/mysqli.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 48ce43fe7
order: 56080
---

## Instalación/Configuración

## Requisitos

Para que estas funciones estén disponibles, es necesario compilar PHP con el soporte de la extensión mysqli.

**MySQL 8**

Si PHP es utilizado en una versión anterior a la 7.1.16, o PHP 7.2 anterior a 7.2.4, el plugin de contraseña debe ser definido a *mysql_native_password* para MySQL 8 Server, ya que de lo contrario pueden aparecer errores similares a *The server requested authentication method unknown to the client \[caching_sha2_password\]* incluso si *caching_sha2_password* no es utilizado.

Esto se debe a que MySQL 8 utiliza por omisión caching_sha2_password, un plugin que no es reconocido por las versiones antiguas de PHP (mysqlnd). En su lugar, es necesario modificar el parámetro `default_authentication_plugin=mysql_native_password` en `my.cnf`. El plugin *caching_sha2_password* es completamente soportado a partir de PHP 7.4.4. Para versiones anteriores, la extensión [mysql_xdevapi](#book.mysql-xdevapi) lo soporta.
