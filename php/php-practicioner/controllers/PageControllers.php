<?php

	class PagesController {
		
		public function home() {
			#$bootstrap_tasks = $query->select_all('todos');
			$bootstrap_tasks = App::get('database_query'); 	

			#CONFIG.PHP all configurable parameters can be done here
			#All the files you would need a require, something line #include
			#All util functions you write 
			require 'views/index1.view.php';
		}

		public function about() {
			require 'views/about.view.php';
		}

		public function contact() {
			require 'views/contact.view.php';
		}

		public function tutorials() {
			require 'views/index.view.php';
		}

		public function addname() {
			#require 'controllers/addname.php';
			$query = App::get('database_query');
			$query->insert('todos',[
				'name' => $_POST['name']]);
		}
	}
