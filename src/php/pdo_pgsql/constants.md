---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/ref.pdo-pgsql.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 858400b07
order: 62480
---

## Constantes predefinidas

Las constantes a continuación son definidas por este controlador y solo estarán disponibles cuando la extensión haya sido compilada en PHP o cargada dinámicamente del motor de ejecución. Además, estas constantes específicas del controlador deberían ser usadas solo si se usa este controlador. Usar atributos específicos de un controlador con otro controlador podría causar un comportamiento inesperado. `PDO::getAttribute` podría ser usado para obtener el atributo `PDO::ATTR_DRIVER_NAME` para verificar el controlador, si su código puede funcionar en múltiples controladores.

`PDO::PGSQL_ATTR_DISABLE_PREPARES` (`int`)  
Alias de `Pdo\Pgsql::ATTR_DISABLE_PREPARES`. A partir de PHP 8.5.0, esta constante está obsoleta.

`PDO::PGSQL_TRANSACTION_IDLE` (`int`)  
Equivalente a `Pdo\Pgsql::TRANSACTION_IDLE`. A partir de PHP 8.5.0, esta constante está obsoleta, ya que no tiene efecto.

`PDO::PGSQL_TRANSACTION_ACTIVE` (`int`)  
Equivalente a `Pdo\Pgsql::TRANSACTION_ACTIVE`. A partir de PHP 8.5.0, esta constante está obsoleta, ya que no tiene efecto.

`PDO::PGSQL_TRANSACTION_INTRANS` (`int`)  
Equivalente a `Pdo\Pgsql::TRANSACTION_INTRANS`. A partir de PHP 8.5.0, esta constante está obsoleta, ya que no tiene efecto.

`PDO::PGSQL_TRANSACTION_INERROR` (`int`)  
Equivalente a `Pdo\Pgsql::TRANSACTION_INERROR`. A partir de PHP 8.5.0, esta constante está obsoleta, ya que no tiene efecto.

`PDO::PGSQL_TRANSACTION_UNKNOWN` (`int`)  
Equivalente a `Pdo\Pgsql::TRANSACTION_UNKNOWN`. A partir de PHP 8.5.0, esta constante está obsoleta, ya que no tiene efecto.
