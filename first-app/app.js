
const logger = require('./logger');
const https = require('https')

//logger('message')

function queryWebsite(query_url){
  https.get(query_url, (res) => {
    console.log('statusCode:', res.statusCode);
    console.log('headers:', res.headers);

    res.on('data', (d) => {
      process.stdout.write(d);
    });

  }).on('error', (e) => {
    console.error(e);
  });
}

data = queryWebsite('https://www.phantom.us/apps/')
