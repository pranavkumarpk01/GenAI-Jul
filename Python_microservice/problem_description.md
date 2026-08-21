1.users can create tasks, manage, delete the tasks, as soon as task has been created or marked as complete a notification will be sent or log entry will be sent.

microservices ->  task microservice 
microservice -> notification microservice

features of microservice 
1.Single Responsibility per service -> task microservices. -> only tasks work and notification service -> notification

2.Each service has its own database 

3.Both the microservice communicarte with each other with the help of httpx protocol

4.Independent deployable -> Each service will have a dockerfile and will get deployed individually

5.Fault isoldation -> if notification service is down, task service will still successfully creates tasks


Inorder to run the complete application please run this command
-> docker-compose up --build