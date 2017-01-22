var myApp = angular.module('MyApp', []);

myApp.controller("MyController",function($scope, $http)
 {
   $http.get('/api/rss').success(function(response){

   $scope.articles = response.Response.rss.channel.item;

    // updating model
    angular.forEach($scope.articles, function(item) {
        item.pubDate = new Date(item.pubDate);
        item.image = item["media:thumbnail"]["@url"];
        item.id = item.link.split('/').pop();
        item.myClass = "glyphicon glyphicon-star pull-right";
      });

    $scope.orderSelect="pubDate";
    $scope.orderSelect.direction="-1";
    //$scope.myClass = "glyphicon glyphicon-star pull-right";
    $scope.addToFav = function(obj){
        obj.myClass = "glyphicon glyphicon-heart pull-right";
//        var myEle = angular.element( document.querySelector( '#in-pictures-38612080' ) );
//         console.log(myEle);
//
//          myEle.myClass = "glyphicon glyphicon-heart pull-right";
//         console.log(obj.link);
         var config = {
                headers : {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                    }
                }
        $http.post('/api/fav/add/',
                    "url="+encodeURIComponent(obj.link),
                     config
                   ).success(function(response){
                    console.log(response);
                    });

        };

    });
 });