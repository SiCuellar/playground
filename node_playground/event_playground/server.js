var http = require('http');

var server = http.createServer(function(req, res) {
  res.writeHead(200);
  res.end('Hi Everyone!')
})

server.on('close', function() { //we listen to the close event
  console.log('it worked');
})

server.listen(8080); // start the server

server.close(); //stops the server.  Trigers the close event
