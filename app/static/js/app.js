'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives', 'myApp.controllers']).
  config(['$routeProvider', '$interpolateProvider', function($routeProvider, $interpolateProvider) {
    $routeProvider.when('/view1', {templateUrl: _ngsu + 'partials/partial1.html', controller: 'MyCtrl1'});
    $routeProvider.when('/view2', {templateUrl: _ngsu + 'partials/partial2.html', controller: 'MyCtrl2'});
    $routeProvider.otherwise({redirectTo: '/view1'});
    
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
  }]);
