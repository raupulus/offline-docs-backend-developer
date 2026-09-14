---
title: ftp_set_option
description: Modifica las opciones de la conexión FTP
source_url: https://www.php.net/manual/es/function.ftp-set-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-set-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: fcd921429
order: 24660
---

ftp_set_option

Modifica las opciones de la conexión FTP

## Descripción

```php
ftp_set_option(FTP\Connection $ftp, int $option, int $value): true
```php

`ftp_set_option` controla diversas opciones de una conexión FTP especificada.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`option`  
Actualmente, las siguientes opciones son soportadas:

|  |  |
|----|----|
| `FTP_TIMEOUT_SEC` | Modifica el tiempo de espera de conexión en segundos utilizado para todas las funciones de red. `value` debe ser un integer mayor que 0. El tiempo de espera de conexión por defecto es de 90 segundos. |
| `FTP_AUTOSEEK` | Cuando está activo, las peticiones GET o PUT con un argumento `resumepos` o `startpos` se posicionarán primero en la posición deseada en el archivo. Esto está activo por defecto. |
| `FTP_USEPASVADDRESS` | Cuando está desactivado, PHP ignora la dirección IP devuelta por el servidor FTP en respuesta al comando PASV y utiliza en su lugar la dirección IP proporcionada en el ftp_connect(). `value` debe ser un valor booleano. |

Opciones FTP soportadas

`value`  
Este argumento depende de la opción `option` que se desea modificar.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se lanza una excepción ValueError si la `option` no es soportada. Se lanza una excepción TypeError si el `value` proporcionado no corresponde al tipo esperado para la `option` dada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | El tipo de retorno es ahora `true`; anteriormente, era `bool`. |
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_set_option`

```
<?php
// Definición del tiempo de espera de conexión a 10 segundos
ftp_set_option($ftp, FTP_TIMEOUT_SEC, 10);
?>

    
```php

## Véase también

`ftp_get_option`
