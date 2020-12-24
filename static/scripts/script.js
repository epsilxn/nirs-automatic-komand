function setMinDate() {
    let currentDate = new Date()
    let year = currentDate.getFullYear()
    let month = currentDate.getMonth() + 1
    let day = currentDate.getDate()
    $("#originDate").attr("min", `${year}-${month}-${day}`)
    $("#destinationDate").attr("min", `${year}-${month}-${day}`)
}

function getData() {
    let originCity = $("#originCity").val()
    let destinationCity = $("#destinationCity").val()
    let originDate = $("#originDate").val()
    let destinationDate = $("#destinationDate").val()
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
        }
    )
}

$(document).ready(function () {
    setMinDate()
    $("button").on("click", ()=>{
        getData();
    })
});