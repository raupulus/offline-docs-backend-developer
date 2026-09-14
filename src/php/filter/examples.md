---
title: Ejemplos
source_url: https://www.php.net/manual/es/filter.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_reviewed: false
translation_revision: 627f933cf
order: 24140
---

## Ejemplos

## Validación

Validando direcciones de email con `filter_var`

```php
<?php
$email_a = 'joe@example.com';
$email_b = 'bogus';

if (filter_var($email_a, FILTER_VALIDATE_EMAIL)) {
    echo "La dirección de email '$email_a' es válida.\n";
}
if (filter_var($email_b, FILTER_VALIDATE_EMAIL)) {
    echo "La dirección de email '$email_b' es válida.\n";
} else {
    echo "La dirección de email no '$email_b' es válida.\n";
}
?>

   
```

El ejemplo anterior mostrará:

    La dirección de email 'joe@example.com' es válida.
    La dirección de email no 'bogus' es válida.

Validando de direcciones IP con `filter_var`

```php
<?php
$ip_a = '127.0.0.1';
$ip_b = '42.42';

if (filter_var($ip_a, FILTER_VALIDATE_IP)) {
    echo "La dirección IP '$ip_a' es válida.";
}
if (filter_var($ip_b, FILTER_VALIDATE_IP)) {
    echo "La dirección IP '$ip_b' es válida.";
}
?>

   
```

El ejemplo anterior mostrará:

    La dirección IP '127.0.0.1' es válida.

Pasando opciones a `filter_var`

```php
<?php
$int_a = '1';
$int_b = '-1';
$int_c = '4';
$options = array(
    'options' => array(
        'min_range' => 0,
        'max_range' => 3,
    )
);
if (filter_var($int_a, FILTER_VALIDATE_INT, $options) !== FALSE) {
    echo "El entero A '$int_a' es válido (entre 0 y 3).\n";
}
if (filter_var($int_b, FILTER_VALIDATE_INT, $options) !== FALSE) {
    echo "El entero B '$int_b' es válido (entre 0 y 3).\n";
}
if (filter_var($int_c, FILTER_VALIDATE_INT, $options) !== FALSE) {
    echo "El entero C '$int_c' es válido (entre 0 y 3).\n";
}

$options['options']['default'] = 1;
if (($int_c = filter_var($int_c, FILTER_VALIDATE_INT, $options)) !== FALSE) {
    echo "El entero C '$int_c' es válido (entre 0 y 3).";
}
?>

   
```

El ejemplo anterior mostrará:

    El entero A '1' es válido (entre 0 y 3).
    El entero C '1' es válido (entre 0 y 3).

## Saneamiento

Saneando y validando direcciones de email

```php
<?php
$a = 'joe@example.org';
$b = 'bogus - at - example dot org';
$c = '(bogus@example.org)';

$sanitized_a = filter_var($a, FILTER_SANITIZE_EMAIL);
if (filter_var($sanitized_a, FILTER_VALIDATE_EMAIL)) {
    echo "Esta dirección de correo saneada (a) es válida.\n";
}

$sanitized_b = filter_var($b, FILTER_SANITIZE_EMAIL);
if (filter_var($sanitized_b, FILTER_VALIDATE_EMAIL)) {
    echo "Esta dirección de correo saneada se considera válida.";
} else {
    echo "Esta dirección de correo saneada (b) no es válida.\n";
}

$sanitized_c = filter_var($c, FILTER_SANITIZE_EMAIL);
if (filter_var($sanitized_c, FILTER_VALIDATE_EMAIL)) {
    echo "Esta dirección de correo saneada (c) es válida.\n";
    echo "Antes: $c\n";
    echo "Después:  $sanitized_c\n";
}
?>

    
```

El ejemplo anterior mostrará:

    Esta dirección de correo saneada (a) es válida.
    Esta dirección de correo saneada (b) no es válida.
    Esta dirección de correo saneada (c) es válida.
    Antes: (bogus@example.org)
    Después: bogus@example.org
