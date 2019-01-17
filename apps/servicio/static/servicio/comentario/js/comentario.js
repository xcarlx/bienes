function comentario() {
    var columnas1 = [
        {
            title: 'Texto',
            data: 'texto',
            width: "40%"
        },
        {
            title: 'Fecha',
            data: 'fecha',
            width: "20%"
        },
        {
            title: "Acciones",
            width: "10%",
        },
        {
            title: "Acciones",
            width: "10%",
            visible: false
        }
    ];
    var listadatos1 = "{% url 'comentario-data' 123 %}".replace("123", datos_servicio.id);
    var table1 = $('#tabla2').DataTable(ConfigTable(listadatos1, columnas1, lenguaje));
    var urlagregar1 = "{% url 'comentario-agregar' 123 %}".replace("123", datos_servicio.id);
    var urleditar1 = "{% url 'comentario-editar' 123 %}";
    var urleliminar1 = "{% url 'comentario-eliminar' 123 %}";
    var titulo1 = "Comentario";
    var data1 = null;
    var btnNuevo1 = $("#btnNuevo1");
    var formulario1 = $("#Formulario");
    $('#Modal').on('shown.bs.modal', function (e) {
        {
            $('#id_texto').trigger('focus')

        }
    });
    FormunarioJs(btnNuevo1, table1, formulario1, data1, titulo1, urlagregar1, urleditar1, urleliminar1);
}