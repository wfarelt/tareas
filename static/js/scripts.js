function abrirModal(url) {
    console.log('abrirModal');
    $('#popup').load(url, function () {
        console.log('modal cargado');
        $(this).modal({
            backdrop: 'static',
            keyboard: false
        });
        $(this).modal('show');
        console.log(data-target);
        console.log('modal aberto');
        
    });
    return false;
}

function cerrarModal() {
    $('#popup').modal('hide');
    return false;
}

function enviarFormulario(form) {
    
    var url = $(form).attr('action');
    console.log(url);
    var dados = $(form).serialize();
    $.post(url, dados, function (data) {
        console.log('form enviado');
        $('#popup').html(data);
        location.reload();

    });
    
    
    return false;
}

