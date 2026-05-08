function validar() {
    let verificar_sigla = document.getElementById('sigla')

    if (verificar_sigla.value == '') {
        alert('Sigla obrigatória')
        return false
    }

}