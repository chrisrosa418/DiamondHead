var request = require('request');

const client_secret = 'jv7iuOez2AC0HhFhuLEVXEYpzDe1zUX5';
const client_id = '7a564d5a-4fd0-11e8-8b57-ac1ff8470000';

var createTicket =  `https://api.ngdesk.com/v2/operations/tickets?client_secret=${client_secret}&client_id=${client_id}`;
var queryUrl = `https://api.ngdesk.com/v2/operations/get_tickets?client_secret=${client_secret}&client_id=${client_id}`;
console.log(queryUrl);


request.post(
    createTicket,
    {
  "TICKETS": [
    {
      "SUBJECT": "This is the ticket's subject",
      "TICKET_MESSAGES": {
  	    "BODY": "This is the initial message for the ticket",
  	    "IS_INTERNAL": "Y"
      },
      "SEVERITY": "Low",
      "SOURCE": "API",
      "STATUS": "NEW"
    }
  ]
},
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body)
        }
    }
);
