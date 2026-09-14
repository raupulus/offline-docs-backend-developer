---
title: Ejemplos
source_url: https://www.php.net/manual/es/win32service.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/win32service/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: win32service
translation_status: ready
translation_revision: a56106f69
order: 101280
---

## Ejemplos

Registrar un script PHP para ejecutar como servicio

```php
<?php
win32_create_service(array(
    'service'     => 'dummyphp',                                           # nombre del servicio
    'display'     => 'sample dummy PHP service',                           # descripción corta
    'description' => 'This is a dummy Windows service created using PHP.', # descripción larga
    'params'      => '"' . __FILE__ . '"  run',                            # ruta hacia el script y argumentos
));
?>

   
```

Eliminar un servicio

```php
<?php
win32_delete_service('dummyphp');
?>

   
```

Ejecutar un servicio

```php
<?php
if ($argv[1] == 'run') {
  win32_start_service_ctrl_dispatcher('dummyphp');

  while (WIN32_SERVICE_CONTROL_STOP != win32_get_last_control_message()) {
    # realizar su trabajo aquí.
    # intente no tomar más de 30 segundos antes de volver al
    # inicio del ciclo
  }
}
?>

   
```
