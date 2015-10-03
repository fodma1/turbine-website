(function () {
  'use strict';

  angular
    .module('thinkster.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
   * @name config
   * @desc Define valid application routes
   */
  function config($routeProvider) {
    $routeProvider.when('/', {
      controller: 'LandingController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/landing/landing.html'
    }).when('/solutions', {
      templateUrl: '/static/templates/solutions/solutions.html',
      title: 'Turbine | Solutions'
    }).when('/about-us', {
      controller: 'AboutUsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/aboutus/aboutus.html',
      title: 'Turbine | About Us'
    }).when('/register', {
      controller: 'RegisterController', 
      controllerAs: 'vm',
      templateUrl: '/static/templates/authentication/register.html'
    }).when('/login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/authentication/login.html'
    }).when('/user/:username', {
      controller: 'AccountController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/accounts/account.html'
    }).when('/user/:username/settings', {
      controller: 'AccountSettingsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/accounts/settings.html'
    }).otherwise('/');
  }
})();
