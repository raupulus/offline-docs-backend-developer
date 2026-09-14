---
title: $_ENV
description: Variables de entorno
source_url: https://www.php.net/manual/es/reserved.variables.environment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/env.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: a6d209f4f
order: 4140
---

\$\_ENV

Variables de entorno

## Descripción

Una variable tipo `array` asociativo de variables pasadas al script actual a través del método del entorno.

Estas variables son importadas en el espacio de nombres global de PHP desde el entorno bajo el que está siendo ejecutado el intérprete PHP. Muchas son entregadas por el intérprete de comandos bajo el que PHP está corriendo y diferentes sistemas suelen tener diferentes tipos de intérpretes de comandos, una lista definitiva es imposible. Por favor consulte la documentación de su intérprete de comandos para una lista de las variables de entorno que se definen.

Otras variables de entorno incluyen las variables CGI, colocadas allí independientemente de que PHP esté siendo ejecutado como módulo del servidor o procesador CGI.

## Ejemplos

Ejemplo de `$_ENV`

```php
<?php
echo '¡Mi nombre de usuario es ' . $_ENV["USER"] . '!';
?>

    
```

Asumiendo que "bjori" ejecuta este script

Resultado del ejemplo anterior es similar a:

    ¡Mi nombre de usuario es bjori!

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

## Véase también

`getenv`, [La extensión filter](#book.filter)
