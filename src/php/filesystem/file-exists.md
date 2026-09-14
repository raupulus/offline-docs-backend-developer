---
title: file_exists
description: Verifica si un fichero o un directorio existe
source_url: https://www.php.net/manual/es/function.file-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/file-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 871a231f4
order: 23460
---

file_exists

Verifica si un fichero o un directorio existe

## Descripción

```php
file_exists(string $filename): bool
```php

Verifica si un fichero o un directorio existe.

## Parámetros

`filename`  
Ruta de acceso al fichero o directorio.

En Windows, utilice el formato de ruta `//computername/share/filename` o `\\\\computername\share\filename` para verificar que un fichero está disponible en el recurso compartido.

## Valores devueltos

Devuelve `true` si el fichero o directorio especificado por el argumento `filename` existe; `false` en caso contrario.

> [!NOTE]
> Devuelve `false` para los enlaces simbólicos que apuntan a un fichero que no existe.

> [!NOTE]
> La verificación se realiza utilizando el UID/GID real en lugar del efectivo.

> [!NOTE]
> Como el tipo entero de PHP es firmado y que muchas plataformas utilizan enteros de 32 bits, algunas funciones relacionadas con el sistema de archivos pueden retornar resultados extraños para ficheros de tamaño superior a 2 Go.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Prueba la existencia de un fichero

```
<?php
$filename = '/path/to/foo.txt';

if (file_exists($filename)) {
    echo "El fichero $filename existe.";
} else {
    echo "El fichero $filename no existe.";
}
?>

    
```php

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`is_readable`, `is_writable`, `is_file`, `file`, `SplFileInfo`
