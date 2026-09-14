---
title: password_hash
description: Crea una clave de hash para una contraseña
source_url: https://www.php.net/manual/es/function.password-hash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/password/functions/password-hash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: password
translation_status: ready
translation_reviewed: false
translation_revision: 5003a6ea9
order: 61110
---

password_hash

Crea una clave de hash para una contraseña

## Descripción

```php
#[\SensitiveParameter] password_hash(string $password, string $algo, [array $options]): string
```php

La función `password_hash` crea un nuevo hash utilizando un algoritmo de hash fuerte e irreversible.

Los siguientes algoritmos son actualmente soportados:

- `PASSWORD_DEFAULT` - Uso del algoritmo bcrypt (por omisión desde PHP 5.5.0). Tenga en cuenta que esta constante está diseñada para cambiar con el tiempo, a medida que se añaden algoritmos más recientes y fuertes a PHP. Por esta razón, la longitud del resultado de este algoritmo puede cambiar con el tiempo, por lo que se recomienda almacenar el resultado en una columna de la base de datos que pueda contener al menos 60 caracteres (255 bytes puede ser una muy buena opción).

- `PASSWORD_BCRYPT` - Uso del algoritmo bcrypt para crear la clave de hash. Esto creará una clave de hash estándar `crypt` utilizando el identificador `$2y$`.

- `PASSWORD_ARGON2I` - Utiliza el algoritmo de hash Argon2i para crear el hash. Este algoritmo solo está disponible si PHP ha sido compilado con el soporte de Argon2

- `PASSWORD_ARGON2ID` - Utiliza el algoritmo de hash Argon2id para crear el hash. Este algoritmo solo está disponible si PHP ha sido compilado con el soporte de Argon2

Opciones soportadas para `PASSWORD_BCRYPT`:

- `salt` (`string`) - para proporcionar manualmente un salt a utilizar durante el hash de la contraseña. Tenga en cuenta que esta opción evitará la generación automática.

  Si se omite, un salt aleatorio será generado por la función `password_hash` para cada contraseña hash. Este es el modo de funcionamiento previsto.

  > [!WARNING]
  > La opción Salt está obsoleta. Es preferible utilizar simplemente el salt que se genera por omisión. A partir de PHP 8.0.0, un salt proporcionado explícitamente es ignorado.

- `cost` (`int`) - determina el costo algorítmico que debe ser utilizado. Ejemplos de estos valores pueden ser encontrados en la página de documentación de la función `crypt`.

  Si se omite, el valor por omisión `12` será utilizado. Este es un buen compromiso, pero debe ser ajustado según el hardware utilizado.

Opciones soportadas para `PASSWORD_ARGON2I` y `PASSWORD_ARGON2ID`:

- `memory_cost` (`int`) - Memoria máxima (en kilobytes binarios) que puede ser utilizada para calcular el hash Argon2. Por omisión a `PASSWORD_ARGON2_DEFAULT_MEMORY_COST`.

- `time_cost` (`int`) - Duración máxima de tiempo que puede tomar para calcular el hash Argon2. Por omisión a `PASSWORD_ARGON2_DEFAULT_TIME_COST`.

- `threads` (`int`) - Número de hilos a utilizar para calcular el hash Argon2. Por omisión a `PASSWORD_ARGON2_DEFAULT_THREADS`.

  > [!WARNING]
  > Solo disponible cuando PHP utiliza libargon2, y no la implementación libsodium.

## Parámetros

`password`  
La contraseña del usuario.

> [!CAUTION]
> El uso de la constante `PASSWORD_BCRYPT` para el algoritmo hará que el parámetro `password` sea truncado a una longitud máxima de 72 bytes.

