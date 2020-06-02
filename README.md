# CrediRap

This is our Portfolio Project, concluding our Foundations Year at Holberton School

## Project Description

<p>This project proposes a workforce based credit system, implementing technology and performance. The main goal is to facilitate fast loan access to workers based on their performance. We have two main participants. Investors and workers. Investors invest in the loan system based on the worker's score and workers will have access to the loan depending on their performance.</p>

<p>Conditions</p>

<p>Worker loans are given under a score performance. Loans can either be used for the purchase of new vehicles or vehicle restoration and/or fixes. Vehicles are meant to be used by the worker inside the platform's activity.</p>

<p>The main objective of our project is to deliver a product that measures workers efficiency for a performance based loan system. We will develop a system that will give a score that depends on different variables, for example, location, distance (km), time, amount of tasks and this will help investors safeguard their investment by loaning to high scoring ranked workers.</p>

## API and Methods
 
<p>GET: Create a new user.</p>
/signup/id

<p>POST: Return accounts information.</p>
/users/id/profile

<p>PUT: Update users information</p>
/users/id/profile/edit

<p>GET:</p>
/users/id/profile/bank-details
/users/id/profile/investment

<p>GET: Return status for investors account.</p>
/users/id/profile/status

<p>PUT: Create a new application form</p>
/users/id/profile/requests

<p>GET: Return form details</p>
/users/id/profile/requests/loan-details

<p>GET: Catch authentication and update credentials</p>
/signin
/help/reset-login-password
/signin/restore-password

<p>PUT:</p>
/signin/restore-password/new


## Authors
Kevin Castro - [Github](https://github.com/KevinCastroP) / [Twitter](https://twitter.com/ccali_k)  
Luis Herrera - [Github](https://github.com/lh1008) / [Twitter](https://twitter.com/lh1008)
Jhonatan Legarda - [Github](https://github.com/steven-cruz) / [Twitter](https://twitter.com/JhonatanLegarda
)