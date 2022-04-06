
let root = document.getElementById('root');

fetch("../fonts/fluent-icons-for-web.json")
.then(response => {
   return response.json();
})
.then(data => {
    let html = ``;
    for(let val in data){
        html += `
            <div class="preview">
                <span class="inner">
                    <i class="fiw fiw-` + val + `"></i>
                </span>
                <br>
                <span class='label'>` + val + `</span>
            </div>
        `;
    }
    root.innerHTML = html
});