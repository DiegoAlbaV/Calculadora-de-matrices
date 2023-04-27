function escribirMatriz(matriz) {
  const contenido = matriz.map((fila) => fila.join(" ")).join("\n");
  const archivo = new Blob([contenido], {type: "text/plain"});
  const enlace = document.createElement("a");
  enlace.href = window.URL.createObjectURL(archivo);
  enlace.download = "salida.txt";
  enlace.click();
}
