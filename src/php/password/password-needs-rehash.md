---
title: password_needs_rehash
description: Verifica que el hash proporcionado cumple con el algoritmo y las opciones
  especificadas
source_url: https://www.php.net/manual/es/function.password-needs-rehash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/password/functions/password-needs-rehash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: password
translation_status: ready
translation_reviewed: false
translation_revision: e302f0794
order: 61120
---

password_needs_rehash

Verifica que el hash proporcionado cumple con el algoritmo y las opciones especificadas

## Descripción

```php
password_needs_rehash(string $hash, string $algo, [array $options]): bool
```php

Esta función verifica que el hash proporcionado corresponde al algoritmo y a las opciones especificadas. Si no es así, el hash debería ser re-generado.

## Parámetros

`hash`  
Un hash creado por la función `password_hash`.

`algo`  
Una [constante del algoritmo de contraseña](#password.constants) que representa el algoritmo a utilizar durante el hasheo de la contraseña.

`options`  
Un array asociativo que contiene las opciones. Ver también [las constantes del algoritmo de contraseña](#password.constants) para la documentación sobre las opciones soportadas para cada algoritmo.

## Valores devueltos

Devuelve `true` si el hash debe ser re-generado para corresponder a los parámetros `algo` y `options` proporcionados, o `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | El parámetro `algo` ahora espera una `string`, pero sigue aceptando un `int` para mantener la compatibilidad con versiones anteriores. |

## Ejemplos

Uso de `password_needs_rehash`

```
<?php

$password = 'rasmuslerdorf';
$hash = '$2y$12$4Umg0rCJwMswRw/l.SwHvuQV01coP0eWmGzd61QH2RvAOMANUBGC.';

$algorithm = PASSWORD_BCRYPT;
// El parámetro cost de bcrypt puede evolucionar con el tiempo según las mejoras de hardware.
$options = ['cost' => 13];

// Primero se verifica que la contraseña coincide con el hash almacenado
if (password_verify($password, $hash)) {
    // Verifica si el algoritmo o las opciones han cambiado
    if (password_needs_rehash($hash, $algorithm, $options)) {
    if (password_needs_rehash($hash, PASSWORD_DEFAULT, $options)) {
        // Se crea un nuevo hash para actualizar el anterior
        $newHash = password_hash($password, $algorithm, $options);

        // Actualizar la entrada del usuario con $newHash
    }

    // Ejecutar el inicio de sesión del usuario
}
?>

    
```php
