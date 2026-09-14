---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/runkit7.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/runkit7/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: runkit7
translation_status: ready
translation_revision: 3a826d03c
order: 73010
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [runkit.superglobal](#ini.runkit7.superglobal) | "" | `INI_PERDIR` |  |
| [runkit.internal_override](#ini.runkit7.internal-override) | "0" | `INI_SYSTEM` |  |

Opciones de Configuración de Runkit

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`runkit.superglobal` `string`  
Una lista separada por comas de nombres de variables que van a ser tratadas como superglobales. Este valor debería estar establecido a través del archivo php.ini, pero puede funcionar en contextos de configuración por directorio dependiendo de su SAPI.

Superglobales personalizadas con runkit.superglobal=\_FOO,\_BAR en php.ini

```php
<?php
function mostrar_valores() {
  echo "Foo es $_FOO\n";
  echo "Bar es $_BAR\n";
  echo "Baz es $_BAZ\n";
}

$_FOO = 'foo';
$_BAR = 'bar';
$_BAZ = 'baz';

/* Muestra foo y bar, pero no baz */
mostrar_valores();
?>

    
```

`runkit.internal_override` `boolean`  
Habilita la capacidad de modificar/renombrar/eliminar funciones internas.
