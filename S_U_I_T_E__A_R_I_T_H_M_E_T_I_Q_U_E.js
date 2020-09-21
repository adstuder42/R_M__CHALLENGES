function getNumber(str) {
    let number = "";
    let i = 0;

    while ((str[i] >= "0" && str[i] <= "9") || str[i] == "+" || str[i] == "-" || str[i] == "*") {
        number = number + str[i];
        i++
    }
    return (parseInt(number));
}

module.exports = {
    'Test_1': function (browser) {
        browser
            .url('http://challenge01.root-me.org/programmation/ch1/')
            .waitForElementVisible('body')
            .source(function (result) {
                console.log(result.value);
                var html = result.value
                var var_1 = "";
                var var_2 = "";
                var var_3 = "";
                var var_4 = "";
                var op_1 = "";
                var i = 0;

                while (html[i] != "[")
                    i++;
                i = i + 2;
                console.log(html.substring(i));
                var_1 = getNumber(html.substring(i));
                while (html[i] != "]")
                    i++;
                i = i + 2;
                op_1 = html[i];
                while (html[i] != "*")
                    i++;
                i = i + 2;
                var_2 = getNumber(html.substring(i));
                while (html[i] != "=")
                    i++;
                i = i + 2;
                var_3 = getNumber(html.substring(i));
                while (html[i] != "U")
                    i++;
                i = i + 6;
                var_4 = getNumber(html.substring(i));
                console.log(var_1);
                console.log(var_2);
                console.log(var_3);
                console.log(var_4);
                console.log(op_1);

                let res = var_3;
                let par_1 = 0;
                let par_2 = 0;

                i = 1;

                while (i <= var_4) {
                    par_1 = res + var_1;
                    par_2 = (i - 1) * var_2;
                    if (op_1 == "+")
                        res = par_1 + par_2;
                    if (op_1 == "-")
                        res = par_1 - par_2;
                    i++;
                }
                console.log(res);
                var link = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=" + res;
                console.log(link);
                browser.url(link)
            })
            .pause(10000)
            .end();
    }
};