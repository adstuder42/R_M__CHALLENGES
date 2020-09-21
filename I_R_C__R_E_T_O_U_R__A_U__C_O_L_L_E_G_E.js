var irc = require('irc');

var Client = new irc.Client('irc.root-me.org', 'gR00tsBot', {
    channels: ['#root-me_challenge'],
    debug: true,
});

function getResult(val_1, val_2) {
    let result;
    val_1 = Math.sqrt(val_1);
    result = val_1 * val_2;
    result = result * 100
    result = Math.round(result);
    result = result / 100;
    return (result);
}

function getVal2(number)
{
    let i = 0;
    let val2;
    while (number[i] != "/")
        i++;
    i = i + 2;
    val2 = number.substr(i)
    val2 = parseInt(val2);
    return (val2);
}

Client.addListener("message", function (from, to, text, message) {
    if (from != "Candy")
        Client.say("candy", "!ep1");
    else {
        let val_1 = parseInt(text);
        let val_2 = getVal2(text);
        let result = getResult(val_1, val_2);
        let solution = result.toString();
        Client.say("candy", "!ep1 -rep " + solution);
    }
});