//ProductsController.ts
var People;
(function (People) {
    var Controller = (function () {
        function Controller($scope) {
            $scope.greetingText = "Hello from TypeScript + AngularJS";
        }
        return Controller;
    })();
    People.Controller = Controller;
})(People || (People = {}));
