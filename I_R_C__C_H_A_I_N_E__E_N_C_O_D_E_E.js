var irc = require('irc');

var Client = new irc.Client('irc.root-me.org', 'gR00tsBot', {
    channels: ['#root-me_challenge'],
    debug: true,
});

let rep = 0;
Client.addListener("message", function (from, to, text, message) {
    if (from != "Candy")
        Client.say("candy", "!ep2");
    else if (rep == 0) {
        rep = 1;
        solution = Buffer.from(text, 'base64').toString();
        Client.say("candy", "!ep2 -rep " + solution);
    }
});