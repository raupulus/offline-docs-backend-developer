---
title: $_POST
description: Datos de formulario de solicitudes HTTP POST
source_url: https://www.php.net/manual/es/reserved.variables.post.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/post.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: f56de7ebe
order: 4200
---

\$\_POST

Datos de formulario de solicitudes HTTP POST

## Descripción

Un array asociativo de variables pasadas al script actual a través del método POST de HTTP cuando se emplea `application/x-www-form-urlencoded` o `multipart/form-data` como Content-Type de HTTP en la petición.

## Ejemplos

Ejemplo de `$_POST`

```php
<?php
echo '¡Hola ' . htmlspecialchars($_POST["name"]) . '!';
?>

    
```

Asumiendo que el usuario envió una solicitud POST con `name=Hannes` en el cuerpo.

Resultado del ejemplo anterior es similar a:

    ¡Hola Hannes!

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

> [!NOTE]
> Para leer datos enviados mediante POST con otros tipos de contenido (por ejemplo, `application/json` o `application/xml`), se debe utilizar [`php://input`](#wrappers.php.input). A diferencia de `$_POST`, que solo funciona con `application/x-www-form-urlencoded` y `multipart/form-data`, `php://input` proporciona acceso directo a los datos sin procesar del cuerpo de la solicitud.

## Véase también

[Manejo de variables externas](#language.variables.external), [La extensión filter](#book.filter)
