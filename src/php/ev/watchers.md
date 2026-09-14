---
title: Watchers
source_url: https://www.php.net/manual/es/ev.watchers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/watchers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18790
---

## Watchers

Un watcher es un objeto creado para registrar particularidades de un evento. Por ejemplo, el código siguiente espera que `STDIN` se vuelva accesible en lectura:

```php
<?php
// Esperar hasta que STDIN sea legible
$w = new EvIo(STDIN, Ev::READ, function ($watcher, $revents) {
 echo "STDIN es accesible en lectura\n";
});
Ev::run(Ev::RUN_ONCE);
?>

  
```

Todos los constructores de los watchers inician automáticamente los watchers. El método `createStopped` detiene un watcher (i.e. EvIo::createStopped).

Tenga en cuenta que un watcher se detendrá automáticamente cuando el objeto watcher sea destruido. Sin embargo, los objetos watchers devueltos por los constructores o los métodos de fábrica serán conservados.

Tenga en cuenta también que todos los métodos que modifican las propiedades de un watcher (*set*, `priority` etc.) detienen y reinician automáticamente el watcher si está activo, lo que significa que los eventos pendientes se perderán.

Ver también: [Las funciones de retrollamada de los Watchers](#ev.watcher-callbacks).
