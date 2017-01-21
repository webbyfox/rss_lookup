var myApp = angular.module('MyApp', []);

myApp.controller("MyController",function($scope, $http)
 {
   $http.get('/api/rss').success(function(response){

   $scope.articles = response.Response.rss.channel.item;

    // updating model
    angular.forEach($scope.articles, function(item) {
        item.pubDate = new Date(item.pubDate);
        item.image = item["media:thumbnail"]["@url"];
      });

    $scope.orderSelect="pubDate";
    $scope.orderSelect.direction="-1";
    });
 });