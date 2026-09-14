---
title: mysqli::__construct
description: Abre una conexión a un servidor MySQL
source_url: https://www.php.net/manual/es/mysqli.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 9dadf7425
order: 54980
---

mysqli::\_\_construct

mysqli::connect

mysqli_connect

Abre una conexión a un servidor MySQL

## Descripción

Estilo orientado a objetos

```php
public #[\SensitiveParameter] mysqli::__construct([string $hostname], [string $username], [string $password], [string $database], [int $port], [string $socket])
```php

```php
public #[\SensitiveParameter] mysqli::connect([string $hostname], [string $username], [string $password], [string $database], [int $port], [string $socket]): bool
```

Estilo procedimental

```php
#[\SensitiveParameter] mysqli_connect([string $hostname], [string $username], [string $password], [string $database], [int $port], [string $socket]): mysqli
```php

Abre una conexión al servidor MySQL.

## Parámetros

`hostname`  
Puede ser un nombre de host o una dirección IP. Al pasar `null`, el valor se recupera desde [mysqli.default_host](#ini.mysqli.default-host). Si es posible, se utilizarán pipes en lugar del protocolo TCP/IP. El protocolo TCP/IP se utiliza si se proporciona un nombre de host y un número de puerto juntos, por ejemplo `localhost:3308`.

Prefijar el host con `p:` abre una conexión persistente. `mysqli_change_user` se llama automáticamente en las conexiones que se utilizan en el grupo de conexiones.

`username`  
El nombre de usuario MySQL o `null` para asumir el nombre de usuario según la opción ini [mysqli.default_user](#ini.mysqli.default-user).

`password`  
La contraseña MySQL o `null` para asumir la contraseña basándose en la opción ini [mysqli.default_pw](#ini.mysqli.default-pw).

`database`  
La base de datos predeterminada a utilizar al ejecutar consultas o `null`.

`port`  
El número de puerto al que intentar conectarse al servidor MySQL o `null` para asumir el puerto según la opción ini [mysqli.default_port](#ini.mysqli.default-port).

`socket`  
El socket o el pipe nombrado que debe utilizarse, o `null` para asumir el socket según la opción ini [mysqli.default_socket](#ini.mysqli.default-socket).

> [!NOTE]
> Especificar el parámetro `socket` no determinará explícitamente el tipo de conexión que se utilizará al conectarse al servidor MySQL. Esto está determinado por el parámetro `hostname`.

## Valores devueltos

mysqli::\_\_construct siempre devuelve un objeto que representa la conexión a un servidor MySQL, incluso si la conexión ha fallado.

`mysqli_connect` devuelve un objeto que representa la conexión al servidor MySQL, o `false` si ocurre un error.

mysqli::connect devuelve `true` en caso de éxito o `false` si ocurre un error. Anterior a PHP 8.1.0, devuelve `null` en caso de éxito.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | mysqli::connect ahora devuelve `true` en lugar de `null` en caso de éxito. |
| 7.4.0 | Todos los parámetros ahora son nullable. |

## Ejemplos

Ejemplo mysqli::\_\_construct

Estilo orientado a objetos

```
<?php
/* Siempre se debe activar el informe de errores para mysqli antes de intentar una conexión */
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli('localhost', 'my_user', 'my_password', 'my_db');
/* Establecer el juego de caracteres deseado después de establecer una conexión */
$mysqli->set_charset('utf8mb4');
printf("Éxito... %s\n", $mysqli->host_info);

   
```php

Estilo procedimental

```
<?php
/* Siempre se debe activar el informe de errores para mysqli antes de intentar una conexión */
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect('localhost', 'my_user', 'my_password', 'my_db');
/* Establecer el juego de caracteres deseado después de establecer una conexión */
mysqli_set_charset($mysqli, 'utf8mb4');
printf("Éxito... %s\n", mysqli_get_host_info($mysqli));

   
```php

Los ejemplos anteriores mostrarán algo similar a:

    Éxito... localhost via TCP/IP

Extender la clase mysqli

```
<?php
class FooMysqli extends mysqli {
    public function __construct($host, $user, $pass, $db, $port, $socket, $charset) {
        mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
        parent::__construct($host, $user, $pass, $db, $port, $socket);
        $this->set_charset($charset);
    }
}
$db = new FooMysqli('localhost', 'my_user', 'my_password', 'my_db', 3306, null, 'utf8mb4');

   
```php

Manejo manual de errores

Si el informe de errores está desactivado, el desarrollador es responsable de verificar y manejar los fallos

Estilo orientado a objetos

```
<?php
error_reporting(0);
mysqli_report(MYSQLI_REPORT_OFF);
$mysqli = new mysqli('localhost', 'my_user', 'my_password', 'my_db');
if ($mysqli->connect_errno) {
    throw new RuntimeException('error de conexión mysqli: ' . $mysqli->connect_error);
}
/* Establecer el juego de caracteres deseado después de establecer una conexión */
$mysqli->set_charset('utf8mb4');
if ($mysqli->errno) {
    throw new RuntimeException('error mysqli: ' . $mysqli->error);
}

   
```php

Estilo procedimental

```
<?php
error_reporting(0);
mysqli_report(MYSQLI_REPORT_OFF);
$mysqli = mysqli_connect('localhost', 'my_user', 'my_password', 'my_db');
if (mysqli_connect_errno()) {
    throw new RuntimeException('error de conexión mysqli: ' . mysqli_connect_error());
}
/* Establecer el juego de caracteres deseado después de establecer una conexión */
mysqli_set_charset($mysqli, 'utf8mb4');
if (mysqli_errno($mysqli)) {
    throw new RuntimeException('error mysqli: ' . mysqli_error($mysqli));
}

   
```php

## Notas

> [!NOTE]
> MySQLnd siempre asume el juego de caracteres predeterminado del servidor. Este juego de caracteres es enviado durante el intercambio de conexión/autenticación, el cual mysqlnd utilizará.
>
> Libmysqlclient utiliza el juego de caracteres predeterminado establecido en el `my.cnf` o mediante una llamada explícita a `mysqli_options` antes de llamar a `mysqli_real_connect`, pero después de `mysqli_init`.

> [!NOTE]
> Estilo orientado a objetos solamente: si la conexión falla, se devuelve un objeto de todos modos. Para verificar si la conexión falló, utilice la función `mysqli_connect_error` o la propiedad [mysqli-\>connect_error](#mysqli.connect-error) como en el ejemplo anterior.

> [!NOTE]
> Si es necesario configurar opciones, como el tiempo de espera de conexión, `mysqli_real_connect` debe ser utilizado.

> [!NOTE]
> Llamar al constructor sin parámetros tiene el mismo efecto que llamar `mysqli_init`.

> [!NOTE]
> El error `"Can't create TCP/IP socket (10106)"` significa generalmente que la directiva de configuración [variables_order](#ini.variables-order) no contiene el carácter `E`. En Windows, si el entorno no se copia, la variable de entorno `SYSTEMROOT` no estará disponible y PHP tendrá problemas para cargar Winsock.

## Véase también

`mysqli_real_connect`, `mysqli_options`, `mysqli_connect_errno`, `mysqli_connect_error`, `mysqli_close`
