---
title: Yaf_Dispatcher::setView
description: Establecer un motor de vistas personalizado
source_url: https://www.php.net/manual/es/yaf-dispatcher.setview.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_dispatcher/setview.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: 4a211b7c8
order: 105820
---

Yaf_Dispatcher::setView

Establecer un motor de vistas personalizado

## Descripción

```php
public Yaf_Dispatcher::setView(Yaf_View_Interface $view): Yaf_Dispatcher
```php

Este método ofrece una solución si desea utilizar una vista personalizada personalizado en lugar de `Yaf_View_Simple`.

## Parámetros

`view`  
Una instancia de `Yaf_View_Interface`

## Valores devueltos

## Ejemplos

Ejemplo de un motor de Vistas personalizado

```
<?php
require "/path/to/smarty/Smarty.class.php";

class Smarty_Adapter implements Yaf_View_Interface
{
    /**
     * Smarty object
     * @var Smarty
     */
    public $_smarty;

    /**
     * Constructor
     *
     * @param string $tmplPath
     * @param array $extraParams
     * @return void
     */
    public function __construct($tmplPath = null, $extraParams = array()) {
        $this->_smarty = new Smarty;

        if (null !== $tmplPath) {
            $this->setScriptPath($tmplPath);
        }

        foreach ($extraParams as $clave => $valor) {
            $this->_smarty->$clave = $valor;
        }
    }

    /**
     * Establecer la ruta a las plantillas
     *
     * @param string $ruta El directorio a establecer como ruta.
     * @return void
     */
    public function setScriptPath($ruta)
    {
        if (is_readable($ruta)) {
            $this->_smarty->template_dir = $ruta;
            return;
        }

        throw new Exception('La ruta proporcionada no es válida');
    }

    /**
     * Asignar una variable a la plantilla
     *
     * @param string $clave El nombre de la variable.
     * @param mixed $valor El valor de la variable.
     * @return void
     */
    public function __set($clave, $valor)
    {
        $this->_smarty->assign($clave, $valor);
    }

    /**
     * Permite que funcionen las pruebas con empty() y isset()
     *
     * @param string $clave
     * @return boolean
     */
    public function __isset($clave)
    {
        return (null !== $this->_smarty->get_template_vars($clave));
    }

    /**
     * Permite que funcione unset() con las porpiedades de los objetos
     *
     * @param string $clave
     * @return void
     */
    public function __unset($clave)
    {
        $this->_smarty->clear_assign($clave);
    }

    /**
     * Asignar variables a la plantilla
     *
     * Permite establecer una clave específica para el valor especificado, O pasar
     * un array de parejas clave => valor para establecer masivamente.
     *
     * @see __set()
     * @param string|array $spec La estrategia de asignación a utilizar (clave o
     * array de parejas clave => valor)
     * @param mixed $valor (Opcional) Si se asignan variables nominadas,
     * utilice este como el valor.
     * @return void
     */
    public function assign($spec, $valor = null) {
        if (is_array($spec)) {
            $this->_smarty->assign($spec);
            return;
        }

        $this->_smarty->assign($spec, $valor);
    }

    /**
     * Limpiar todas las variables asignadas
     *
     * Limpia todas las variables asignadas a Yaf_View mediante
     * {@link assign()} o con sobrecarga de propiedades
     * ({@link __get()}/{@link __set()}).
     *
     * @return void
     */
    public function clearVars() {
        $this->_smarty->clear_all_assign();
    }

    /**
     * Procesa una plantilla y devuelve la salida.
     *
     * @param string $nombre La plantilla a procesar.
     * @return string La salida.
     */
    public function render($nombre, $valor = NULL) {
        return $this->_smarty->fetch($nombre);
    }

    public function display($nombre, $valor = NULL) {
        echo $this->_smarty->fetch($nombre);
    }

}
?>

   
```php

Ejemplo de `Yaf_Dispatcher::setView`

```
<?php
class Bootstrap extends Yaf_Bootstrap_Abstract {

    /**
     * existen configuraciones para smarty en la configuración:
     *
     * smarty.left_delimiter   = "{{"
     * smarty.right_delimiter  = "}}"
     * smarty.template_dir     = APPLICATION_PATH "/views/scripts/"
     * smarty.compile_dir      = APPLICATION_PATH "/views/templates_c/"
     * smarty.cache_dir        = APPLICATION_PATH "/views/templates_d/"
     *
     */
    public function _initConfig() {
        $config = Yaf_Application::app()->getConfig();
        Yaf_Registry::set("config", $config);
    }

    public function _initLocalName() {
        /** ponemos la clase Smarty_Adapter bajo el directorio de bibliotecas local */
        Yaf_Loader::getInstance()->registerLocalNamespace('Smarty');
    }

    public function _initSmarty(Yaf_Dispatcher $despachador) {
        $smarty = new Smarty_Adapter(null, Yaf_Registry::get("config")->get("smarty"));
        $despachador->setView($smarty);
        /* ahora el motor de vistas de Smarty se convierte en el motor de vistas predeterminado de Yaf */
    }
}
?>

   
```php

## Véase también

Yaf_View_Interface

Yaf_View_Simple
