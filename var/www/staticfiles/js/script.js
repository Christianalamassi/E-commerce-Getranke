var messages = document.getElementById('message_alert');
var alerts = new bootstrap.Alert(messages);

//for notification message
setTimeout(function () {
    alerts.close();
}, 3000);