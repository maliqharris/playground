from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html", phrase="hello", times = 5)# Return the string 'Hello World!' as a response

# import statements, maybe some other routes
@app.route('/play')
def play(): 
    return render_template("index2.html")
@app.route('/play/<num>')
def playme(num): 
    actualnum = int(num)

    return render_template("index3.html", actualnum = actualnum)
@app.route('/play/<num>/<color>')
def playmecol(num,color): 
    actualnum = int(num)

    return render_template("index4.html", actualnum = actualnum, color = color)
@app.route('/dojo')
def dojo():
    return "Dojo!"   
@app.route('/success')
def success():
  return "success"
@app.route('/say/<wordname>')
def say(wordname):
    print(wordname)
    return "Hi "  + wordname + "!"
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name
@app.route('/repeat/<num>/<wordyo>')
def repeat(wordyo,num):
    print(wordyo)
    realnum = int(num)
    return wordyo * realnum

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

