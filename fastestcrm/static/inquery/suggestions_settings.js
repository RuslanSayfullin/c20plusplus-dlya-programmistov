$("#address_client").suggestions({
    serviceUrl: "https://dadata.ru/api/v2",
    token: "51b22a5aa3db36bc9e89b07c3310e6987d0fa3af",
    type: "ADDRESS",
    /* Вызывается, когда пользователь выбирает одну из подсказок */
    onSelect: function (suggestion) {
        console.log(suggestion);
    }
});