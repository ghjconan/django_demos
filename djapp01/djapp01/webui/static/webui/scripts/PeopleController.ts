//ProductsController.ts
module People {
    export interface Scope {
        greetingText: string;
    }

    export class Controller {
        constructor($scope: Scope) {
            $scope.greetingText = "Hello from TypeScript + AngularJS";
        }
    }
}