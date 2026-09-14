---
title: EvStat::attr
description: Devuelve el valor más reciente detectado por Ev
source_url: https://www.php.net/manual/es/evstat.attr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evstat/attr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18530
---

EvStat::attr

Devuelve el valor más reciente detectado por Ev

## Descripción

```php
public EvStat::attr(): array
```php

Devuelve un array de los valores más recientes detectados por Ev.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de los valores más recientes detectados por Ev (sin el `stat` actual):

| Clave       | Descripción                                       |
|-------------|---------------------------------------------------|
| `'dev'`     | ID del dispositivo que contiene el fichero        |
| `'ino'`     | número de inodos                                  |
| `'mode'`    | protección                                        |
| `'nlink'`   | número de enlaces duros                           |
| `'uid'`     | ID del usuario del propietario                    |
| `'size'`    | tamaño total, en bytes                            |
| `'gid'`     | ID del grupo del propietario                      |
| `'rdev'`    | ID del dispositivo (si fichero especial)          |
| `'blksize'` | tamaño del bloque para un sistema de ficheros I/O |
| `'blocks'`  | número de bloques 512B asignados                  |
| `'atime'`   | Fecha/hora del último acceso                      |
| `'ctime'`   | Fecha/Hora de la última modificación de estado    |
| `'mtime'`   | Fecha/hora de la última modificación              |

Lista de claves del array devuelto por el método EvStat::attr

Consulte la página del manual sobre `stat(2)` para más detalles.

## Ejemplos

Monitoreo de cambios en /var/log/messages

```
<?php
// Uso de un intervalo de 10 segundos.
$w = new EvStat("/var/log/messages", 8, function ($w) {
    echo "/var/log/messages ha cambiado\n";

    $attr = $w->attr();

    if ($attr['nlink']) {
        printf("Tamaño actual: %ld\n", $attr['size']);
        printf("atime actual: %ld\n", $attr['atime']);
        printf("mtime actual: %ld\n", $attr['mtime']);
    } else {
        fprintf(STDERR, "¡El fichero `messages` no está presente!");
        $w->stop();
    }
});

Ev::run();
?>

   
```php

## Véase también

EvStat::prev

EvStat::stat
