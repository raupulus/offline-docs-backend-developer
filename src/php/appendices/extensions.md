---
title: Otros cambios en las extensiones
source_url: https://www.php.net/manual/es/migration56.extensions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration56/extensions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: f7a4ba553
order: 190
---

## Otros cambios en las extensiones

## [cURL](#book.curl)

Se han eliminado varias constantes de la biblioteca cURL, previamente marcadas como obsoletas:

- `CURLOPT_CLOSEPOLICY`

- `CURLCLOSEPOLICY_CALLBACK`

- `CURLCLOSEPOLICY_LEAST_RECENTLY_USED`

- `CURLCLOSEPOLICY_LEAST_TRAFFIC`

- `CURLCLOSEPOLICY_OLDEST`

- `CURLCLOSEPOLICY_SLOWEST`

## [OCI8](#book.oci8)

- Se ha añadido soporte para conjuntos de resultados implícitos para Oracle Database 12c a través de la nueva función `oci_get_implicit_resultset`.

- El uso de `oci_execute($s, OCI_NO_AUTO_COMMIT)` para una sentencia SELECT ya no desencadena necesariamente un ROLLBACK interno cuando se cierra la conexión.

- Se han añadido sondas DTrace controladas por la opción de configuración `--enable-dtrace`.

- `oci_internal_debug` ya no tiene efecto.

- El formato de salida de `phpinfo` para OCI8 ha cambiado.

## [Zip](#book.zip)

Se ha añadido la opción de configuración `--with-libzip` para utilizar la instalación de libzip del sistema. Se requiere la versión 0.11 de libzip, aunque se recomienda utilizar la versión 0.11.2 o superior.

## [MySQLi](#book.mysqli)

Se ha añadido una nueva opción [mysqli.rollback_on_cached_plink](#ini.mysqli.rollback-on-cached-plink) que controla el comportamiento de restauración de conexiones persistentes.
