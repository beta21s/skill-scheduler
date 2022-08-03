function select2_2_json(val) {
    var arr = [];
    for (j = 0; j < val.length; j++) {
        arr.push(val[j].id);
    }
    return JSON.stringify(arr);
}

function numberToWeek(val) {
    val = parseInt(val);
    if(val === 0)
        return 'Chủ nhật';
    return "Thứ " + (val + 1);
}

function numberToWeekf_array(val) {
    var qk = [];
    val.forEach(function (item){
        qk.push(numberToWeek(item));
    });
    return qk;
}


