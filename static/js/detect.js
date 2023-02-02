function change_pic(){

    select = document.getElementById('plant_name');
    var value = select.options[select.selectedIndex].value;

    if(value == 'Strawberry'){
        document.getElementById('plant-img').src = "../static/images/icons8-strawberry-64.png";
    }

}