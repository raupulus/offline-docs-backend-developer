---
title: gettext
description: Busca un mensaje en el dominio actual
source_url: https://www.php.net/manual/es/function.gettext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gettext/functions/gettext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gettext
translation_status: ready
translation_reviewed: false
translation_revision: 9dea6e3d7
order: 26390
---

gettext

Busca un mensaje en el dominio actual

## Descripción

```php
gettext(string $message): string
```php

Busca un mensaje en el dominio actual.

## Parámetros

`message`  
El mensaje a traducir.

## Valores devueltos

Devuelve un string traducido, si se encuentra uno en la tabla de traducción, o bien el mensaje `message`, si no se encuentra.

## Ejemplos

Ejemplo con `gettext`

```
<?php
// Selección del alemán
putenv('LC_ALL=de_DE');
setlocale(LC_ALL, 'de_DE');

// Especifica la localización de las tablas de traducción
bindtextdomain("myPHPApp", "./locale");

// Elige el dominio
textdomain("myPHPApp");

// La traducción se busca en ./locale/de_DE/LC_MESSAGES/myPHPApp.mo

// Mostrar un mensaje de prueba
echo gettext("Bienvenido a mi aplicación PHP");

// O utiliza el alias _() para reemplazar gettext()
echo _("Que tengas un buen día");
?>

    
```php

## Notas

> [!NOTE]
> Puede utilizarse el carácter guión bajo (\_) como alias de esta función.

> [!NOTE]
> Definir un idioma no es suficiente para algunos sistemas operativos y puede ser necesario utilizar la función `putenv` para definir la configuración local actual.

## Véase también

`_`, `setlocale`
