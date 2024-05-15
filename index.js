const port = 9075;

const credentials = [];
const ranking = [];
const gamePending = [];
let gameOnGoing;

function verifyCredentials(username, pass) {
    const user = credentials.find(([user, password]) => user === username);
    if (user) {
        return user[1] === pass;
    }
    credentials.push([username, pass]);
    return true;
}

const http = require('http');
const server = http.createServer(async (request, response) => {
    const { method, url } = request;

    if (method === 'OPTIONS') {
        response.writeHead(204, {
            'Access-Control-Allow-Headers': 'content-type',
            'Access-Control-Max-Age': '86400',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Origin': '*',
            'Connection': 'Keep-Alive',
            'Keep-Alive': 'timeout=2, max=100',
            'Vary': 'Accept-Encoding, Origin'
        });
        response.end();
        return;
    }

    if (method === 'POST') {
        let body = [];
        for await (const chunk of request) {
            body.push(chunk);
        }
        body = JSON.parse(Buffer.concat(body).toString());

        if (url === '/ranking') {
            response.writeHead(200, {
                'Access-Control-Allow-Origin': '*',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Keep-Alive': 'timeout=5',
                'Transfer-Encoding': 'chunked'
            });
            const responseBody = { ranking: ranking.slice(0, 10) };
            response.write(JSON.stringify(responseBody));
            response.end();
            return;
        }

        if (url === '/register') {
            const isValid = verifyCredentials(body.nick, body.password);
            const responseNum = isValid ? 200 : 400;
            const responseBody = isValid
                ? { success: "Successful registration" }
                : { error: "User registered with a different password" };

            response.writeHead(responseNum, {
                'Access-Control-Allow-Origin': '*',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Keep-Alive': 'timeout=5',
                'Transfer-Encoding': 'chunked'
            });
            response.write(JSON.stringify(responseBody));
            response.end();
            return;
        }
    }
});

server.listen(port, (error) => {
    if (error) {
        console.log("Something went wrong");
    } else {
        console.log("Listening on port " + port);
    }
});
