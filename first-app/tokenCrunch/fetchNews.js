const GoogleNewsRss = require('google-news-rss');

const googleNews = new GoogleNewsRss();

googleNews
   .search('Crytocurrency')
   .then(resp => console.log(resp));
