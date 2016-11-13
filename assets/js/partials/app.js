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
    $scope.link = "http://127.0.0.1:8080/api/root/"
    $scope.question = 'С чего начнем?';
    $scope.answers = [];

    fetch();
    function fetch() {
    $http.get($scope.link)
        .success(function(response) {
            response.forEach(function (item, i, arr) {
                if(item.itemtype==="Question"){
                    $scope.question = item.text;
                }
                 $scope.answers.push(item);
            })
            });
}
});

