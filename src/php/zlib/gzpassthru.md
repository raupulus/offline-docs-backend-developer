---
title: gzpassthru
description: Muestra todos los datos restantes a partir del apuntador al achivo gz
source_url: https://www.php.net/manual/es/function.gzpassthru.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzpassthru.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 15352977c
order: 108850
---

gzpassthru

Muestra todos los datos restantes a partir del apuntador al achivo gz

## Descripción

```php
gzpassthru(resource $stream): int
```php

Lee hasta el EOF desde la posición en el apuntador al archivo gz y escribe los resultados (sin comprimir) en la salida estándar.

> [!NOTE]
> Se puede necesitar llamar a la función `gzrewind` para restablecer el apuntador al inicio del archivo, si ya se han escrito datos en él.

> [!TIP]
> Si sólo se desea volcar el contenido de un archivo en el buffer de salida, sin modificarlo primero o buscando una posición particular, se puede usar la función `readgzfile`, la cual ahorra el llamado a la función `gzopen`.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

## Valores devueltos

El número de caracteres sin comprimir leídos de `gz` y pasados a través de la entrada.

## Ejemplos

Ejemplo de `gzpassthru`

```
<?php
$fp = gzopen('file.gz', 'r');
gzpassthru($fp);
gzclose($fp);
?>

    
```php
