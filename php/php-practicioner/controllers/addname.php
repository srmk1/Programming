<?php
#var_dump($_SERVER)
#var_dump($_REQUEST)
#var_dump($_GET)
echo 'You typed '.$_POST['name'];
$query->insert('todos',[
	'name' => $_POST['name']]);
?>
