function returnValue() {
     document.getElementById("resultado").innerHTML = "Verificando..." + "<br>" + '<div class="loader"><div>';

     
     const api_url = 'https://detector-fake-news.herokuapp.com';
     
     const noticia = {
         url: document.getElementById("noticia_url").value
        };
        
    axios.post(api_url, noticia)
        
    .then(function(response){
        //document.getElementById("resultado").innerHTML = response.data.results.resultado;

        if (response.data.results.resultado == "true") {
            document.getElementById("resultado").setAttribute("class", "true");
            document.getElementById("resultado").innerHTML = "Verdadeiro";
        } else {
            document.getElementById("resultado").setAttribute("class", "false");
            document.getElementById("resultado").innerHTML = "Falso";
        }

        document.getElementById("prob").innerHTML = "Probabilidade de ser falsa: " + 
        (100*response.data.results.probabilidade).toFixed(3) + "%";
        console.log(response.data);
    });
}
function centerTitle() {
	document.getElementsByClassName("title toc-ignore")[0].setAttribute("align", "center");
}