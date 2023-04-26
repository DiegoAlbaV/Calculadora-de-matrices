//Esto es nada más una primera versión; pero no es definitiva; @valdes Nava Javier

var arrayData = new Array();
var arrayFilas = new Array();
var arrayColumnas = new Array();         //Creo los arreglos

var archivoTxt = new XMLHttpRequest();   //nos ayuda a  obtener cualquier tipo de dato
var fileRuta = 'index.txt';             //aquí pongo el nombre del archivo que queremos leer
var dataSum = 0;
archivoTxt.open('GET',fileRuta,false);  //abre el archivo
archivoTxt.send(null);

// creo una variable que será un arreglo
var txt = archivoTxt.responseText;
var fil = archivoTxt.responseText;
var col = archivoTxt.responseText;

console.log('el arreglo de txt mide: ' + txt.length);

// voy llenando el arreglo que acabo de crear con los datos del archivo txt
for (var i = 0; i < txt.length; i++)
{
    arrayData.push(txt[i]);
}

//esto nomas es para verificar que todo salió bien
arrayData.forEach
    (
    function(data)
    {
        console.log(data);
        dataSum += parseFloat(data);
    }
    );
    if(dataSum==0)
    {
        console.log('inserta un dato en index.txt');
    }
    else
    {
        console.log('la suma de los datos De TXT es :' + dataSum);
    }
    console.log(txt[0]);

    for(var j = 0; j < txt.length; j++)
    {
        if (j < (txt.length)/2)
        {
            arrayFilas.push(fil[j]);
            console.log("de las filas salio: "+ fil[j]);
        }
        if (j > (txt.length)/2)
        {
            arrayColumnas.push(col[j]);
            console.log("de las columnas salio: "+ fil[j]);
        }
        if (j == txt.length)
        {
            console.log("aquí voy a meter el resultado");
            //llenar el arreglo con resultados
        }
    }
