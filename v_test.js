const 
    Base64 = require('./base64'),
    fs = require('fs'),
    ASN1DOM = require('./dom');

let txt_file = process.argv[2];
let dg = process.argv[3];
let data;
console.log(txt_file);
fs.readFile(txt_file, 'utf-8', (err, raw_data) => {
    data = JSON.parse(raw_data);
    console.log('Decoding data group %s ...', dg);
    switch (dg){
        case 'dg1':
            text = data.dg1;
            break;
        case 'dg13':
            text = data.dg13;
            break;
        case 'dg14':
            text = data.dg14;
            break;
        case 'dg15':
            text = data.dg15;
            break;
        case 'com':
            text = data.com;
            break;
        case 'sod':
            text = data.sod;
            break;
        case 'sodFile':
            text = data.sodFile;
            break;
        default:
            console.log("Cannot decode %s group.", dg);
            return;
    }
    let b64Norm = Base64.unarmor(text);
    const asn1 = ASN1DOM.decode(b64Norm, 0);
    console.log(asn1.toVText());
});