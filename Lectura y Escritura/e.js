function leerMatriz() {
  const archivo = document.getElementById("entrada").files[0];
  const lector = new FileReader();

  lector.onload = function(evento) {
    const contenido = evento.target.result;
    const lineas = contenido.trim().split("\n");
    const matriz = [];

    for (let i = 0; i < lineas.length; i++) {
      const valores = lineas[i].trim().split(" ");
      matriz.push(valores.map((x) => parseInt(x)));
    }

    // Procesa la matriz como desees
    const resultado = matriz.map((fila) => fila.reverse());

    // Escribe el resultado en un archivo de texto
    escribirMatriz(resultado);
  };

  lector.readAsText(archivo);
}
