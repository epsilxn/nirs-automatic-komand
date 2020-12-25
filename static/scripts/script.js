function setMinDate() {
    let currentDate = new Date()
    let year = currentDate.getFullYear()
    let month = currentDate.getMonth() + 1
    let day = currentDate.getDate()
    $("#originDate").attr("value", `${year}-${month}-${day + 1}`)
    $("#originDate").attr("min", `${year}-${month}-${day}`)
    $("#originDate").attr("max", `${year + 1}-${month}-${day}`)
    $("#destinationDate").attr("value", `${year}-${month}-${day + 4}`)
    $("#destinationDate").attr("min", `${year}-${month}-${day}`)
    $("#destinationDate").attr("max", `${year + 1}-${month}-${day}`)

    $("#originCity").val("Ульяновск")
    $("#destinationCity").val("Москва")
}

function cityCheck(city) {
    let result = city.match(/[^а-яА-Я-]/)
    if (result == null) {
        return true
    } else {
        return false
    }
}

function getData() {
    let originCity = $("#originCity").val()
    let destinationCity = $("#destinationCity").val()
    let originDate = $("#originDate").val()
    let destinationDate = $("#destinationDate").val()
    if ((originDate <= destinationDate) && cityCheck(originCity) && cityCheck(destinationCity)) {
        $.getJSON(
            "/get_prices",
            {
                "originCity": originCity,
                "destinationCity": destinationCity,
                "originDate": originDate,
                "destinationDate": destinationDate
            },
            function (data) {
                console.log(data)
                console.log(data.tickets)
                console.log(data.hotels)
                var app = new Vue({
                    el: "#app",
                    data: {
                        tickets: data.tickets,
                        hotels: data.hotels
                    }
                })
            }
        )
    } else {
        console.log("Случилась страшная беда!")
    }
}

$(document).ready(function () {
    setMinDate()
    $("button").on("click", ()=>{
        getData();
    })
});