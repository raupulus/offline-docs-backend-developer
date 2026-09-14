---
title: Ejemplos
source_url: https://www.php.net/manual/es/gnupg.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_revision: a148eb08b
order: 28940
---

## Ejemplos

## Firma de texto (clearsign)

Ejemplo que firma un texto dado.

Ejemplo de firma (clearsign) gnupg mediante funciones

```php
<?php
// Inicializamos gnupg
$res = gnupg_init();
// Esto realmente no es necesario, clearsign es el valor por defecto
gnupg_setsignmode($res,GNUPG_SIG_MODE_CLEAR);
// Añade clave con la contraseña 'test' para firmar
gnupg_addsignkey($res,"8660281B6051D071D94B5B230549F9DC851566DC","test");
// Firma
$signed = gnupg_sign($res,"just a test");
echo $signed;
?>

   
```

Ejemplo de firma gnupg (clearsign) mediante orientación a objetos

```php
<?php
// Instanciamos la clase
$gnupg = new gnupg();
// Esto realmente no es necesario, clearsign es el valor por defecto
$gnupg->setsignmode(gnupg::SIG_MODE_CLEAR);
// Añade clave con la contraseña 'test' para firmar
$gnupg->addsignkey("8660281B6051D071D94B5B230549F9DC851566DC","test");
// Firma
$signed = $gnupg->sign("just a test");
echo $signed;
?>

   
```

keylistiterator

Esta extensión trae también un Iterator para un juego de claves

```php
<?php
// Crea un nuevo Iterator para listar todas las claves públicas que coinciden
// con 'example'
$iterator = new gnupg_keylistiterator("example");
foreach($iterator as $fingerprint => $userid){
    echo $fingerprint." -> ".$userid."\n";
}
?>

   
```
