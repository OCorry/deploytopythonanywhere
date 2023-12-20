# Create a flask application server to implement RESTful API
# Carry out CRUD (Create, Read, Update & Delete) operations on the API
# Two APIS created - Candles & Frames
# Code Adapted from Topic 8 lectures and labs & Topic 10


# Import the DAOs from the DAO files
from candlesDAO import candlesDAO
from framesDAO import framesDAO

from flask import Flask, url_for, request, redirect, abort, jsonify
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Test the server works 
# @app.route('/')
# def index():
    #return "Hello World"

#Implement the requests:

                ################################################################
                                        #Candles#
                ################################################################   

# Get ALL request
# curl http://127.0.0.1:5000/candles
@app.route('/candles')
def getall():
    #print("in getall")
    results = candlesDAO.getAll()
    return jsonify(results)


# Find By Id
# curl http://127.0.0.1:5000/candles/1
@app.route('/candles/<int:id>')
def findById(id):
    findCandle= candlesDAO.findByID(id)
    return jsonify(findCandle)

    
# Create a new candle
# curl -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Orchard\", \"Colour\":\"Light Green\", \"Height\":16, \"Width\":10, \"Scent\":\"Apple\", \"Price\":13}" http://127.0.0.1:5000/candles
@app.route('/candles', methods=['POST'])
#Create the candle 
def create():

    if not request.json:
        abort(400)
    candle = {
        "Name": request.json["Name"],
        "Colour":request.json["Colour"],
        "Height": request.json["Height"],
        "Width": request.json["Width"],
        "Scent": request.json["Scent"],
        "Price": request.json["Price"],

    }
    values =(candle['Name'],candle['Colour'],candle['Height'],candle['Width'],candle['Scent'],candle['Price'])
    newId = candlesDAO.create(values)
    candle['id'] = newId
    return jsonify(candle)
    


# Update an existing candle
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"orange\",\"Colour\":\"Orange\"}" http://127.0.0.1:5000/candles/5
@app.route('/candles/<int:id>', methods=['PUT'])
def update(id):
    findCandle = candlesDAO.findByID(id)
    if not findCandle:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json

    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    
    if 'Height' in reqJson and type(reqJson['Height']) is not int:
        abort(400)

    if 'Width' in reqJson and type(reqJson['Width']) is not int:
        abort(400)

    if 'Name' in reqJson:
        findCandle['Name'] = reqJson['Name']
    if 'Colour' in reqJson:
        findCandle['Colour'] = reqJson['Colour']
    if 'Height' in reqJson:
        findCandle['Height'] = reqJson['Height']
    if 'Width' in reqJson:
        findCandle['Width'] = reqJson['Width']
    if 'Scent' in reqJson:
        findCandle['Scent'] = reqJson['Scent']
    if 'Price' in reqJson:
        findCandle['Price'] = reqJson['Price']

    values = (findCandle['Name'],findCandle['Colour'],findCandle['Height'],findCandle['Width'],findCandle['Scent'], findCandle['Price'],findCandle['id'])
    candlesDAO.update(values)
    return jsonify(findCandle)


# Delete a candle
# curl -X "DELETE" http://127.0.0.1:5000/candles/1
@app.route('/candles/<int:id>', methods =['DELETE'])
def delete(id):
    candlesDAO.delete(id)

    return jsonify({"done":True})




                ################################################################
                                        #FRAMES#
                ################################################################                        


# Get ALL request
# curl http://127.0.0.1:5000/frames
@app.route('/frames')
def getallFrames():
    #print("in getall")
    results = framesDAO.getAllFrames()
    return jsonify(results)


# Find By Id
# curl http://127.0.0.1:5000/frames/1
@app.route('/frames/<int:id>')
def findFrameById(id):
    findFrame= framesDAO.findFrameByID(id)
    return jsonify(findFrame)

    

# Create a new frame
# curl -i -H "Content-Type:application/json" -X POST -d "{\"Occasion\":\"Baby Girl\", \"Colour\":\"Pink\", \"Height\":16, \"Width\":10, \"Scent\":\"Apple\", \"Price\":13}" http://127.0.0.1:5000/frames
@app.route('/frames', methods=['POST'])
#Create the frame 
def createNewFrame():

    if not request.json:
        abort(400)
    newFrame ={
        "Occasion": request.json["Occasion"],
        "Colour":request.json["Colour"],
        "Height": request.json["Height"],
        "Width": request.json["Width"],
        "Price": request.json["Price"],

    }
    values =(newFrame['Occasion'],newFrame['Colour'],newFrame['Height'],newFrame['Width'],newFrame['Price'])
    newId = framesDAO.createNewFrame(values)
    newFrame['id'] = newId
    return jsonify(newFrame)
    


# Update an existing frame
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Occasion\":\"Easter\",\"Colour\":\"Yellow\"}" http://127.0.0.1:5000/frames/5
@app.route('/frames/<int:id>', methods=['PUT'])
def updateFrame(id):
    findFrame = framesDAO.findFrameByID(id)
    if not findFrame:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json

    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    
    if 'Height' in reqJson and type(reqJson['Height']) is not int:
        abort(400)

    if 'Width' in reqJson and type(reqJson['Width']) is not int:
        abort(400)

    if 'Occasion' in reqJson:
        findFrame['Occasion'] = reqJson['Occasion']
    if 'Colour' in reqJson:
        findFrame['Colour'] = reqJson['Colour']
    if 'Height' in reqJson:
        findFrame['Height'] = reqJson['Height']
    if 'Width' in reqJson:
        findFrame['Width'] = reqJson['Width']
    if 'Price' in reqJson:
        findFrame['Price'] = reqJson['Price']

    values = (findFrame['Occasion'],findFrame['Colour'],findFrame['Height'],findFrame['Width'], findFrame['Price'],findFrame['id'])
    framesDAO.updateFrame(values)
    return jsonify(findFrame)


# Delete a frame
# curl -X "DELETE" http://127.0.0.1:5000/frames/1
@app.route('/frames/<int:id>', methods =['DELETE'])
def deleteFrame(id):
    framesDAO.deleteFrame(id)

    return jsonify({"done":True})



# main function to execute all of the above 
if __name__ == "__main__":
    app.run(debug=True)