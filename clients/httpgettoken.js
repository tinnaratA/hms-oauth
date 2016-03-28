var http = require('http');
 
// Set the headers
var headers = {
    'User-Agent':       'Super Agent/0.0.1',
    'Content-Type':     'application/x-www-form-urlencoded'
}
 
// Configure the request
//var uri = 'http://10.105.163.62:8000/o/token/?grant_type=password&username=admin&password=admin@1234&client_id=odQEaUKYZy9dinS1vhvZj6xotgbj5YEg9vFDDggN&client_secret=n7VAmhVOtF9CEBgrK3DHMtoZitcZgMPQW2lvXuCthyarucjKqP1ln5gzsHNLjga8YDCRWfiZk5KyFncYdRhhwzDDZljswd8O02NStrto0r78RoK5Smmj3uAHpkejs29R'
var options = {
    method: 'POST',
    host: '127.0.0.1',
    port: '8000',
    path: '/o/token/?grant_type=password&username=admin&password=admin@1234&client_id=oNqcvFrINsdc5l2vJxkYRKtBBg6TWr0ktJN0tSBV&client_secret=Bhc5wl09ih34MC8EEoJzrFukBNayZ7egQP4Zyzi6xtFqtGzXqFhQPBXXxRRkfMZ7swUB6Tf4f3rm2G6zJFXrrMP8OHoeXHKYsmgbIHAZa8YeVvkdm1mVJdeark7XwTMI'
    }
// Start the request
var request =  http.request(options, function (res) {
//var request = http.request(uri, function(res) {
  var chunks = [];
   
  res.on("data", function (chunk) {
    chunks.push(chunk);
    //console.log("response.dsta="+)
   // console.log(chunks.)
  });

  res.on("end", function () {
    var body = Buffer.concat(chunks);
    console.log(body.toString());

    var json = JSON.parse(body)

    var access_token = json.access_token;
    console.log("RECEIVED->ACCESS_TOKEN:"+json.access_token);
   // var user_url = "http://çΩΩ8000/users"
    var userapi_options =  {
         method: 'GET',
         host: '127.0.0.1',
         port: '8000',
         path: '/groups/',
         headers: {
             'Authorization': 'bearer '+access_token
            }
    };

    //var users_http_request = http.request(userapi_options, function(res) {
      var users_http_request = http.request(userapi_options, function(res) {
        users_http_request.auth = 'Bearer '+access_token;
       // console.log('request url:'+users_http_request.url);
        var user_chunks =[];
        
        res.on("data", function(chunk){
            user_chunks.push(chunk);
            //console.log("users_http_request.ondata.chunk"+chunk);
        });


        res.on("end", function(){
          var body = Buffer.concat(user_chunks);
          console.log("users_http_request.end");
        });
      //
    });
    users_http_request.on('error', function(e){
      if (e)
           throw(e);
      //TODO:
    });
    users_http_request.end();
   
  /**  var users_request = http.request(userapi_options, function (res) {
        var chunks = [];
   
  res.on("data", function (chunk) {
    chunks.push(chunk);
    //console.log("response.dsta="+)
   // console.log(chunks.)
   });
   //expecting user list data as json
    res.on("end", function () {
    var body = Buffer.concat(chunks);
    console.log(body.toString());

    });**/

  });
});

request.end();