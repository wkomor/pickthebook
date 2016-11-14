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
    $scope.question = 'С чего начнем?';
    $scope.answers = [];
    $scope.transit = function(id){
        $http.get("http://127.0.0.1:8080/api/detail/?id="+id)
        .success(function(response) {
            $scope.answers = [];
            $scope.question = response.node.text;
            var answers = response.answers;
            if (answers){
                answers.forEach(function (item, i, arr) {
                    $scope.answers.push(item);
                })
            }
            });
    };

    fetch();
    function fetch() {
    $http.get("http://127.0.0.1:8080/api/root/")
        .success(function(response) {
            response.forEach(function (item, i, arr) {
                if(item.itemtype === "Question"){
                    $scope.question = item.text;
                }
                 $scope.answers.push(item);
            })
            });
}
});

