<?php

class Connection {
	public static function make($config) {
		#create an instance of Php Data Object (PDO)
		try {
			#return new PDO('mysql:host=127.0.0.1;dbname=mytodo', 'root', '');
			return new PDO(
				$config['connection'].';dbname='.$config['name'],
				$config['username'],
				$config['password']);
		} catch(PDOException $e) {
			print ($e->getMessage());
		}
	}
}
