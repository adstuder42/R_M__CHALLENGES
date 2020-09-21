var irc = require('irc');
var zlib = require('zlib');

var Client = new irc.Client('irc.root-me.org', 'gR00tsBot', {
    channels: ['#root-me_challenge'],
    debug: true,
});

var rep = 0;
Client.addListener("message", function (from, to, text, message) {
    if (rep == 1)
        return;
    if (from != "Candy")
        Client.say("candy", "!ep4");
    else {
        var buffer = new Buffer(text, 'base64');
        buffer = zlib.unzip(buffer, function (err, buffer) {
            if (!err) {
                Client.say("candy", " !ep4 -rep " + buffer.toString());
            }
        });
        result = buffer.toString();
        rep = 1;
    }
}
);