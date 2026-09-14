---
title: chgrp
description: Cambia el grupo de un fichero
source_url: https://www.php.net/manual/es/function.chgrp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/chgrp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 0c9c2dd66
order: 23280
---

chgrp

Cambia el grupo de un fichero

## Descripción

```php
chgrp(string $filename, string $group): bool
```php

Intenta reemplazar el grupo propietario actual del fichero `filename` por `group`.

Solo el superusuario (root) puede cambiar el grupo propietario de un fichero arbitrariamente; los usuarios comunes solo pueden cambiar el grupo propietario de un fichero si el usuario propietario del fichero es miembro del grupo.

## Parámetros

`filename`  
Ruta hacia el fichero.

`group`  
Un nombre o un número de grupo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Modificación de grupo de un fichero

```
<?php
$filename = 'shared_file.txt';
$format = "%s's Group ID @ %s: %d\n";
printf($format, $filename, date('r'), filegroup($filename));
chgrp($filename, 8);
clearstatcache(); // no almacenar en caché el resultado de filegroup()
printf($format, $filename, date('r'), filegroup($filename));
?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

> [!NOTE]
> En Windows, esta función falla silenciosamente cuando se aplica sobre un fichero ordinario.

## Véase también

`chown`, `chmod`
