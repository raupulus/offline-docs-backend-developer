---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pdo-odbc.global.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_odbc/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_odbc
translation_status: ready
translation_revision: 8d40a1fab
order: 62440
---

## Constantes predefinidas

Las constantes a continuación son definidas por este controlador y solo estarán disponibles cuando la extensión haya sido compilada en PHP o cargada dinámicamente del motor de ejecución. Además, estas constantes específicas del controlador deberían ser usadas solo si se usa este controlador. Usar atributos específicos de un controlador con otro controlador podría causar un comportamiento inesperado. `PDO::getAttribute` podría ser usado para obtener el atributo `PDO::ATTR_DRIVER_NAME` para verificar el controlador, si su código puede funcionar en múltiples controladores.

`PDO_ODBC_TYPE` (`string`)  
Describe la biblioteca ODBC enlazada con la extensión PDO_ODBC. Los valores posibles incluyen `unixODBC`, `iODBC` o `generic`.

> [!WARNING]
> Las constantes listadas a continuación están *OBSOLETAS* a partir de PHP 8.5.0. Utilice las constantes correspondientes de `Pdo\Odbc` en su lugar.

`PDO::ODBC_ATTR_USE_CURSOR_LIBRARY` (`int`)  
Alias de `Pdo\Odbc::ATTR_USE_CURSOR_LIBRARY`.

`PDO::ODBC_SQL_USE_IF_NEEDED` (`int`)  
Alias de `Pdo\Odbc::SQL_USE_IF_NEEDED`.

`PDO::ODBC_SQL_USE_DRIVER` (`int`)  
Alias de `Pdo\Odbc::SQL_USE_DRIVER`.

`PDO::ODBC_SQL_USE_ODBC` (`int`)  
Alias de `Pdo\Odbc::SQL_USE_ODBC`.

`PDO::ODBC_ATTR_ASSUME_UTF8` (`bool`)  
Alias de `Pdo\Odbc::ATTR_ASSUME_UTF8`.
