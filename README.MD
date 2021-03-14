# ToDo

## Rules:

1. OOP -> SOLID

## Design Pattern for func
1. Factory -> task creation
2. Command -> CLI 
3. Observer -> dashboard/ mail remainder
4. Singleton -> connection to db, universal unique id
5. Facade -> db api (chcemy mieć możliwość zmiany bazy lub obsługi kilku baz danych + schowanie zapytania do bazy poza commands)
6. Iterator -> get all task, sort and filtering


What's next?

1. Dashboard + cls task (powinna opierać się tylko o bazę danych). Wszystkie metody w dashbordzie powinny robić query do bazy
2. Dashboard powinien być observerem
3. Jeżeli coś się zmieni w bazie powinno zmienić się w dashboardzie
4. Wszystkie tabele powinny być stworzone na podstawie modeli
5. Dokumentacja
6. unit testy
7. statyczne typowanie
