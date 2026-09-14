---
title: ftp_ssl_connect
description: Abierto una conexión FTP segura con SSL
source_url: https://www.php.net/manual/es/function.ftp-ssl-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-ssl-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 11a4d4964
order: 24690
---

ftp_ssl_connect

Abierto una conexión FTP segura con SSL

## Descripción

```php
ftp_ssl_connect(string $hostname, [int $port], [int $timeout]): FTP\Connection
```php

`ftp_ssl_connect` abre *explícitamente* una conexión SSL-FTP al `hostname` especificado. Esto implica que `ftp_ssl_connect` tendrá éxito incluso si el servidor no está configurado para SSL-FTP. Es únicamente cuando `ftp_login` es llamado, que el cliente recibirá la orden `AUTH FTP` apropiada, entonces `ftp_login` fallará. La conexión establecida por `ftp_ssl_connect` *no* realizará ninguna verificación del certificado de par.

> [!NOTE]
> Anterior a PHP 7.0.0, `ftp_ssl_connect` solo estaba disponible si el módulo ftp y el soporte [OpenSSL](#ref.openssl) habían sido compilados estáticamente en php; esto significa que, bajo Windows, esta función no estaba definida en la versión oficial de PHP. Para tener esta función disponible bajo Windows, era necesario compilar los propios binarios PHP.

> [!NOTE]
> `ftp_ssl_connect` no está previsto para funcionar con sFTP. Para utilizar sFTP con PHP, consúltese la función `ssh2_sftp`.

## Parámetros

`hostname`  
La dirección FTP del servidor. Este parámetro no debe contener barra final y no debe estar prefijado por `ftp://`.

`port`  
Este parámetro especifica un puerto alternativo de conexión. Si es omitido o definido a cero, entonces el puerto por defecto FTP, 21, será utilizado.

`timeout`  
Este parámetro especifica el tiempo de espera de conexión para todas las operaciones sobre el red. Si es omitido, el valor por defecto será de 90 segundos. Este tiempo de espera de conexión puede ser modificado y consultado en cualquier momento con las funciones `ftp_set_option` y `ftp_get_option`.

## Valores devueltos

Devuelve una instancia de `FTP\Connection` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `FTP\Connection`; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `ftp_ssl_connect`

```
<?php

// Establecimiento de una conexión básica
$ftp = ftp_ssl_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);
if (!$login_result) {
    // PHP ya habrá lanzado un mensaje de nivel E_WARNING en este caso
    die("no se ha podido iniciar sesión");
}

echo ftp_pwd($ftp);

// Cierre de la conexión SSL
ftp_close($ftp);
?>

    
```php

## Véase también

`ftp_connect`
