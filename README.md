# CrediRap

This is our Portfolio Project, concluding our Foundations Year at Holberton School

## Project Description

<p>This project proposes a workforce based credit system, implementing technology and performance. The main goal is to facilitate fast loan access to workers based on their performance. We have two main participants. Investors and workers. Investors invest in the loan system based on the worker's score and workers will have access to the loan depending on their performance.</p>

<p>Conditions</p>

<p>Worker loans are given under a score performance. Loans can either be used for the purchase of new vehicles or vehicle restoration and/or fixes. Vehicles are meant to be used by the worker inside the platform's activity.</p>

<p>The main objective of our project is to deliver a product that measures workers efficiency for a performance based loan system. We will develop a system that will give a score that depends on different variables, for example, location, distance (km), time, amount of tasks and this will help investors safeguard their investment by loaning to high scoring ranked workers.</p>

## API and Methods
 
GET: Create a new user.
* /signup/id

POST: Return accounts information.
* /users/id/profile

PUT: Update users information
* /users/id/profile/edit

GET:
* /users/id/profile/bank-details
* /users/id/profile/investment

GET: Return status for investors account.
* /users/id/profile/status

PUT: Create a new application form
* /users/id/profile/requests

GET: Return form details
* /users/id/profile/requests/loan-details

GET: Catch authentication and update credentials
* /signin
* /help/reset-login-password
* /signin/restore-password

PUT:
* /signin/restore-password/new

## Data Modeling

![](img/modelo_entidad_relacionDB.png)

## Build With

* Python - Programming language
* Mysql - Databases

## License

Public Domain. No copy write protection.

## Authors
* Kevin Castro - [Github](https://github.com/KevinCastroP) / [Twitter](https://twitter.com/ccali_k)  
* Luis Herrera - [Github](https://github.com/lh1008) / [Twitter](https://twitter.com/lh1008)
* Jhonatan Legarda - [Github](https://github.com/steven-cruz) / [Twitter](https://twitter.com/JhonatanLegarda
)