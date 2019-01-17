function ConfigTable(listadatos, columnas, lenguaje) {
    var paraters = {
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": listadatos,
        },
        "columns": columnas,
        "scrollY": "450",

        language: {
            "url": lenguaje
        },
        "lengthMenu": [[5, 10, 15, 20], [5, 10, 15, 20]],
        "dom": '<"top">frt<"bottom row"<"col col-md-6"l><"col col-md-6"p>"><"clear"i>',
        "columnDefs": [
            {
                "name": "acciones",
                "targets": -3,
                "data": null,
                "defaultContent": "<button class='btnInfo btn btn-info btn-sm fa fa-info-circle'></button>",
                "orderable": false
            },
            {
                "name": "acciones",
                "targets": -2,
                "data": null,
                "defaultContent": "<button  class='btnEditar btn btn-info btn-sm fa fa-pencil'></button>&nbsp;<button class='btnEliminar btn btn-danger btn-sm fa fa-trash-o'></button>",
                "orderable": false
            },
            {
                "name": "pendiente_pago",
                "targets": -1,
                "data": null,
                "defaultContent": "<button  class='btnGenerarCodigo btn btn-info btn-sm fa fa-money'></button>",
                "orderable": false
            }
        ],
        select: true

    };
    return paraters;

}
