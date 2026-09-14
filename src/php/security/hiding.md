---
title: Ocultar PHP
source_url: https://www.php.net/manual/es/security.hiding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/hiding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: ab6785b01
order: 109960
---

## Ocultar PHP

En general, la seguridad por ocultación es una de las formas más débiles de seguridad. Aunque en algunos casos, es aconsejable cada pequeño elemento extra de seguridad.

Unas cuantas técnicas simples pueden ayudar a ocultar PHP, posiblemente retrasando a un atacante que esté tratando de descubrir debilidades en el sistema. Al establecer expose_php a `off` en el fichero `php.ini`, se reduce la cantidad de información disponible.

Otra táctica es configurar servidores web como Apache para interpretar diferentes tipos de ficheros por medio de PHP, ya sea con una directiva de `.htaccess` o en el propio fichero de configuración de Apache. Así se pueden utilizar extensiones de ficheros engañosas:

Ocultando PHP como si fuera otro lenguaje

```php
## Hacer que el código de PHP parezca otro tipo de código
AddType application/x-httpd-php .asp .py .pl

   
```

U ocultarlo completamente:

Utilizar tipos desconocidos para extensiones de PHP

```php
## Hacer que el código de PHP parezca de tipo desconocido
AddType application/x-httpd-php .bop .foo .133t

   
```

U ocultarlo como código HTML, lo cual tiene un pequeño impacto de rendimiento debido a que todos los ficheros HTML serán procesados por el motor de PHP:

Utilizar tipos HTML para extensiones de PHP

```php
## Hacer que el código de PHP parezca HTML
AddType application/x-httpd-php .htm .html

   
```

Para que esto funcione eficazmente, se debe cambiar el nombre de los ficheros PHP con las extensiones de arriba. Si bien es una forma de seguridad por ocultamiento, es una medida preventiva menor con pocos inconvenientes.
