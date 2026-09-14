---
title: mysqli::real_connect
description: Establece una conexión con un servidor MySQL
source_url: https://www.php.net/manual/es/mysqli.real-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/real-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 71ebfcb54
order: 55270
---

mysqli::real_connect

mysqli_real_connect

Establece una conexión con un servidor MySQL

## Descripción

Estilo orientado a objetos

```php
public #[\SensitiveParameter] mysqli::real_connect([string $hostname], [string $username], [string $password], [string $database], [int $port], [string $socket], [int $flags]): bool
```php

Estilo procedimental

```php
#[\SensitiveParameter] mysqli_real_connect(mysqli $mysql, [string $hostname], [string $username], [string $password], [string $database], [int $port], [string $socket], [int $flags]): bool
```

Abre una conexión al servidor de base de datos MySQL con opciones de conexión opcionales.

Esta función difiere de `mysqli_connect`:

- `mysqli_real_connect` requiere un objeto válido que debe ser creado por `mysqli_init`.

- Existe un parámetro adicional `flags`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`hostname`  
Puede ser un nombre de host o una dirección IP. Al pasar `null`, el valor se recupera desde [mysqli.default_host](#ini.mysqli.default-host). Si es posible, se utilizarán pipes en lugar del protocolo TCP/IP. El protocolo TCP/IP se utiliza si se proporciona un nombre de host y un número de puerto juntos, por ejemplo `localhost:3308`.

`username`  
El nombre de usuario MySQL o `null` para asumir el nombre de usuario según la opción ini [mysqli.default_user](#ini.mysqli.default-user).

`password`  
La contraseña MySQL o `null` para asumir la contraseña según la opción ini [mysqli.default_pw](#ini.mysqli.default-pw).

`database`  
La base de datos por defecto a utilizar al ejecutar consultas o `null`.

`port`  
El número de puerto al que intentar conectarse al servidor MySQL o `null` para asumir el puerto según la opción ini [mysqli.default_port](#ini.mysqli.default-port).

`socket`  
El socket o el pipe nombrado que debería utilizarse, o `null` para asumir el socket según la opción ini [mysqli.default_socket](#ini.mysqli.default-socket).

> [!NOTE]
> Especificar explícitamente el parámetro `socket` no determina el tipo de método utilizado al conectarse a MySQL. El método se determina por el parámetro `hostname`.

`flags`  
Con el parámetro `flags`, se pueden configurar diferentes directivas de conexión:

| Nombre | Descripción |
|----|----|
| `MYSQLI_CLIENT_COMPRESS` | Utiliza el protocolo comprimido |
| `MYSQLI_CLIENT_FOUND_ROWS` | Devuelve el número de filas encontradas, no el número de filas afectadas. |
| `MYSQLI_CLIENT_IGNORE_SPACE` | Permite espacios entre los nombres de funciones y los argumentos. Esto fuerza a que los nombres de funciones sean palabras reservadas. |
| `MYSQLI_CLIENT_INTERACTIVE` | Permite `interactive_timeout` segundos (en lugar de `wait_timeout` segundos) de inactividad antes de cerrar la conexión. |
| `MYSQLI_CLIENT_SSL` | Utiliza el cifrado SSL |
| `MYSQLI_CLIENT_SSL_DONT_VERIFY_SERVER_CERT` | Igual que `MYSQLI_CLIENT_SSL`, pero desactiva la validación de los certificados SSL proporcionados. Esta constante está prevista solo para instalaciones que utilizan el driver MySQL nativo y MySQL 5.6 o superior. |

Opciones soportadas {#mysqli.real-connect.flags}

> [!NOTE]
> Por razones de seguridad, la opción `MULTI_STATEMENT` no es soportada en PHP. Si se desea ejecutar múltiples comandos, utilice la función `mysqli_multi_query`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Historial de cambios

| Versión | Descripción                              |
|---------|------------------------------------------|
| 7.4.0   | Todos los parámetros son ahora nullable. |

## Ejemplos

Ejemplo con mysqli::real_connect

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_init();

$mysqli->options(MYSQLI_INIT_COMMAND, 'SET AUTOCOMMIT = 0');
$mysqli->options(MYSQLI_OPT_CONNECT_TIMEOUT, 5);

$mysqli->real_connect('localhost', 'my_user', 'my_password', 'my_db', null, null, MYSQLI_CLIENT_COMPRESS|MYSQLI_CLIENT_FOUND_ROWS);

echo 'Éxito... ' . $mysqli->host_info . "\n";

   
```

Estilo orientado a objetos, con extensión de la clase mysqli

```php
<?php

class foo_mysqli extends mysqli {
    public function __construct($host, $user, $pass, $db)
    {
        parent::__construct();

        parent::options(MYSQLI_INIT_COMMAND, 'SET AUTOCOMMIT = 0');
        parent::options(MYSQLI_OPT_CONNECT_TIMEOUT, 5);

        parent::real_connect($host, $user, $pass, $db, null, null, MYSQLI_CLIENT_COMPRESS|MYSQLI_CLIENT_FOUND_ROWS);
    }
}

$db = new foo_mysqli('localhost', 'my_user', 'my_password', 'my_db');

echo 'Éxito... ' . $db->host_info . "\n";

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_init();

mysqli_options($link, MYSQLI_INIT_COMMAND, 'SET AUTOCOMMIT = 0');
mysqli_options($link, MYSQLI_OPT_CONNECT_TIMEOUT, 5);

mysqli_real_connect($link, 'localhost', 'my_user', 'my_password', 'my_db', null, null, MYSQLI_CLIENT_COMPRESS|MYSQLI_CLIENT_FOUND_ROWS);

echo 'Éxito... ' . mysqli_get_host_info($link) . "\n";
?>

   
```

Los ejemplos anteriores mostrarán:

    Éxito... MySQL host info: localhost via TCP/IP

## Notas

> [!NOTE]
> MySQLnd siempre asume el juego de caracteres predeterminado del servidor. Este juego de caracteres es enviado durante el intercambio de conexión/autenticación, el cual mysqlnd utilizará.
>
> Libmysqlclient utiliza el juego de caracteres predeterminado establecido en el `my.cnf` o mediante una llamada explícita a `mysqli_options` antes de llamar a `mysqli_real_connect`, pero después de `mysqli_init`.

## Véase también

`mysqli_connect`, `mysqli_init`, `mysqli_options`, `mysqli_ssl_set`, `mysqli_close`
