---
title: ftp_alloc
description: Asigna espacio para una descarga de fichero
source_url: https://www.php.net/manual/es/function.ftp-alloc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-alloc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24350
---

ftp_alloc

Asigna espacio para una descarga de fichero

## Descripción

```php
ftp_alloc(FTP\Connection $ftp, int $size, [string $response]): bool
```php

`ftp_alloc` envía el comando FTP `ALLO` para asignar espacio en el servidor FTP de `filesize` bytes.

> [!NOTE]
> Muchos servidores FTP no soportan este comando. Estos servidores pueden devolver un código de error (`false`) que indica que el comando no es soportado, o (`true`) para indicar que la preasignación no es necesaria: el cliente continúa entonces sus operaciones de la misma forma. Debido a esto, es preferible utilizar esta función solo con los servidores que requieran específicamente esta función.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`size`  
El número de bytes a asignar.

`response`  
Una representación textual de la respuesta del servidor que será devuelta por referencia en `response` si se proporciona una variable.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_alloc`

```
<?php

$file = "/home/user/myfile";

// Conexión al servidor
$ftp = ftp_connect('ftp.example.com');
$login_result = ftp_login($ftp, 'anonymous', 'user@example.com');

if (ftp_alloc($ftp, filesize($file), $result)) {
  echo "Espacio asignado con éxito en el servidor. Enviando $file.\n";
  ftp_put($ftp, '/incoming/myfile', $file, FTP_BINARY);
} else {
  echo "No se pudo asignar el espacio en el servidor. Respuesta del servidor: $result\n";
}

ftp_close($ftp);

?>

    
```php

## Véase también

`ftp_put`, `ftp_fput`
