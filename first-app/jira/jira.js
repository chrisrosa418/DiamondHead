// With ES5
var JiraApi = require('jira-client');


// Initialize
var jira = new JiraApi({
  protocol: 'https',
  host: 'jira-sandbox.eng.fireeye.com:8443',
  username: 'christopher.rosa',
  password: '',
  apiVersion: '2',
  strictSSL: true
});

jira.findIssue('FPLUG-900')
  .then(function(issue) {
    console.log('Status: ' + issue.fields.status.name);
  })
  .catch(function(err) {
    console.error(err);
  });
