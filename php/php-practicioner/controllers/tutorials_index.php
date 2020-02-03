<?php

//Variable Syntax
$name = htmlspecialchars($_GET['name']); 
$name1 = $_GET['name'];

//Array syntax
$name_array = [
	'Ashwini',
	'Aditi',
	'Arjun',
	'Manjula',
	'Kirshna Murthy',
	'Ananth'
];

//Appending to array
$name_array[] = 'Deepa';

//Associative array
$person = [
	'name' => 'Srikanth',
	'age' => '36',
	'profession' => 'Software Engineer'
];

//Appending to associative array
$person['Company'] = 'Cisco';

//Booleans and conditionals
$task = [
	'title' => 'CLI ddts',
	'due' => 'today',
	'assigned_to' => 'srmk',
	'completed' => true 
];

//Functions and builtin functions
//	Bulitin - var_dump dumps the variable
//	pre-tag - properly organizes the variables
//	Builtin die - it dies at that point, does not continue to load index_view
//	dd - dump and die, commonly named function in php 

function dd($data) {
	echo '<pre>';
	die(var_dump($data));
	echo '</pre>';
}

$animals = [
	'dog',
	'cat',
	'cow'
];
#dd($animals);

#CLASSES
class Task {
	public $description;
	public $is_complete;

	public function __construct($description) {
		$this->description = $description;
	}

	public function is_completed() {
		return $this->is_complete;
	}
}

$task1 = new Task("test task");
#dd($tasks);

$tasks = [
	new Task("test task"),
	new Task("test task1"),
	new Task("test task2")
];
#dd($tasks);

#PDO 
require 'core/database.php';
$pdo = connect_to_db();
$db_tasks = fetch_all_tasks($pdo);

#PDO Refractoring and Collaborators - Episode 14
#Building these little classes to handle connection, query.. is called
#refactorint the code.
#Constructor parameters are also called as collaborators.
#Building connections and query builder can be also moved to
#bootstrap.php 
#require 'core/database/Connection.php';
$config_1 = require 'config.php';
$refactored_pdo = Connection::make($config_1['database']);
#$refactored_pdo = Connection::make();
$refactored_db_tasks = fetch_all_tasks($refactored_pdo);

#require 'core/database/QueryBuilder.php';
$query = new QueryBuilder($refactored_pdo);
$collaborator_tasks = $query->select_all('todos');

#You can move all init functions to bootstrap.php
#You can also make bootstrap return a query builder
#$query = require 'core/bootstrap.php';
$bootstrap_tasks = $query->select_all('todos');

#Array Filtering: Episode-18
class Post {
	public $title;
	public $published;
	
	public function __construct($title, $published) {
		$this->title = $title;
		$this->published = $published;
	}
};

$posts = [
	new Post('My first post', true),
	new Post('My Second post', true),
	new Post('My third post', true),
	new Post('My fourth post', false),
];		

$unpublished_posts = array_filter($posts, function ($post) {
#	if ($post->published == false)
#		return $post;
#Above 2 lines can be writte in short hand form
	return !$post->published;
});

$published_posts = array_filter($posts, function ($post) {
#	if ($post->published == true)
#		return $post;
#Above 2 lines can be writte in short hand form
	return $post->published;
});

#Array mapper functions
$map_posts = array_map(function ($post) {
	#Anything you do here, will be done for each post in $posts
	#you could transform $posts to array of posts instead of object post
	#return (array) $post;
	#Retain only one element of object
	#return ['title' => $post->title];
	$post->published = true;
	return $post;
}, $posts);

#Array column 
$title_column = array_column($posts, 'title');
#CONFIG.PHP all configurable parameters can be done here
#All the files you would need a require, something line #include
#All util functions you write 
require 'views/index.view.php';
?>
