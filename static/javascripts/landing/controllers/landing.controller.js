(function () {
    'use static';

    angular
        .module('thinkster.landing.controllers')
        .controller('LandingController', LandingController);

    LandingController.$inject = ['$location', '$scope'];

    function LandingController($location, $scope, Authentication) {
        var vm = this;

    }
})();
