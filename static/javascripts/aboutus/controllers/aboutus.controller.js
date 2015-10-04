(function () {
    'use strict';

    angular
        .module('thinkster.aboutus.controllers')
        .controller('AboutUsController', AboutUsController);

    AboutUsController.$inject = ['$scope', '$http'];

    function AboutUsController($scope, $http) {

        $scope.submit = function() {
            $http.post('/api/v1/contact-us/', angular.toJson($scope.submitter)).then(
                function(){
                    console.log('sent');
                }, function(){
                    console.log('not sent');
                });
        };
    }
})();
