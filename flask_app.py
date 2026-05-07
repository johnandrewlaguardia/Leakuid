from flaskr import create_app, db
import socket
import webbrowser

app = create_app()

if __name__ == "__main__":
    app.config["FLASKENV"] = "development"
    app.debug = True

    host_name = socket.gethostname()
    host = socket.gethostbyname(host_name)

    port = 900

    web_site = f"http://{host}:{port}"
    print("Host:", host_name)
    print("URL:", web_site)

    webbrowser.open(web_site)

    app.run(host="0.0.0.0", port=port)