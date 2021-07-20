var object = {"a": { "b": { "c": "d" }}};

var object2 = {"x":{"y":{"z":"a"}}};

function getObjectKeys(object, key) {
    const keys = key.split('.');
    let obj = object;
    for (let ikey of keys) {
        for (let [objKey, value] of Object.entries(obj)) {
            if(!keys.includes(objKey)) {
                continue;
            }
            obj = value;
        }
    }
    return obj;
}

alert(getObjectKeys(object, 'a.b.c'));
alert(getObjectKeys(object2, 'x.y.z'));

