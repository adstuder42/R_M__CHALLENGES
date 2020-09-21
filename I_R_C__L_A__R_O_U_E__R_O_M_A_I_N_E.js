var irc = require('irc');

var Client = new irc.Client('irc.root-me.org', 'gR00tsBot', {
    channels: ['#root-me_challenge'],
    debug: true,
});

var base = "abcdefghijklmnopqrstuvwxyz";
var basemaj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var base2 = "nopqrstuvwxyzabcdefghijklm";
var base2maj = "NOPQRSTUVWXYZABCDEFGHIJKLM";
var solution = "";
var rep = 0;
Client.addListener("message", function (from, to, text, message) {
    if (rep == 1)
        return;
    if (from != "Candy")
        Client.say("candy", "!ep3");
    else {
        let i = 0;
        while (text[i]) {
            let j = 0;
            if (text[i] == "0" || text[i] == "1" || text[i] == "2" || text[i] == "3" || text[i] == "4" || text[i] == "5" || text[i] == "6" || text[i] == "7" || text[i] == "8" || text[i] == "9") {
                solution = solution + text[i];
            }
            else {
                while (base2[j]) {
                    if (base2[j] == text[i]) {
                        solution = solution + base[j];
                        break;
                    }
                    j++;
                }
                j = 0;
                while (base2maj[j]) {
                    if (base2maj[j] == text[i]) {
                        solution = solution + basemaj[j];
                        break;
                    }
                    j++;
                }
            }
            i++;
        }
        console.log("==========", solution);
        Client.say("candy", "!ep3 -rep " + solution);
        rep = 1;
    }
});