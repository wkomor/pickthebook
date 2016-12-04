/**
 * Created by vitold on 10.11.16.
 */
var app = angular.module('pickthebook', []);


app.controller('indexController', function($scope,  $http, $location) {
    $scope.question = 'С чего начнем?';
    $scope.answers = [];
    $scope.transit = function(id){
        $http.get("http://pickthebook.ru/api/detail/?id="+id)
        .success(function(response) {
            $scope.answers = [];
            $scope.question = response.node.text;
            $location.hash(id);
            var answers = response.answers;
            var book = response.book;
            if (answers){
                answers.forEach(function (item, i, arr) {
                    $scope.answers.push(item);
                })
            }
            if (book){
                $scope.question = book.title;
                $scope.author = book.author;
                $scope.description = book.description;
                $scope.image = book.image;
            }
            }).error(function (reasons) {
             $scope.answers = [];
             $scope.question = "Извините, ничего не найдено:("
        });
    };

    fetch();
    function fetch() {
    $http.get("http://pickthebook.ru/api/root/")
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

