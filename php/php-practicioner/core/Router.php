<?php
	class Router {
		public $routes = [
			'GET' => [],
			'POST' => []
		];

		#public function define($routes) {
		#	$this->routes = $routes;
		#}

		public function get($uri, $controller) {
			$this->routes['GET'][$uri] = $controller;
		}

		public function post($uri, $controller) {
			$this->routes['POST'][$uri] = $controller;
		}

		public function direct($uri, $request_type) {
			#When refactor controllers for classes
			# $this->routes[$request_type][$uri] returns PagesController@home
			# we need to split the string using explode and call appropriate function
			#if (array_key_exists($uri, $this->routes[$request_type]))
			#	return $this->routes[$request_type][$uri];
			if (array_key_exists($uri, $this->routes[$request_type]))
				return $this->call_action(
				...explode('@', $this->routes[$request_type][$uri])
				);
			throw new Exception('No route defined for this URI');
		}

		public function call_action($controller, $action) {
			if (!method_exists($controller, $action)) {
				throw new Exception(
					"{$controller} does not respond to {$action} action.");
			}
			return (new $controller)->$action();
		}
	}
?>
