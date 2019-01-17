function FormunarioJs(btnNuevo, table, formulario, data, titulo, urlagregar, urleditar, urleliminar) {
    $('#tabla tbody').on('click', 'tr', function () {
        data = table.row(this).data();
    });
    btnNuevo.on("click", function () {
        $("#Modal").find(".modal-body").load(urlagregar);
        $("#Modal").modal('show');
        $("#ModalLabel").text("Nuevo " + titulo);
        formulario.attr('action', urlagregar);
    });

    table.on('click', '.btnEditar', function () {
        var url1 = urleditar.replace('123', data.id);
        $("#Modal").find(".modal-body").load(url1);
        $("#Modal").modal('show');
        formulario.attr('action', url1);
        $("#ModalLabel").text("Editando " + titulo);
    });
    table.on('click', '.btnEliminar', function () {
        var url1 = urleliminar.replace('123', data.id);
        $("#Modal").find(".modal-body").load(url1);
        $("#Modal").modal('show');
        formulario.attr('action', url1);
        $("#ModalLabel").text("Eliminado " + titulo);
    });

    formulario.submit(function (event) {
        event.preventDefault();
        $("#Modal").modal('hide');
        // $('.Contenedor').waitMe({
        //     effect: 'ios',
        //     text: '',
        //     maxSize: '',
        //     waitTime: -1,
        //     textPos: 'vertical',
        //     fontSize: '',
        //     source: '',
        // });
        var post_url = $(this).attr("action");
        var request_method = $(this).attr("method");
        var formData = new FormData($(this)[0]);
        $.ajax({
            url: post_url,
            type: request_method,
            data: formData,
            processData: false,  // tell jQuery not to process the data
            contentType: false,   // tell jQuery not to set contentType
            success: function (response) {
                if (typeof response.datos === 'undefined') {
                    // $('.Contenedor').waitMe("hide");
                    $("#Modal").modal('show');
                    $("#Modal").find(".modal-body").html(response);
                }
                else {
                    // $('.Contenedor').waitMe("hide");
                    table.ajax.reload();
                    $.notify(response.mensaje + " (" + response.datos.descripcion + ")", "success");
                }
            },
            error: function (response) {
                console.log(response)
                // $('.Contenedor').waitMe("hide");
                $.notify("Ocurrio algo inesperado", "error");

            }
        });

    });

}


function SaveFormulario(formulario, table) {

    formulario.submit(function (event) {
        event.preventDefault();
        $("#Modal").modal('hide');
        // $('.Contenedor').waitMe({
        //     effect: 'ios',
        //     text: '',
        //     maxSize: '',
        //     waitTime: -1,
        //     textPos: 'vertical',
        //     fontSize: '',
        //     source: '',
        // });
        var post_url = $(this).attr("action");
        var request_method = $(this).attr("method");
        var formData = new FormData($(this)[0]);
        $.ajax({
            url: post_url,
            type: request_method,
            data: formData,
            processData: false,  // tell jQuery not to process the data
            contentType: false,   // tell jQuery not to set contentType
            success: function (response) {
                if (typeof response.datos === 'undefined') {
                    $('.Contenedor').waitMe("hide");
                    $("#Modal").modal('show');
                    $("#Modal").find(".modal-body").html(response);
                } else {
                    // $('.Contenedor').waitMe("hide");
                    table.ajax.reload();
                    $.notify(response.mensaje + " (" + response.datos.descripcion + ")", "success");
                }
            },
            error: function (response) {
                // $('.Contenedor').waitMe("hide");
                $.notify("Ocurrio algo inesperado", "error");

            }
        });

    });
}

function SaveFormularioSolo(formulario, modal) {

    formulario.submit(function (event) {
        event.preventDefault();
        modal.modal('hide');
        // $('.Contenedor').waitMe({
        //     effect: 'ios',
        //     text: '',
        //     maxSize: '',
        //     waitTime: -1,
        //     textPos: 'vertical',
        //     fontSize: '',
        //     source: '',
        // });
        var post_url = $(this).attr("action");
        var request_method = $(this).attr("method");
        var formData = new FormData($(this)[0]);
        $.ajax({
            url: post_url,
            type: request_method,
            data: formData,
            processData: false,  // tell jQuery not to process the data
            contentType: false,   // tell jQuery not to set contentType
            success: function (response) {
                if (typeof response.datos === 'undefined') {
                    // $('.Contenedor').waitMe("hide");
                    modal.modal('show');
                    modal.find(".modal-body").html(response);
                } else {
                    $('.Contenedor').waitMe("hide");
                    $.notify(response.mensaje + " (" + response.datos.descripcion + ")", "success");

                }
            },
            error: function (response) {
                // $('.Contenedor').waitMe("hide");
                $.notify("Ocurrio algo inesperado", "error");
            }
        });

    });
}