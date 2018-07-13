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
  console.log(value)
  //sendEmail(value)
  //writeToFile(value)
});
  //writeToFile(value)

  //console.info(value); // Success!
  //var arrayLength = value.length;
  //for (var i = 0; i < arrayLength; i++){
  //  console.log(value[i]);
  //}



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

//This function diffs the two arrays
Array.prototype.diff = function(a) {
    return this.filter(function(i) {return a.indexOf(i) < 0;});
};

//var dif1 = [1,2,3,4,5,6].diff( [3,4,5] );
//console.log(dif1); // => [1, 2, 6]
let fileDiff = file1Contents.diff(file2Contents)
//console.log(fileDiff)
//console.log(file1Contents)
//var arrayLength = file1Contents.length;
//for (var i = 0; i < arrayLength; i++){
//  console.log(file1Contents[i]);}

//First read json files contents to variable, convert if necessary
//Make a function that accepts two inputs, file1 and file2.  Diff the contents and returns diff
//DIFF END



function sendEmail(value){
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
    text: 'That was easy!',
    attachments: [
      {
        //filename: 'currentAppList.json',
        //content: value,
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

function writeToFile(value){
  var filepath = '/Users/christopher.rosa/Desktop/first-app/my-headless-chrome/currentAppList.json';
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

//sendEmail()
//Need to remove ['ALL APPS\n', 'JOIN THE COMMUNITY\n', 'Don’t see what you’re looking for? Build your own app.\nJoin the Phantom community to access developer resources, including documentation and tutorials on app development.\n\n', '']
//Need to format JSON to HTML

//Read file async
/*
var fs = require('fs');
var obj;
fs.readFile('file', 'utf8', function (err, data) {
  if (err) throw err;
  obj = JSON.parse(data);
});
*/




//Fetch list of APPS
//Write to file
//Email list of new plugins

//24 hours
//Fetch list of APPS and check against local file
//IF DIFF --> email
//ELSE --> do nothing
