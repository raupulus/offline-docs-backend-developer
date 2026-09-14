---
title: Datos Enviados por el Usuario
source_url: https://www.php.net/manual/es/security.variables.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/variables.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: f0ed705e1
order: 109990
---

## Datos Enviados por el Usuario

Las mayores debilidades de muchos programas PHP no son inherentes al lenguaje mismo, sino simplemente un problema generado cuando se escribe código sin pensar en la seguridad. Por esta razón, usted debería tomarse siempre el tiempo para considerar las implicaciones de cada pedazo de código, para averiguar el posible peligro involucrado cuando una variable inesperada es enviada.

Uso Peligroso de Variables

```php
<?php
// eliminar un archivo del directorio personal del usuario .. ¿o
// quizás de alguien más?

unlink ($evil_var);

// Imprimir el registro del acceso... ¿o quizás una entrada de /etc/passwd?
fwrite ($fp, $evil_var);

// Ejecutar algo trivial.. ¿o rm -rf *?
system ($evil_var);
exec ($evil_var);

?>

   
```

Usted debería examinar siempre, y cuidadosamente su código para asegurarse de que cualquier variable siendo enviada desde un navegador web sea chequeada apropiadamente, y preguntarse a sí mismo:

- ¿Este script afectará únicamente los archivos que se pretende?

- ¿Puede tomarse acción sobre datos inusuales o indeseados?

- ¿Puede ser usado este script en formas malintencionadas?

- ¿Puede ser usado en conjunto con otros scripts en forma negativa?

- ¿Serán adecuadamente registradas las transacciones?

Al preguntarse adecuadamente estas preguntas mientras escribe su script, en lugar de hacerlo posteriormente, usted previene una desafortunada re-implementación del programa cuando desee incrementar el nivel de seguridad. Al comenzar con esta mentalidad, no garantizará la seguridad de su sistema, pero puede ayudar a mejorarla.

Mejore la seguridad deshabilitando las configuraciones de conveniencia que oscurecen el origen, la validez o la integridad de los datos de entrada. La creación implícita de variables y la entrada no verificada pueden llevar a vulnerabilidades como ataques de inyección y manipulación de datos.

Características como `register_globals` y `magic_quotes` (ambas eliminadas en PHP 5.4.0) contribuyeron a estos riesgos al crear automáticamente variables a partir de la entrada del usuario y escapar datos de manera inconsistente. Aunque ya no están en PHP, riesgos similares persisten si la gestión de la entrada es incorrecta.

Habilite [error_reporting(E_ALL)](#function.error-reporting) para ayudar a detectar variables no inicializadas y validar la entrada. Utilice tipos estrictos ([declare(strict_types=1)](#language.types.declarations.strict), introducido en PHP 7) para imponer la seguridad de tipos, prevenir conversiones de tipos no intencionadas y mejorar la seguridad general.
