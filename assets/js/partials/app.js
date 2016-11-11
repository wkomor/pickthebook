/**
 * Created by vitold on 10.11.16.
 */
var app = angular.module('pickthebook', []);

app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
    }
]);

app.controller('indexController', function($scope,  $http) {
    $scope.details = [];
    fetch();
    function fetch() {
    $http.get("http://127.0.0.1:8080/api/items/")
        .success(function(response) {
            $scope.details = response[0].title; });
}
});

