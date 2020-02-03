<?php
$query = require 'core/bootstrap.php';
$router = new Router;
require 'routes.php';
#Super Global Arrays
#var_dump($_SERVER['REQUEST_URI']);
#var_dump($_GET);
#var_dump($_POST);
$req_uri_path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$req_uri_method = $_SERVER['REQUEST_METHOD']; 
#require $router->direct(trim($req_uri_path,'/'), $req_uri_method);
$router->direct(trim($req_uri_path,'/'), $req_uri_method);
?>
