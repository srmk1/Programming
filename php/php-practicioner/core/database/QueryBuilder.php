<?php

#QueryBuilder is a factory method
class QueryBuilder
{
	protected $pdo;

	public function __construct(PDO $pdo) {
		#These objects required by a class are called Collaborators
		$this->pdo = $pdo;
	}

	public function select_all($table) {
		try {
			$statement = $this->pdo->prepare("select * from {$table}");
			$statement->execute();

			#You can fetch a table to an associative array
			#var_dump($statement->fetchAll());
			#var_dump($results[0]->description);

			#You can fetch a table to an general object 
			#var_dump($statement->fetchAll(PDO::FETCH_OBJ));

			#You can fectch a table to an class defined by you
			#$db_tasks = $statement->fetchAll(PDO::FETCH_CLASS,'Task');
			#var_dump($statement->fetchAll(PDO::FETCH_OBJ));
		} catch (PDOException $e) {
			print ($e->getMessage());
		}
		return $statement->fetchAll(PDO::FETCH_CLASS);
	}

	public function insert($table, $item) {
		try {
			// insert into names (name, email) values (:id, :todo, :com)
			$insert_query = sprintf("insert into %s values (%s)",
				$table,
				":id,:desc,:comp");
			#var_dump($insert_query);
			var_dump($item);
			$statement = $this->pdo->prepare($insert_query);
			$statement->execute([
					     ":id" => 9,
				             ":desc" => $item['name'],
					     ":comp" => 0]);
			$this->print_pdo_error($statement);
			$statement = $this->pdo->prepare("select * from {$table}");
			$statement->execute();
			#var_dump($statement->fetchAll(PDO::FETCH_OBJ));
		} catch (PDOException $e) {
			print ($e->getMessage());
		}
	}

	public function print_pdo_error($statement) {
		echo "\nPDOStatement::errorInfo():\n";
		$arr = $statement->errorInfo();
		print_r($arr);
	}
}
?>
