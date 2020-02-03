<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title> HTML - PHP </title>
	<style>
		header {
			background: #e3e3e3;
			padding: 2em;
			text-align-last: center;
		}
	</style>
</head>
<body>
	<header>
	<h1>
		Variables
	</h1>
		<?php
			echo "Hello, $name";
			echo "Hello, $name1";
		?>
	<h1>
		Arrays and Associative Arrays	
	</h1>
		<?php
			foreach ($name_array as $name_a) {
				echo "<li>";
				echo $name_a;
				echo "</li>";
			}			
		?>

		<!-- Better to embed html inside foreach php syntax,
			as html gets complicated, doing echo for each tag looks ugly
		-->
	<h1>
	 	Shorthand for php-html integration	
	</h1>
		<?php foreach ($person as $feature_name => $feature_value) : ?>
			<li> <?php echo "$feature_name: $feature_value"; ?> </li>
		<?php endforeach; ?>

	<h1>
		Booleans and Conditional, Unicode characters
	</h1>
		<ul>
		<li> <strong> Task name: </strong> <?php echo $task['description']; ?> </li> 
		<li> <strong> Due Date: </strong> <?php echo $task['due']; ?> </li> 
		<li> <strong> Assigned to: </strong> <? echo $task['assigned_to']; ?> </li> 
		<li> <strong> Completed?: </strong> <?php echo $task['completed'] ? '&#9989' : "No";  ?> </li> 
		</ul>
	<h1>
		CLASSES	
	</h1>
		<?php foreach ($tasks as $t_task) : ?>
		<li> <?php echo "$t_task->description"; ?> </li>
		<?php endforeach; ?>

	<h1>
	 	DATABASES/PDO Objects	
	</h1>
		<?php foreach ($db_tasks as $t_task) : ?>
		<li> <?php echo "$t_task->description"; ?> </li>
		<?php endforeach; ?>

	<h1>
	 	DATABASES/PDO Refactoring: Moving specific functions to different files
		database/connection.php
	</h1>
		<?php foreach ($db_tasks as $t_task) : ?>
		<li> <?php echo "$t_task->description"; ?> </li>
		<?php endforeach; ?>

	<h1>
		Collaborators - Parameters to constructors of classes
		database/QueryBuilder.php
	</h1>
		<?php foreach ($collaborator_tasks as $t_task) : ?>
		<li> <?php echo "$t_task->description"; ?> </li>
		<?php endforeach; ?>

	<h1>
		Bootstrap.php - Moving kind of system_init functions to one file 
	</h1>
		<?php foreach ($bootstrap_tasks as $t_task) : ?>
		<li> <?php echo "$t_task->description"; ?> </li>
		<?php endforeach; ?>

	<h1>
		CONFIG.PHP - Moved all configurable parameters to config.php	
	</h1>
		<li> Define all configurable parameters as a Associative array </li>
		<li> Make config.php return this associative array </li>

	<h1>
		Router - Navigating between different pages in PHP Structure	
	</h1>
		<li> You can create basic php files under root directory ex: about.php and then
			can access it using localhost:8888/about.php </li>
		<li> Linking your URI to filename under root directory might not be scalable
			solution, you might not want to expose your files </li>
		<li> Created all directory structure
			<ul> Views: all views and html files </ul>
			<ul> Core: Contains all database, bootstrap </ul> 
			<ul> Controllers: </ul> </li>
		<li> index.php should only bootstrap and defer everything to
			index.view.php </li>
	<h1>
		Partials - Like template view that is commonly used across all pages	
	</h1>
		<li> Created a partials directory </li>
		<li> Added the common navigation header to partials/nav.php </li>
		<li> Added 'require partials/nav.php' to all views </li>
		<li> Added common head.php and foot.php and added it to all views </li>

	<h1>
		Arrays & Array filtering
	</h1>
		<li> <b> Array filter function: </b> takes array & filtering functions as parameters</li>
				<ul> <?php var_dump($posts); ?> </ul>
				<ul> <?php var_dump($unpublished_posts); ?> </ul>

	<h1>
		Array mapping 
	</h1>
		<li> <b> Array mapper function: </b> takes array & mapper functions as parameters</li>
				<ul> <?php var_dump($map_posts); ?> </ul>

	<h1>
		Array Column 
	</h1>
		<li> <b> Array column function: </b> takes array & key as parameters</li>
				<ul> <?php var_dump($title_column); ?> </ul>

	<h1>
		Forms, Request Types and Routing
	</h1>
		<li> Form: takes methohd(get,post) and action </li>
		<li> PHP built api: parse_url can be used to get specific portion of URIs </li>
		<li> PHP built in api trim: can be used to trim starting and ending chars </li>
		<li> When you GET URI you need to just take URL_PATH, trim leading/ending / and then pass it to controllers </li>
		<li> PHP offers ($_SERVER) global variable which gives various information about server </li>
		<li> PHP offers ($_REQUEST) global variable which gives various parameters in GET query </li>
		<li> PHP offers ($_GET) global variable which gives various parameters in GET query </li>
		<li> GET is suitable for passing some parameters, but not all. For other cases, you might have to POST it in server </li>

	<h1>
	        Dynamic PDO insert	
	</h1>
		<li> Prepare insert query using placeholder strings and execute </li>
		<li> Use var_dump api to dump any variables for ease of debugging </li>
		<li> If there is a error in mysql insert, it did not throw exception. Wrote a error api 
			<a href="http://us2.php.net/manual/en/pdostatement.errorinfo.php"> print_pdo_error </a> to print errors. </li> 

	<h1>
	        <a href="https://getcomposer.org/">Composer Autoloading</a>
	</h1>
		<li> <a href="https://getcomposer.org/download/">Download and install</a> composer</li>
		<li> Created composer.json file for autoloading class files</li>
		<li> Did ./composer.phar install in the root directory, it created autoload classes </li> 
		<li> Once autoloader.php is there, you dont need to do explicitly "require" php files. It will autoload </li>
		<li> However you need to do "require vendor/autoload.php' atleast once may be in bootstrap.php </li> 

	<h1>
		Dependency Injection Container
	</h1>
		<li> Container is like throwing something to a box with label on it,
			then query it using the label to get it back </li>
		<li> Move the config of the application to DI container instead of using array </li>
		<li> You could just throw all config, databases, queries and then query it back from DI </li>
		<li> Everytime you write a class you need to do './composer.phar dump-autoload' for it to autoload </li>

	<h1>
		Refactoring to Controller Classes	
	</h1>
		<li> Controller is responsible: Receiving a request, Delgating it to some form & sending response to request <li>
		<li> implode and exploed inbuilt functions are very useful to modify strings</li>
</header>
<body>
</html>
