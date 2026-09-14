---
title: phpcredits
description: Muestra los créditos de PHP
source_url: https://www.php.net/manual/es/function.phpcredits.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/phpcredits.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: f78180344
order: 39160
---

phpcredits

Muestra los créditos de PHP

## Descripción

```php
phpcredits([int $flags]): true
```php

Muestra la lista de desarrolladores de PHP, módulos, etc. Genera el código HTML apropiado para insertar la información en una página.

## Parámetros

`flags`  
Para generar una página personalizada sobre los créditos, debe utilizarse el argumento `flags`.

| Nombre | Descripción |
|----|----|
| CREDITS_ALL | Todos los créditos, equivalente a: `CREDITS_DOCS` + `CREDITS_GENERAL` + `CREDITS_GROUP` + `CREDITS_MODULES` + `CREDITS_FULLPAGE`. La función genera entonces una página HTML completa. |
| CREDITS_DOCS | Los créditos del grupo de documentación |
| CREDITS_FULLPAGE | En general, este argumento se utiliza con otras constantes. Indica que la página generada debe ser una página HTML completa, con todas las etiquetas necesarias. |
| CREDITS_GENERAL | Créditos Generales: diseño y concepción del lenguaje, autores de PHP y del módulo SAPI. |
| CREDITS_GROUP | Una lista de los desarrolladores principales |
| CREDITS_MODULES | Una lista de las extensiones de PHP y sus autores |
| CREDITS_SAPI | Una lista de las API de servidor para PHP y sus autores |

Argumentos predefinidos de `phpcredits`

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Ejemplo con `phpcredits`

```
<?php
phpcredits(CREDITS_GENERAL);
?>

    
```php

Muestra los desarrolladores principales así como el grupo de documentación

```
<?php
phpcredits(CREDITS_GROUP | CREDITS_DOCS | CREDITS_FULLPAGE);
?>

    
```php

Muestra todos los créditos

```
<html>
 <head>
  <title>Mi página de créditos</title>
 </head>
 <body>
<?php
// Un poco de su código
phpcredits(CREDITS_ALL - CREDITS_FULLPAGE);
// Más de su código
?>
 </body>
</html>

    
```php

## Notas

> [!NOTE]
> La función `phpcredits` muestra texto plano en lugar de HTML cuando se utiliza en modo CLI.

## Véase también

`phpversion`, `phpinfo`