`algo`  
Una [constante del algoritmo de contraseña](#password.constants) que representa el algoritmo a utilizar durante el hasheo de la contraseña.

`options`  
Un array asociativo que contiene las opciones. Ver también [las constantes del algoritmo de contraseña](#password.constants) para la documentación sobre las opciones soportadas para cada algoritmo.

## Valores devueltos

Retorna la contraseña hash.

El algoritmo utilizado, el costo y el salt están contenidos en el hash retornado. También, toda la información útil para verificar este último está incluida. Esto permite que la función `password_verify` verifique el hash sin necesidad de almacenar por separado esta información.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El valor por omisión de la opción `cost` del algoritmo `PASSWORD_BCRYPT` ha sido aumentado de `10` a `12`. |
| 8.3.0 | `password_hash` ahora asocia la excepción Random\RandomException subyacente a Exception::\$previous cuando una ValueError es lanzada debido a un fallo en la generación del salt. |
| 8.0.0 | `password_hash` ya no retorna `false` en caso de fallo, una `ValueError` será lanzada si el algoritmo de hash de contraseña no es válido, o una `Error` si el hash de contraseña falló por una razón desconocida. |
| 8.0.0 | `algo` ahora es nullable. |
| 7.4.0 | El parámetro `algo` ahora espera una `string`, pero sigue aceptando un `int` para mantener la compatibilidad hacia atrás. |
| 7.4.0 | La extensión sodium proporciona una implementación alternativa para las contraseñas Argon2. |
| 7.3.0 | Añadido el soporte para contraseñas Argon2id utilizando `PASSWORD_ARGON2ID`. |
| 7.2.0 | Añadido el soporte para contraseñas Argon2i utilizando `PASSWORD_ARGON2I`. |

## Ejemplos

Ejemplo con `password_hash`

```
<?php
echo password_hash("rasmuslerdorf", PASSWORD_DEFAULT);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    $2y$12$4Umg0rCJwMswRw/l.SwHvuQV01coP0eWmGzd61QH2RvAOMANUBGC.

Ejemplo con `password_hash` definiendo manualmente la opción cost

```
<?php
$options = [
     // Aumenta el costo de bcrypt de 12 a 13.
    'cost' => 13,
];
echo password_hash("rasmuslerdorf", PASSWORD_BCRYPT, $options);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    $2y$13$xeDfQumlmdm0Sco.4qmH1OGfUUmOcuRmfae0dPJhjX1Bq0yYhqbNi

Ejemplo con `password_hash` para encontrar un buen costo (cost)

Este código realizará un benchmark de la máquina para determinar el costo máximo que puede ser utilizado sin degradar la experiencia del usuario. Se recomienda elegir el costo más alto posible sin ralentizar otras operaciones que la máquina debe ejecutar. 11 es una buena base, y un valor más alto es preferible si la máquina es suficientemente rápida. El código de abajo apunta a un tiempo de estiramiento ≤ 350 milisegundos, lo cual representa un retraso adecuado para sistemas que manejan conexiones interactivas.

```
<?php
$timeTarget = 0.350; // 350 milisegundos

$cost = 11;
do {
    $cost++;
    $start = microtime(true);
    password_hash("test", PASSWORD_BCRYPT, ["cost" => $cost]);
    $end = microtime(true);
} while (($end - $start) < $timeTarget);

echo "Valor de 'cost' más apropiado: " . $cost - 1;
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Valor de 'cost' más apropiado: 13

Ejemplo con `password_hash` y Argon2i

```
<?php
echo 'Argon2i hash: ' . password_hash('rasmuslerdorf', PASSWORD_ARGON2I);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Argon2i hash: $argon2i$v=19$m=1024,t=2,p=2$YzJBSzV4TUhkMzc3d3laeg$zqU/1IN0/AogfP4cmSJI1vc8lpXRW9/S0sYY2i2jHT0

## Notas

> [!CAUTION]
> Se recomienda encarecidamente no proporcionar un salt explícito para esta función. Un salt seguro será generado automáticamente si no se especifica ningún salt.
>
> Como se mencionó anteriormente, el uso de la opción `salt` a partir de PHP 7.0.0 generará una advertencia de deprecación. El soporte para un salt explícito fue eliminado a partir de PHP 8.0.0.

> [!NOTE]
> Se recomienda probar esta función en la máquina utilizada y ajustar el/los parámetro(s) de costo para que la ejecución de la función tome menos de 350 milisegundos para conexiones interactivas. El script del ejemplo anterior ayudará a elegir un costo bcrypt adecuado para la máquina dada.

> [!NOTE]
> La actualización de los algoritmos soportados por esta función (o el cambio al por omisión) debe seguir las siguientes reglas:
>
> - Cada nuevo algoritmo debe formar parte del núcleo de PHP durante al menos 1 versión completa antes de aspirar a convertirse en el algoritmo por omisión. También, si, por ejemplo, un nuevo algoritmo es añadido en la versión 7.5.5, no será elegible como algoritmo por omisión hasta PHP 7.7 (sabiendo que 7.6 será la primera versión completa). Pero si un algoritmo diferente ha sido añadido en 7.6.0, también será elegible como algoritmo por omisión a partir de la versión 7.7.0.
>
> - El algoritmo por omisión solo puede ser cambiado durante una versión completa (7.3.0, 8.0.0, etc...) y no durante una versión de revisión. La única excepción a este principio básico sería una emergencia, por ejemplo, al descubrir un bug crítico de seguridad en el algoritmo por omisión.

## Véase también

`password_verify`, `password_needs_rehash`, `crypt`, `sodium_crypto_pwhash_str`
