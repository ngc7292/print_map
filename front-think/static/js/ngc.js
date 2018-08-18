//var login = new Vue{

//}

//var register = new Vue{

//}

var addCitys = new Vue({
    el:"#citys",
    data :{
        citys:[{
            name:'',
        }]
    },
    created:function(){
        if (this.citys.name == "")
        {
            console.log("yes");
        }
        else {
         console.log("no");
        }
    },
    methods:{
        addcity:function () {
            this.citys.push({
                name:''
            })
        },
        submitcity:function () {
            var cityStr="";
            for (var city in this.citys) {
                cityStr += this.citys[city].name + "+";
            }
            console.log(JSON.stringify(cityStr));
            this.$http.post('http://127.0.0.1/map',cityStr).then((response) => {
                console.log(response.data);
            },(response) =>{
                console.log("error");
            });
        }
    }
});

var login = new Vue({
    el:"#form-top",
    data:{
        formss:"            <p class=\"welcome\">Welcome</p>\n" +
        "            <button class=\"button history\">history</button>\n" +
        "            <button class=\"button history\">logout</button>"
    }
})


