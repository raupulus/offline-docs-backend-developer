---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/ref.pdo-firebird.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_firebird/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_firebird
translation_status: ready
translation_revision: 8d40a1fab
order: 62300
---

## Constantes predefinidas

Las constantes a continuación son definidas por este controlador y solo estarán disponibles cuando la extensión haya sido compilada en PHP o cargada dinámicamente del motor de ejecución. Además, estas constantes específicas del controlador deberían ser usadas solo si se usa este controlador. Usar atributos específicos de un controlador con otro controlador podría causar un comportamiento inesperado. `PDO::getAttribute` podría ser usado para obtener el atributo `PDO::ATTR_DRIVER_NAME` para verificar el controlador, si su código puede funcionar en múltiples controladores.

> [!WARNING]
> Las constantes listadas a continuación están *OBSOLETAS* a partir de PHP 8.5.0. Utilice las constantes correspondientes de `Pdo\Firebird` en su lugar.

`PDO::FB_ATTR_DATE_FORMAT` (`int`)  
Alias de `Pdo\Firebird::ATTR_DATE_FORMAT`.

`PDO::FB_ATTR_TIME_FORMAT` (`int`)  
Alias de `Pdo\Firebird::ATTR_TIME_FORMAT`.

`PDO::FB_ATTR_TIMESTAMP_FORMAT` (`int`)  
Alias de `Pdo\Firebird::ATTR_TIMESTAMP_FORMAT`.
