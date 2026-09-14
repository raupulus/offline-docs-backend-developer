---
title: dba_handlers
description: Listar todos los gestores disponibles
source_url: https://www.php.net/manual/es/function.dba-handlers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-handlers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11570
---

dba_handlers

Listar todos los gestores disponibles

## Descripción

```php
dba_handlers([bool $full_info]): array
```php

`dba_handlers` lista todos los gestores soportados por esta extensión.

## Parámetros

`full_info`  
Activa/desactiva la mostración de la información completa en el resultado.

## Valores devueltos

Devuelve un array de gestores de bases de datos. Si `full_info` está establecido a `true`, el array será asociativo con los nombres de los gestores como claves y la información de su versión com valor. De otro modo, el resultado será un array indexado de nombres de gestores.

> [!NOTE]
> Cuando se usa la biblioteca cdb interna verá `cdb` y `cdb_make`.

## Ejemplos

Ejemplo de `dba_handlers`

```
<?php

echo "Gestores de DBA disponibles:\n";
foreach (dba_handlers(true) as $nombre_gestor => $versión_gestor) {
  // limpiar las versiones
  $versión_gestor = str_replace('$', '', $versión_gestor);
  echo " - $nombre_gestor: $versión_gestor\n";
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Gestores de DBA disponibles:
     - cdb: 0.75, Revision: 1.3.2.3
     - cdb_make: 0.75, Revision: 1.2.2.4
     - db2: Sleepycat Software: Berkeley DB 2.7.7: (08/20/99)
     - inifile: 1.0, Revision: 1.6.2.3
     - flatfile: 1.0, Revision: 1.5.2.4
