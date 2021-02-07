cred_prompt = """
<!DOCTYPE html>
<html>
    <head>
        <title>ESP8266 connection</title>
    </head>
    <body>
        <h2>
            Enter the UID and Password to connect to WiFi
        </h2>
        <form action="/post">
            uid: <input type="text" name="uid">
            password: <input type="text" name="password">
            <input type="submit" value="Submit">
        </form><br>
    </body>
</html>
"""

connection_response = """
<!DOCTYPE html>
<html>
    <head>
        <title>ESP8266 connection</title>
    </head>
    <body>
        <h2>
            Your ESP8266 IP address is {}
        </h2>
    </body>
</html>
"""