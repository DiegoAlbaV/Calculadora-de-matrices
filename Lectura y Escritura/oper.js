const dropArea = document.querySelector(".drop-area");
const dragText = dropArea.querySelector("h2");
const button = dropArea.querySelector("button");
const input = dropArea.querySelector("#input-file");
let files;

button.addEventListener
('click',e =>
{
    input.click();
}
)

input.addEventListener('change', (e) =>
{
    files = input.file;
    dropArea.classList.add("active");
    showFiles(files);
    dropArea.classList.remove("active");
});

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("active");
    dragText.textContent = "suelta para subir los archivos";
})

dropArea.addEventListener("dragleave", (e) => {
    e.preventDefault();
    dropArea.classList.remove("active");
    dragText.textContent = "Arrastra y suelta imagenes";
})

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    files = e.dataTransfer.files;
    showFiles(files);
    dropArea.classList.remove("active");
    dragText.textContent = "Arrastra y suelta imagenes";
})

function showFiles(files)
{
    if(files.length ==undefined)
    {
        processFile(files);
    }
    else
    {
        for(const file of files)
        {
            processFile(file);
        }
    }
}

function processFile(file)
{
    const docType = file.type;
    const validExtensions = ['text/csv','text/txt', 'image/png', 'image/gif'];

    if(validExtensions.includes(docType))
    {
        //archivo valido
        const fileReader = new FileReader();
        const id = 'file-${Math.random().toString(32).substring(7)}';

        fileReader.addEventListener("load", (e) => 
        {
            const fileUrl = fileReader.result;
            const image = '<div id = "${id}" class = "file-container"><img src="${fileUrl}" alt="${file.name}" width = "50"><div class="status"><span>${file.name}</span><span class="status-text">Loading...</span></div></img></div>;'

            const html = document.querySelector("#preview").innerHTML;
            document.querySelector('#preview').innerHTML= image + html;
        });
        fileReader.readAsDataURL(file);
        uploadFile(file, id);
    }
    else
    {
        //no se vale
        alert("no es un archivo valido");
    }
}

async function uploadFile(file)
{
    const formData = new FormData();
    formData.append('file', file);

    try
    {
        const response = await fetch("http://127.0.0.1:5500/lectura2.html",{method: 'POST', body: formData,});
        
        const responseText = await response.text();
        console.log(responseText);
        
        document.querySelector('${id} .status-text').innerHTML = '<span class = "success">Archivo subido correctamente</span>';
    }
    catch(error)
    {
        document.querySelector('${id} .status-text').innerHTML = '<span class = "failure">el Archivo no se ha subido...</span>';
    }
}
