(function () {
    'use static';

    angular
        .module('thinkster.aboutus.controllers')
        .controller('AboutUsController', AboutUsController);

    AboutUsController.$inject = ['$location', '$scope'];

    function AboutUsController($location, $scope, Authentication) {
        var vm = this;

    }
})();
