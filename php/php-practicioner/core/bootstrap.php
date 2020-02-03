<?php
	#require 'core/database/Connection.php';
	#require 'core/database/QueryBuilder.php';
	#require 'core/Router.php';
	require 'vendor/autoload.php';

	#$config = require 'config.php';
	App::bind('config', require 'config.php');
	$config = App::get('config');
	#var_dump(App::get('config'));

	#$refactored_pdo = Connection::make();
	$refactored_pdo = Connection::make($config['database']);
	
	#return new QueryBuilder($refactored_pdo);
	App::bind('database_query', new QueryBuilder($refactored_pdo));
	return App::get('database_query');
?>
