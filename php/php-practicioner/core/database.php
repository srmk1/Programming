<?php

#DATABASES
function connect_to_db() {
	#create an instance of Php Data Object (PDO)
	try {
		return new PDO('mysql:host=127.0.0.1;dbname=mytodo', 'root', '');
	} catch(PDOException $e) {
		print ($e->getMessage());
	}
}

function fetch_all_tasks($pdo) {
	$statement = $pdo->prepare('select * from todos');
	$statement->execute();

	#You can fetch a table to an associative array
	#var_dump($statement->fetchAll());
	#var_dump($results[0]->description);

	#You can fetch a table to an general object 
	#var_dump($statement->fetchAll(PDO::FETCH_OBJ));

	#You can fectch a table to an class defined by you
	#$db_tasks = $statement->fetchAll(PDO::FETCH_CLASS,'Task');
	return $statement->fetchAll(PDO::FETCH_OBJ);
}

?>
