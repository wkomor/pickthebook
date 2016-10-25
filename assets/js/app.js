/**
 * Created by vitold on 25.10.16.
 */
var app = angular.module('pickthebook', []);

app.controller('indexController', function($scope) {
    $scope.firstName= "John";
    $scope.lastName= "Doe";
});