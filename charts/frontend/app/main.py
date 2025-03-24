from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <body>
        <h1>Ecomarket Frontend</h1>
        <button onclick="document.getElementById('form').style.display='block'">Cadastro</button>
        <button onclick="listUsers()">Listar</button>
        <div id="form" style="display:none">
            <form id="cadastroForm" onsubmit="submitForm(event)">
                <label>Nome:</label><input type="text" name="nome"><br>
                <label>Email:</label><input type="text" name="email"><br>
                <input type="submit" value="Cadastrar">
            </form>
        </div>
        <div id="result"></div>
        <script>
            async function submitForm(event) {
                event.preventDefault();
                const form = document.getElementById('cadastroForm');
                const nome = form.nome.value;
                const email = form.email.value;
                const scoreResponse = await fetch('http://app.tunnelsw.com/score', {
                    headers: { 'Host': 'api2.tunnelsw.com' }
                });
                const scoreData = await scoreResponse.json();
                const score = scoreData.score;
                const response = await fetch('http://app.tunnelsw.com/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Host': 'api1.tunnelsw.com'
                    },
                    body: JSON.stringify({ nome, email, score })
                });
                const result = await response.json();
                document.getElementById('result').innerHTML = JSON.stringify(result);
            }
            async function listUsers() {
                const response = await fetch('http://app.tunnelsw.com/users', {
                    headers: { 'Host': 'api1.tunnelsw.com' }
                });
                const users = await response.json();
                document.getElementById('result').innerHTML = JSON.stringify(users);
            }
        </script>
    </body>
    </html>
    """
