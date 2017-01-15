/**
 * Created by vitold on 10.11.16.
 */
var app = angular.module('pickthebook', []);

app.controller('indexController', function($scope,  $http, $location) {
    $scope.question = 'С чего начнем?';
    $scope.answers = [];

    // Обработка нажатия на любую кнопку
    function transit(id){
        $location.path(id);

        $http.get("http://pickthebook.ru/api/detail/?id="+id)
        .success(function(response) {
            $scope.answers = [];
            $scope.question = response.node.text;
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
            })
        .error(function (reasons) {
             $scope.answers = [];
             $scope.question = "Извините, ничего не найдено:("
        });
    }

    $scope.transit = transit;

    // Обработка кнопок назад и вперед в браузере
    window.onhashchange = function() {
     var location = $location.path();
        if (location == "") {
            $scope.question = 'С чего начнем?';
            $scope.answers = [];
            $scope.author = '';
            $scope.description = '';
            $scope.image = '';
            fetch()
        }
        else  {
            id = location.slice(1);
            $scope.author = '';
            $scope.description = '';
            $scope.image = '';
            transit(id);
            console.log($location);
        }
    };

    // Обработка главной страницы
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

