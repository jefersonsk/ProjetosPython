function validar() {
    
    const regexSigla = /^[A-Z]{3,5}$/;
    const dataInicio = new Date('1890-01-01');

    var controle = true;
    var s = document.getElementById("sigla");
    var n = document.getElementById("nome");
    var uf = document.getElementById("estado");
    var d = document.getElementById("data");
    var dataFim = new Date(d.value);

    var e = document.getElementById("erros");

    e.innerHTML = '';

    if (s.value == '' || regexSigla.test(s.value) === false) {
        e.innerHTML += "<li>Sigla é obrigatória e conter de três a cinco letras maiúsculas!!!</li>";
        s.style = "background-color: #FF0000";
        controle = false;
    } else {
        s.style = "background-color: #FFFFFF";
    }

    if (n.value == '' || n.value.length < 20 || n.value.length > 100) {
        e.innerHTML += "<li>Nome é obrigatório e ter de 20 a 100 caracteres!!!</li>";
        n.style = "background-color: #FF0000";
        controle = false;
    } else {
        n.style = "background-color: #FFFFFF";
    }

    if (d.value == '' || (dataFim.getTime() < dataInicio.getTime())) {
        e.innerHTML += "<li>Data de fundação é obrigatória e ser marior que 01 de janeiro de 1890!!!</li>";
        d.style = "background-color: #FF0000";
        controle = false;
    } else {
        d.style = "background-color: #FFFFFF";
    }

    if (uf.value == '') {
        e.innerHTML += "<li>Estado é obrigatório!!!</li>";
        uf.style = "background-color: #FF0000";
        controle = false;
    } else {
        uf.style = "background-color: #FFFFFF";
    }

    return controle;
}

function validarJQuery() {
    $('#erros').empty();

    const regexSigla = /^[A-Z]{3,5}$/;

    // O seletor pode selecionar a classe, no exemplo abaixo .obg
    // Pode o selettor pode selecionar os componentes classes, tags, ids
    var x = $('.obg');
    for (var i=0; i<x.length; i++) {
        if (x[i].value == '') {
            $('#erros').append('<li>Campus "'+$('label[for="'+x[i].id+'"]').text()+'" obrigatório!!!</li>');
            x[i].style = 'background-color: #FF0000';
        } else {
            x[i].style = 'background-color: #FFFFFF';
        }
    }
    
    if ($('#sigla').val() == '' || regexSigla.test($('#sigla').val()) === false) {
        $('#sigla').after('<p>Sigla deve conter de três a cinco letras maiúsculas!!!</p>');
        $('#sigla').css('background-color', 'red');
        controle = false;
    } else {
        $('#sigla').css('background-color', 'white');
    }

    return controle;
}

function buscarcep() {
    var params ='{}';
    $.ajax({
        type: "GET",
        url: "https//viacep.com.br/ws/"+$('#cep').val()+"/json/",
        data: params,
    })
}

// Comunicação assincrona e componentes prontos