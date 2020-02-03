<?php
#$router->define([
#	'' => 'controllers/index.php',
#	'tutorials' => 'controllers/tutorials_index.php',
#	'about' => 'controllers/about.php',
#	'contact' => 'controllers/contact.php',
#	'names' => 'controllers/add-name.php'
#]);

#$router->get('','controllers/index.php');
#$router->get('tutorials','controllers/tutorials_index.php');
#$router->get('about','controllers/about.php');
#$router->get('contact','controllers/contact.php');
#$router->post('names','controllers/add-name.php');
#var_dump($router->routes);

$router->get('','PagesController@home');
$router->get('about','PagesController@about');
$router->get('contact','PagesController@contact');
$router->post('names','PagesController@addname');
$router->get('tutorials','PagesController@tutorials');
?>
