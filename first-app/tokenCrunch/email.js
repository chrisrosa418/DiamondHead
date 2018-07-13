var nodemailer = require('nodemailer');
var fs = require('fs');

function sendEmail(htmlFile){
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
    html: htmlFile
    };

  transporter.sendMail(mailOptions, function(error, info){
    if (error) {
      console.log(error);
    } else {
      console.log('Email sent: ' + info.response);
    }
  });
}

//sendEmail('x')
var file1 = '/Users/christopher.rosa/Desktop/first-app/tokenCrunch/testEmail.html';

var htmlFile = fs.readFileSync(file1, 'utf8');

//console.log(htmlFile);
sendEmail(htmlFile);
