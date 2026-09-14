---
title: Lista de secciones de php.ini
source_url: https://www.php.net/manual/es/ini.sections.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/ini.sections.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: d4d5216e7
order: 140
---

## Lista de secciones de `php.ini`

Esta lista incluye las secciones de `php.ini` que se pueden establecer para configurar los ajustes de PHP según cada servidor o ruta. Estas secciones son opcionales.

Estas secciones no afectan directamente a PHP. Se utilizan para agrupar otras directivas de `php.ini` y hacerlas funcionar para un servidor o ruta determinados.

Estas secciones solo se utilizan en modo CGI/FastCGI y no pueden configurar directivas de [extensión](#ini.extension) ni de [zend_extension](#ini.zend-extension).

| Nombre                     | Cambiable    | Historial de cambios |
|----------------------------|--------------|----------------------|
| [\[HOST=\]](#ini.per-host) | `INI_SYSTEM` |                      |
| [\[PATH=\]](#ini.per-path) | `INI_SYSTEM` |                      |

Secciones

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`[HOST=<host>]`  
Esta sección permite definir un conjunto de directivas de `php.ini` que afectarán solamente al servidor designado.

Activar la notificación completa de errores por pantalla para el dominio dev.

```php
[HOST=dev.site.com]
error_reporting = E_ALL
display_errors = On

       
```

`[PATH=<path>]`  
Esta sección permite definir un conjunto de directivas de `php.ini` que tomarán efecto al ejecutar un script en la ruta designada.

Añadir un script de seguridad para aréas protegidas

```php
[PATH=/home/site/public/secure]
auto_prepend_file=security.php

       
```
