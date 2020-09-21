var fs = require('fs');
const replaceColor = require('replace-color');
const sharp = require('sharp');
const tesseract = require("node-tesseract-ocr");

const config = {
  lang: "eng",
  dpi: 300,
  oem: 3,
  psm: 3,
}

var captcha = "";

module.exports = {
  'Captcha solver': function (browser) {
    browser
      .url('http://challenge01.root-me.org/programmation/ch8/')
      .waitForElementVisible('body')
      .source(function (result) {
        console.log(result.value);
        var html = result.value
        var data = "";
        var i = 0;
        while (html[i]) {
          if (html[i] == "e" && html[i + 1] == "6" && html[i + 2] == "4" && html[i + 3] == ",") {
            i = i + 4;
            while (html[i] != "\"") {
              data = data + html[i];
              i++
            }
            console.log(data);
            break;
          }
          i++;
        }
        let buff = new Buffer(data, 'base64');
        fs.writeFileSync('captcha.png', buff);
        replaceColor({
          image: './captcha.png',
          colors: {
            type: 'hex',
            targetColor: '#000000',
            replaceColor: '#FFFFFF'
          }
        }, (err, jimpObject) => {
          if (err) return console.log(err)
          jimpObject.write('./output.png', (err) => {
            if (err) return console.log(err)
            let inputFile = "output.png";
            let outputFile = "final.png";

            sharp(inputFile).resize({ height: 300 }).toFile(outputFile)
              .then(function (newFileInfo) {
                console.log("Success")
              })
              .catch(function (err) {
                console.log("Error occured");
              });
            tesseract.recognize("final.png", config)
              .then(text => {
                console.log("Result:", text);
                browser.setValue('input[type=text]', text);
              })
              .catch(error => {
                console.log(error.message)
              })
            console.log("\n\n\n\n", captcha, "\n\n\n\n\n");
          })
        })
      })
      .assert.visible('input[type=text]')
      .pause(10000)
      .assert.visible('input[type=submit]')
      .click('input[type=submit]')
      .pause(10000)
      .end();
  }
};
