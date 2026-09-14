---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/password.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/password/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: password
translation_status: ready
translation_revision: 66aff414b
order: 61080
---

## Constantes predefinidas

Las constantes listadas aquí están siempre disponibles en PHP.

`PASSWORD_BCRYPT` (`string`)  
La constante `PASSWORD_BCRYPT` se utiliza para crear un nuevo hash de contraseña utilizando el algoritmo `CRYPT_BLOWFISH`.

Siempre ha devuelto el resultado del hash utilizando el formato crypt "\$2y\$", que siempre será un string de 60 caracteres de longitud.

Opciones admitidas:

- `salt` (`string`) - permite proporcionar manualmente un salt a utilizar para el hash de la contraseña. Tenga en cuenta que esto sobrescribirá cualquier salt generado automáticamente.

  Si se omite, un salt aleatorio será generado por la función `password_hash` para cada contraseña hasheada. Este es el propósito de la operación y a partir de PHP 7.0.0 la opción salt ha sido desaconsejada.

- `cost` (`int`) - el costo algorítmico a utilizar. Ejemplos de estos valores pueden encontrarse en la página de documentación de la función `crypt`.

  Si se omite, se utilizará un valor por defecto de `12`. Es una buena base pero podría ser necesario aumentarlo según la arquitectura del hardware.

`PASSWORD_BCRYPT_DEFAULT_COST` (`int`)  

`PASSWORD_ARGON2I` (`string`)  
`PASSWORD_ARGON2I` se utiliza para crear nuevos hashes de contraseña utilizando el algoritmo Argon2i.

Opciones admitidas:

- `memory_cost` (`int`) - Memoria máxima (en kibibytes) que puede ser utilizada para calcular el hash Argon2. Por defecto a `PASSWORD_ARGON2_DEFAULT_MEMORY_COST`.

- `time_cost` (`int`) - Tiempo máximo de duración que puede tomar calcular el hash Argon2. Por defecto a `PASSWORD_ARGON2_DEFAULT_TIME_COST`.

- `threads` (`int`) - Número de hilos a utilizar para calcular el hash Argon2. Por defecto a `PASSWORD_ARGON2_DEFAULT_THREADS`. Solo disponible con libargon2, y no con la implementación libsodium.

Disponible a partir de PHP 7.2.0.

`PASSWORD_ARGON2ID` (`string`)  
`PASSWORD_ARGON2ID` se utiliza para crear nuevos hashes de contraseña utilizando el algoritmo Argon2id. Admite las mismas opciones que [`PASSWORD_ARGON2I`](#constant.password-argon2i).

Disponible a partir de PHP 7.3.0.

`PASSWORD_ARGON2_DEFAULT_MEMORY_COST` (`int`)  
Cantidad de memoria por defecto (en bytes) que será utilizada al intentar calcular un hash.

Disponible a partir de PHP 7.2.0.

`PASSWORD_ARGON2_DEFAULT_TIME_COST` (`int`)  
Tiempo por defecto que se tomará para intentar calcular un hash.

Disponible a partir de PHP 7.2.0.

`PASSWORD_ARGON2_DEFAULT_THREADS` (`int`)  
Número por defecto de hilos que Argon2lib utilizará. No disponible con la implementación libsodium.

Disponible a partir de PHP 7.2.0.

`PASSWORD_ARGON2_PROVIDER` (`string`)  
Disponible a partir de PHP 7.4.0.

`PASSWORD_DEFAULT` (`string`)  
El algoritmo por defecto a utilizar para el hash si no se proporciona ningún algoritmo. Este valor puede cambiar en futuras versiones de PHP donde es probable que se admitan mejores algoritmos de hash.

Es importante tener en cuenta que con el tiempo, esta constante puede cambiar. Por lo tanto, es crucial ser consciente de que la longitud del hash resultante puede variar. Por consiguiente, al utilizar `PASSWORD_DEFAULT`, el hash resultante debe almacenarse de una manera capaz de admitir hashes arbitrarios, la anchura recomendada es de `255` bytes.

Actualmente, es un alias de `PASSWORD_BCRYPT`.

Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Los valores para las constantes `PASSWORD_BCRYPT`, `PASSWORD_ARGON2I`, `PASSWORD_ARGON2ID` y `PASSWORD_DEFAULT` ahora son `string`s. Anteriormente, eran `int`s. |
