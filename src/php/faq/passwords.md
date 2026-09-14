---
title: Hash de contraseñas seguro
source_url: https://www.php.net/manual/es/faq.passwords.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/passwords.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_reviewed: false
translation_revision: f012b2761
order: 1510
---

## Hash de contraseñas seguro

Esta sección explica las razones que justifican el uso de funciones hash para proteger las contraseñas. También se explica cómo hacerlo de un modo efectivo.

**Q:** ¿Por qué debo usar hash en las contraseñas de los usuarios de mi aplicación?

**A:** El hash de contraseñas es una de las consideraciones de seguridad más elementales que se deben llevar a la práctica al diseñar una aplicación que acepte contraseñas de los usuarios. Sin hashing, cualquier contraseña que se almacene en la base de datos de la aplicación podrá ser robada si la base de datos se ve comprometida, con lo que inmediatamente no sólo estaría comprometida la aplicación, sino también las cuentas de otros servicios de nuestros usuarios, siempre y cuando no utilicen contraseñas distintas.

Si aplicamos un algoritmo hash a las contraseñas antes de almacenarlas en la base de datos, dificultamos al atacante el determinar la contraseña original, pese a que en un futuro podrá comparar el hash resultante con la contraseña original.

Sin embargo, es importante tener en cuenta que el hecho de aplicar hash a las contraseñas sólo protege de que se vean comprometidas las contraseñas almacenadas, pero no las protege necesariamente de ser interceptadas por un código malicioso inyectado en la propia aplicación.

**Q:** ¿Por qué las funciones hash más comunes como `md5` y `sha1` no son adecuadas para las contraseñas?

**A:** Los algoritmos hash como MD5, SHA1 o SHA256 están diseñados para ser muy rápidos y eficientes. Con las técnicas y equipos modernos, es algo trivial “extraer por fuerza bruta” la salida de estos algoritmos, para determinar los datos de entrada originales.

Dada la velocidad con que los ordenadores actuales pueden “invertir” estos algoritmos hash, muchos profesionales de la seguridad recomiendan encarecidamente no utilizarlas como funciones hash para contraseñas.

**Q:** ¿Qué hash debo aplicar a mis contraseñas, si las funciones hash más comunes no son adecuadas?

**A:** Al aplicar un algoritmo hash, los dos factores más importantes son el coste computacional y la sal. Cuanto más cueste aplicar un algoritmo hash, más costará analizar su salida por fuerza bruta.

PHP proporciona una [API de hash de contraseñas nativa](#book.password) que maneja cuidadosamente [el empleo de hash](#function.password-hash) y la [verificación de contraseñas](#function.password-verify) de una manera segura.

El algoritmo recomendado para el empleo de contraseñas con hash es Blowfish, que es también el predeterminado de la API de hash de contraseñas, que, aunque es significativamente más caro computacionalmente que MD5 o SHA1, sigue siendo escalable.

La función `crypt` también está disponible para el hash de contraseñas, pero solo se recomienda para la interoperabilidad con otros sistemas. En su lugar, se recomienda encarecidamente el uso de la [API de hash de contraseñas nativa](#book.password) siempre que sea posible.

**Q:** ¿Qué es una sal (salt)?

**A:** Una sal criptográfica es un dato que se utiliza durante el proceso de hash para eliminar la posibilidad de que el resultado pueda buscarse a partir de una lista de pares precalculados de hash y sus entradas originales, conocidas como tablas rainbow.

Es decir, una sal es un pequeño dato añadido que hace que los hash sean significantemente más difíciles de crackear. Existe un gran número de servicios online que ofrecen grandes listas de códigos hash precalculados, junto con sus datos de entrada originales. El uso de una sal hace muy difícil o imposible encontrar el hash resultante en cualquiera de estas listas.

`password_hash` creará una sal aleatoria si no se proporciona una, siendo esta generalmente la estrategia más sencilla y segura.

**Q:** ¿Cómo almaceno mis sales?

**A:** Al utilizar `password_hash` o `crypt`, el valor devuelto incluye la sal como parte del hash generado. Este valor debería almacenarse tal cual en la base de datos, ya que incluye información sobre la función hash que se empleó y así proporcionarla directamente a `password_verify` al verificar contraseñas.

> [!WARNING]
> Siempre debería utilizarse `password_verify` en lugar de volver a aplicar hash y comparar el resultado con un hash almacenado, a fin de evitar ataques de temporización.

El siguiente diagrama muestra el formato de un valor devuelto por `crypt` o `password_hash`. Como se puede observar, son autocontenidos, con toda la información del algoritmo y la sal requerida para futuras verificaciones de contraseñas.

<img src="en/faq/figures/crypt-text-rendered.svg" width="690" height="192" alt="Los componentes del valor devuelto por password_hash y crypt: en orden, el algoritmo elegido, las opciones del algoritmo, la sal utilizada, y la contraseña con hash." />
