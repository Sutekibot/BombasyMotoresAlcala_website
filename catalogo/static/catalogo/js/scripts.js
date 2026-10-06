function abrirCorreo() {
    var email = "motoresalcala1@hotmail.com";
    var subject = "Solicitud de Pedido";
    var body = "Hola, quiero realizar un pedido.";
    
    var isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

    if (isMobile) {
        window.location.href = "mailto:" + email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    } else {
        var gmailWebUrl = "https://mail.google.com/mail/?view=cm&fs=1&to=" + email + "&su=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
        window.open(gmailWebUrl, "_blank");
    }
}