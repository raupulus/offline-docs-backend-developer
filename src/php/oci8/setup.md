---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/oci8.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: 9e2d8231b
order: 58530
---

## Instalación/Configuración

## Requisitos

OCI8 3.0 está incluida con PHP 8. También está disponible desde [PECL](https://pecl.php.net/). Para PHP 7, utilice OCI8 2.2 desde [PECL](https://pecl.php.net/). OCI8 requiere Oracle 10*g* o bibliotecas cliente posteriores.

Si la base de datos Oracle está en la misma máquina que PHP, el software de base de datos ya contiene las bibliotecas y encabezados necesarios. Cuando PHP está en una máquina diferente, utilice las bibliotecas gratuitas [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html).

Para utilizar Oracle Instant Client, instale el archivo comprimido ZIP `Basic` o `Basic Light` de Oracle Instant Client, el paquete RPM, o el paquete DMG. Al compilar OCI8 desde el código fuente, instale también el `SDK` de Instant Client.

Debe ejecutar PHP con la misma versión o una versión más reciente de las bibliotecas cliente de Oracle utilizadas para construir OCI8.

> [!NOTE]
> La interoperabilidad estándar de red cliente-servidor de Oracle permite conexiones entre diferentes versiones de Oracle Client y Oracle Database. Para configuraciones certificadas, consulte la documentación Oracle Support ID ID 207303.1. En resumen, Oracle Client 19, 18 y 12.2 pueden conectarse a Oracle Database 11.2 o superior. Oracle Client 12.1 puede conectarse a Oracle Database 10.2 o superior. Oracle Client 11.2 puede conectarse a Oracle Database 9.2 o superior.

> [!NOTE]
> El soporte de todas las funcionalidades de OCI8 solo está disponible al utilizar las versiones más recientes de las bibliotecas cliente de Oracle así como la base de datos más reciente.
