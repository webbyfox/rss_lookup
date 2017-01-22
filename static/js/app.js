var myApp = angular.module('MyApp', []);

myApp.controller("MyController",function($scope, $http)
 {
   $http.get('/api/rss').success(function(response){

   $scope.articles = response.Response.rss.channel.item;

    // Update model
    angular.forEach($scope.articles, function(item) {
        item.pubDate = new Date(item.pubDate);
        item.image = item["media:thumbnail"]["@url"];
        item.id = item.link.split('/').pop();
        item.myClass = "glyphicon glyphicon-star pull-right";
      });

    $scope.orderSelect="pubDate";
    $scope.orderSelect.direction="-1";
    $scope.addToFav = function(obj){
        obj.myClass = "glyphicon glyphicon-heart pull-right";
        var config = {
                headers : {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                    }
                }
        //TODO: validate to avoid duplicate
        $http.post('/api/fav/add/',
                    "url="+encodeURIComponent(obj.link),
                     config
                   ).success(function(response){
                    console.log(response);
                    });

        };

    });
 });

var favApp = angular.module('FavApp', []);
 favApp.controller("FavController",function($scope, $http)
 {
   $http.get('/api/fav/').success(function(response){
   $scope.fav_articles = response.response;
   })
});
