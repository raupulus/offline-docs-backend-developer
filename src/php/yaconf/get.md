---
title: Yaconf::get
description: Recuperar un elemento
source_url: https://www.php.net/manual/es/yaconf.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaconf/yaconf/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaconf
translation_status: ready
translation_reviewed: false
translation_revision: a464df4c7
order: 104430
---

Yaconf::get

Recuperar un elemento

## Descripción

```php
public static Yaconf::get(string $name, [mixed $default_value]): mixed
```php

## Parámetros

`name`  
Clave de configuración, la clave se ve como "filename.key", o "filename.sectionName,key".

`default_value`  
si la clave no existe, Yaconf::get devolverá esto como resultado.

## Valores devueltos

Devuelve el resultado de configuración (string o array) si la clave existe, devuelve default_value si no.

## Ejemplos

Ejemplo de `INI`

```
;filenmame foo.ini, colocado en el directorio que es yaconf.directoy
[SectionA]
;key value pair
key=val
;hash[a]=val
hash.a=val
;arr[0]=val
arr.0=val
;or
arr[]=val

;SectionB hereda SectionA
[SectionB:SectionA]
;reemplazar la clave de configuración en SectionA
key=new_val

   
```php

Resultado del ejemplo anterior es similar a:

    php7 -r 'var_dump(Yaconf::get("foo.SectionA.key"));'
    //string(3) "val"

    php7 -r 'var_dump(Yaconf::get("foo.SectionB.key"));'
    //string(7) "new_val"

    php7 -r 'var_dump(Yaconf::get("foo")["SectionA"]["hash"]);'
    //array(1)
