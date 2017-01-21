var myApp = angular.module('MyApp', []);

myApp.controller("MyController",function($scope, $http)
 {
   $http.get('/api/rss').success(function(response){

   $scope.articles = response.Response.rss.channel.item;
   $scope.orderPub='pubDate';
    });
 });

