---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/ref.pdo-mysql.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_mysql/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_mysql
translation_status: ready
translation_revision: 8d40a1fab
order: 62370
---

## Constantes predefinidas

Las constantes a continuación son definidas por este controlador y solo estarán disponibles cuando la extensión haya sido compilada en PHP o cargada dinámicamente del motor de ejecución. Además, estas constantes específicas del controlador deberían ser usadas solo si se usa este controlador. Usar atributos específicos de un controlador con otro controlador podría causar un comportamiento inesperado. `PDO::getAttribute` podría ser usado para obtener el atributo `PDO::ATTR_DRIVER_NAME` para verificar el controlador, si su código puede funcionar en múltiples controladores.

> [!WARNING]
> Las constantes listadas a continuación están *OBSOLETAS* a partir de PHP 8.5.0. Utilice las constantes correspondientes de `Pdo\Mysql` en su lugar.

`PDO::MYSQL_ATTR_USE_BUFFERED_QUERY` (`int`)  
Alias de `Pdo\Mysql::ATTR_USE_BUFFERED_QUERY`

`PDO::MYSQL_ATTR_LOCAL_INFILE` (`int`)  
Alias de `Pdo\Mysql::ATTR_LOCAL_INFILE`

`PDO::MYSQL_ATTR_LOCAL_INFILE_DIRECTORY` (`int`)  
Alias de `Pdo\Mysql::ATTR_LOCAL_INFILE_DIRECTORY`. Disponible a partir de PHP 8.1.0.

`PDO::MYSQL_ATTR_INIT_COMMAND` (`int`)  
Alias de `Pdo\Mysql::ATTR_INIT_COMMAND`

`PDO::MYSQL_ATTR_READ_DEFAULT_FILE` (`int`)  
Alias de `Pdo\Mysql::ATTR_READ_DEFAULT_FILE`

`PDO::MYSQL_ATTR_READ_DEFAULT_GROUP` (`int`)  
Alias de `Pdo\Mysql::ATTR_READ_DEFAULT_GROUP`

`PDO::MYSQL_ATTR_MAX_BUFFER_SIZE` (`int`)  
Alias de `Pdo\Mysql::ATTR_MAX_BUFFER_SIZE`

`PDO::MYSQL_ATTR_DIRECT_QUERY` (`bool`)  
Alias de `PDO::ATTR_EMULATE_PREPARES`

A partir de PHP 8.4.0 esta constante es de tipo `bool`; anteriormente, era de tipo `int`.

`PDO::MYSQL_ATTR_FOUND_ROWS` (`int`)  
Alias de `Pdo\Mysql::ATTR_FOUND_ROWS`

`PDO::MYSQL_ATTR_IGNORE_SPACE` (`int`)  
Alias de `Pdo\Mysql::ATTR_IGNORE_SPACE`

`PDO::MYSQL_ATTR_COMPRESS` (`int`)  
Alias de `Pdo\Mysql::ATTR_COMPRESS`

`PDO::MYSQL_ATTR_SERVER_PUBLIC_KEY` (`int`)  
Alias de `Pdo\Mysql::ATTR_SERVER_PUBLIC_KEY`

`PDO::MYSQL_ATTR_SSL_CA` (`int`)  
Alias de `Pdo\Mysql::ATTR_SSL_CA`

`PDO::MYSQL_ATTR_SSL_CAPATH` (`int`)  
Alias de `Pdo\Mysql::ATTR_SSL_CAPATH`

`PDO::MYSQL_ATTR_SSL_CERT` (`int`)  
Alias de `Pdo\Mysql::ATTR_SSL_CERT`

`PDO::MYSQL_ATTR_SSL_CIPHER` (`int`)  
Alias de `Pdo\Mysql::ATTR_SSL_CIPHER`

`PDO::MYSQL_ATTR_SSL_KEY` (`int`)  
Alias de `Pdo\Mysql::ATTR_SSL_KEY`

`PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT` (`int`)  
Alias de `Pdo\Mysql::ATTR_SSL_VERIFY_SERVER_CERT` Disponible a partir de PHP 7.0.18 y PHP 7.1.4.

`PDO::MYSQL_ATTR_MULTI_STATEMENTS` (`int`)  
Alias de `Pdo\Mysql::ATTR_MULTI_STATEMENTS`
