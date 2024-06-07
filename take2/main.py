from website import create_app

app = create_app()

# run the webserver only when this file is run directly
if __name__ == '__main__':
    app.run(debug = True)  #everytime a change is made in the py code, the server will automatically rerun



