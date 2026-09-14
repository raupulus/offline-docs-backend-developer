---
title: enchant_broker_set_ordering
description: Declara una preferencia para un diccionario de un idioma
source_url: https://www.php.net/manual/es/function.enchant-broker-set-ordering.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/functions/enchant-broker-set-ordering.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_reviewed: false
translation_revision: a6b55f8de
order: 17440
---

enchant_broker_set_ordering

Declara una preferencia para un diccionario de un idioma

## Descripción

```php
enchant_broker_set_ordering(EnchantBroker $broker, string $tag, string $ordering): bool
```php

Declara una preferencia para un diccionario a utilizar para el idioma especificado por el argumento `tag`. El orden de los idiomas es una lista separada por comas. El carácter especial "\*" puede ser utilizado como idioma para declarar un orden por defecto para todos los idiomas que no declaren explícitamente un orden.

## Parámetros

`broker`  
Un broker Enchant devuelto por `enchant_broker_init`.

`tag`  
El idioma. El carácter "\*" puede ser utilizado como idioma para declarar un orden por defecto para todos los idiomas que no declaren explícitamente un orden.

`ordering`  
Lista de nombres de proveedores separada por comas

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `broker` ahora espera una instancia de `EnchantBroker`; anteriormente, se esperaba un `resource`. |
