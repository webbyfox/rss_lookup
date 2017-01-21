var myApp = angular.module('MyApp', []);

myApp.controller("MyController",function($scope, $http)
 {
   $http.get('/api/rss').success(function(response){

   $scope.articles = response.Response.rss.channel.item;

    angular.forEach($scope.articles, function(item) {

        item.pubDate = new Date(item.pubDate);
        //console.log(item);
        item.image = item["media:thumbnail"]["@url"];

      });
   $scope.orderSelect="pubDate";
    });
 });

