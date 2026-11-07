from app import create_app

app = create_app()

if __name__ == "__main__":
    # Only listen on this computer (127.0.0.1), not the whole network
    app.run(host="127.0.0.1", port=5000)
