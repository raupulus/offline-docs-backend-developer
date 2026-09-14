---
title: EvStat::__construct
description: Construye un objeto EvStat watcher
source_url: https://www.php.net/manual/es/evstat.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evstat/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18540
---

EvStat::\_\_construct

Construye un objeto EvStat watcher

## Descripción

```php
public EvStat::__construct(string $path, float $interval, callable $callback, [mixed $data], [int $priority])
```php

Construye un objeto EvStat watcher e inicia el watcher automáticamente.

## Parámetros

`path`  
La ruta de acceso para la cual se espera una modificación de estado.

`interval`  
Intervalo de detección de una modificación; debe valer normalmente `0.0` para dejar que *libev* elija el valor adecuado.

`callback`  
Ver las [retrollamadas Watcher](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Las prioridades del Watcher](#ev.constants.watcher-pri)

## Ejemplos

Monitoreo de cambios en el directorio /var/log/messages

```
<?php
// Uso de un intervalo de 10 segundos.
 $w = new EvStat("/var/log/messages", 10, function ($w) {
 echo "/var/log/messages ha cambiado\n";

 $attr = $w->attr();

 if ($attr['nlink']) {
  printf("Tamaño actual: %ld\n", $attr['size']);
  printf("Hora de último acceso: %ld\n", $attr['atime']);
  printf("Hora de última modificación: %ld\n", $attr['mtime']);
 } else {
  fprintf(STDERR, "¡El fichero `messages` no está presente!");
  $w->stop();
 }
});

?>

   
```php
