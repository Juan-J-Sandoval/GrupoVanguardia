$(function(){
    $("#btn_datos").click(function () {
        var user = $('input:radio[name=nombre]:checked').val()
        var btn = $('#btn_datos').val();
        $.ajax({
            url: "/req",
            data: {"nombre":user, "boton":btn},
            type: "GET",
            success: function (datos) {
                var obj = $.parseJSON(datos)
                salida = '';
                for(var i=0; i< obj.baseDeIncidencias.length; i++){
                    if (obj.baseDeIncidencias[i]['true'] != undefined){
                        salida += '<tr>'
                        + '<td scope="row"> Aceptable </td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['true'].comentario +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['true'].Usuario +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['true'].Bot +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['true'].usuario +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['true'].bot +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['true'].fecha +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['true'].hora +'</td>'
                        +'</tr>';
                    }
                    else{
                        salida += '<tr>'
                        + '<td scope="row"> Error </td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['false'].comentario +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['false'].Usuario +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['false'].Bot +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['false'].usuario +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['false'].bot +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['false'].fecha +'</td>'
                        + '<td>'+ obj.baseDeIncidencias[i]['false'].hora +'</td>'
                        +'</tr>';
                    }
                }
                $('#vistaT').html(salida);
            },
            error: function(error){
                alert(error);
            }
        });
    });
    $("#btn_esta").click(function () {
        var user = $('input:radio[name=nombre]:checked').val();
        var btn = $('#btn_esta').val();
        $.ajax({
            url: "/req",
            data: {"nombre":user, "boton":btn},
            type: "GET",
            success: function (datos) {
                alert("Porcentaje de respuestas correctas: "+datos.acerto+ "\nProcentaje de respuestas incorrectas: "+datos.erro)
            },
            error: function(error){
                alert(error);
            }
        });
    });
});