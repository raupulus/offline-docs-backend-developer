---
title: Ejemplos
source_url: https://www.php.net/manual/es/ldap.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: 39899ee59
order: 42950
---

## Ejemplos

## Uso básico

Lee las informaciones sobre todas las entradas cuyo nombre comienza por "S" en el servidor de directorio, luego muestra el nombre y la dirección de correo electrónico.

Búsqueda con LDAP

```php
<?php
// La secuencia de base con LDAP es
// conexión, enlace, búsqueda, interpretación del resultado
// desconexión

echo '<h3>consulta de prueba de LDAP</h3>';
echo 'Conectando ...';
$ds=ldap_connect("localhost");  // debe ser un servidor LDAP válido !
echo 'El resultado de conexión es ' . $ds . '<br />';

if ($ds) {
    echo 'Enlazando ...';
    $r=ldap_bind($ds);     // conexión anónima, típica
                                     // para un acceso de solo lectura.
    echo 'El resultado de conexión es ' . $r . '<br />';

    echo 'Buscando (sn=S*) ...';
    // Búsqueda por apellido
    $sr=ldap_search($ds, "o=My Company, c=US", "sn=S*");
    echo 'El resultado de la búsqueda es ' . $sr . '<br />';

    echo 'El número de entradas devueltas es ' . ldap_count_entries($ds,$sr)
         . '<br />';

    echo 'Lectura de las entradas ...<br />';
    $info = ldap_get_entries($ds, $sr);
    echo 'Datos para ' . $info["count"] . ' entradas:<br />';

    for ($i=0; $i<$info["count"]; $i++) {
        echo 'dn es : ' . $info[$i]["dn"] . '<br />';
        echo 'primera entrada cn : ' . $info[$i]["cn"][0] . '<br />';
        echo 'primer correo electrónico : ' . $info[$i]["mail"][0] . '<br />';
    }

    echo 'Cierre de la conexión';
    ldap_close($ds);

} else {
    echo '<h4>No es posible conectarse al servidor LDAP.</h4>';
}
?>

   
```

## Controles LDAP

A continuación se muestran algunos ejemplos de uso de los controles LDAP con PHP \>= 7.3.0.

Enlazar con información de política

```php
<?php

$user   = 'cn=admin,dc=example,dc=com';
$passwd = 'adminpassword';

$ds = ldap_connect('ldap://localhost');

if ($ds) {
    $r = ldap_bind_ext($ds, $user, $passwd, [['oid' => LDAP_CONTROL_PASSWORDPOLICYREQUEST]]);

    if (ldap_parse_result($ds, $r, $errcode, $matcheddn, $errmsg, $referrals, $ctrls)) {
        if ($errcode != 0) {
            die("Error: $errmsg ($errcode)");
        }
        if (isset($ctrls[LDAP_CONTROL_PASSWORDPOLICYRESPONSE])) {
            $value = $ctrls[LDAP_CONTROL_PASSWORDPOLICYRESPONSE]['value'];
            echo "Expira en : ".$value['expire']." segundos\n";
            echo "Número de autentificaciones restantes : ".$value['grace']."\n";
            if (isset($value['error'])) {
                echo "Código de error de política : ".$value['error'];
            }
        }
    }
} else {
    die("No es posible conectarse al servidor LDAP");
}
?>

   
```

Modificar la descripción solo si no está vacía

```php
<?php
// $link es una conexión LDAP

$result = ldap_mod_replace_ext(
    $link,
    'o=test,dc=example,dc=com',
    ['description' => 'Nueva descripción'],
    [
        [
            'oid'         => LDAP_CONTROL_ASSERT,
            'iscritical'  => TRUE,
            'value'       => ['filter' => '(!(description=*))']
        ]
    ]
);

// Luego utilizar ldap_parse_result
?>

   
```

Leer valores antes de su eliminación

```php
<?php
// $link es una conexión LDAP

$result = ldap_delete_ext(
    $link,
    'o=test,dc=example,dc=com',
    [
        [
            'oid'         => LDAP_CONTROL_PRE_READ,
            'iscritical'  => TRUE,
            'value'       => ['attrs' => ['o', 'description']]
        ]
    ]
);

// Luego utilizar ldap_parse_result
?>

   
```

Eliminar una referencia

```php
<?php
// $link es una conexión LDAP

// Sin el control esto eliminaría el nodo referenciado
// Asegúrese de definir el control como crítico para evitar esto
$result = ldap_delete_ext(
    $link,
    'cn=reference,dc=example,dc=com',
    [['oid' => LDAP_CONTROL_MANAGEDSAIT, 'iscritical' => TRUE]]
);

// Luego utilizar ldap_parse_result
?>

   
```

Utilizar paginación para una búsqueda

```php
<?php
// $link es una conexión LDAP

$cookie = '';

do {
    $result = ldap_search(
        $link, 'dc=example,dc=base', '(cn=*)', ['cn'], 0, 0, 0, LDAP_DEREF_NEVER,
        [['oid' => LDAP_CONTROL_PAGEDRESULTS, 'value' => ['size' => 2, 'cookie' => $cookie]]]
    );
    ldap_parse_result($link, $result, $errcode , $matcheddn , $errmsg , $referrals, $controls);
    // Para mantener el ejemplo simple los errores no son verificados
    $entries = ldap_get_entries($link, $result);
    foreach ($entries as $entry) {
        echo "cn: ".$entry['cn'][0]."\n";
    }
    if (isset($controls[LDAP_CONTROL_PAGEDRESULTS]['value']['cookie'])) {
        // Debe pasar el cookie del último llamado al próximo
        $cookie = $controls[LDAP_CONTROL_PAGEDRESULTS]['value']['cookie'];
    } else {
        $cookie = '';
    }
    // Cookie vacía significa última página
} while (strlen($cookie) > 0);
?>

   
```
