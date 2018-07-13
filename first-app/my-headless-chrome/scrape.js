//Imports
const puppeteer = require('puppeteer');
var fs = require('fs');
var nodemailer = require('nodemailer');

//Scrape website
let scrape = async () => {
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();

    await page.goto('https://www.phantom.us/apps/');
    await page.waitFor(1000);

    const result = await page.evaluate(() => {
        let data = [];
        let elements = document.querySelectorAll('#apps-main-content > div > div.col-md-9.app-list > div.all-apps');

        for (var element of elements){
          let title = element.innerText;

          data.push(title)
        }
        return data
    });

    browser.close();
    return result;
};


scrape().then((value) => {
  //console.log(value[0]);
  //var filepath = '/Users/christopher.rosa/Desktop/first-app/my-headless-chrome/currentAppList.json';

  //console.log('Success - Writing to local file /currentAppList');
  //writeToFile(value, filepath);

  //console.log('File write success - Sending email');
  //sendEmail(filepath);


  //var arrayLength = value.length;
  //for (var i = 0; i < arrayLength; i++){
  //  console.log(value[i]);
  //}

});

function sendEmail(filepath){
  var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'aclark.dil@gmail.com',
      pass: 'GreWic98*'
    }
    });

  var mailOptions = {
    from: 'aclark.dil@gmail.com',
    to: 'chrisrosa418@gmail.com',
    subject: 'Sending Email using Node.js',
    text: 'Current app list attached;',
    attachments: [
      {
        path:'/Users/christopher.rosa/Desktop/first-app/my-headless-chrome/currentAppList.json'

      },
    ]
    };

  transporter.sendMail(mailOptions, function(error, info){
    if (error) {
      console.log(error);
    } else {
      console.log('Email sent: ' + info.response);
    }
  });
}

function writeToFile(value, filepath){
  var buffer = JSON.stringify(value);


  fs.open(filepath, 'w', function(err, fd) {
      if (err) {
          throw 'error opening file: ' + err;
      }

      fs.write(fd, buffer, 0, buffer.length, null, function(err) {
          if (err) throw 'error writing file: ' + err;
          fs.close(fd, function() {
              console.log('file written');
          })
      });
  });
}

function readFile(filepath){
  //READ FROM FILE
  function readFile(file){
    fs.readFile(file, 'utf8', function (err,data) {
      if (err) {
        return console.log(err);
      }
      var fileContents = data;
      console.log(fileContents)
      return(data);
      //console.log(data)
    });
    //return(fileContents);
  }
  var file1 = '/Users/christopher.rosa/Desktop/first-app/my-headless-chrome/currentAppList.json';
  var file2 = '/Users/christopher.rosa/Desktop/first-app/my-headless-chrome/currentAppList2.json';


  var file1Contents = JSON.parse(fs.readFileSync(file1, 'utf8'));
  var file2Contents = JSON.parse(fs.readFileSync(file2, 'utf8'));
  //END READ FILE
}




//Fetch list of APPS
//Write to file
//Email list of new plugins

//24 hours
//Fetch list of APPS and check against local file
//IF DIFF --> email
//CheckSum on the list
//ELSE --> do nothing
