// Ajax Functions
// These are imported to the candles.html page using: <script src="candlesAjax.js"></script>
// Code sourced from Topic 6 Lectures and labs and Topic 10//
  
    // Get All Candles
    function getAllAjax(){
        $.ajax({
            "url": "/candles",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                console.log("Showing all candles")
                console.log(result);
                for (candle of result){
                    addCandleToTable(candle);
                }
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }

    // Create New Candle
    function createCandleAjax(candle){
        console.log(JSON.stringify(candle));
        $.ajax({
            "url": "/candles",
            "method":"POST",
            "data":JSON.stringify(candle),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log("New candle created")
                console.log(result);
                candle.id = result.id
                addCandleToTable(candle)
                clearForm()
                showViewAll()
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }

    //Update An Existing Candle
    function updateCandleAjax(candle){
        console.log(JSON.stringify(candle));
        $.ajax({
            "url": "/candles/"+encodeURI(candle.id),
            "method":"PUT",
            "data":JSON.stringify(candle),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
               console.log("Candle updated")
               console.log(result);                  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }

    //Delete A Candle
    function deleteCandleAjax(id){
        
        console.log(JSON.stringify('deleting '+id));
        $.ajax({
            "url": "/candles/"+encodeURI(id),
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    //Calling the getAll Ajax function so that the contents of the database are show on opening of the webpage
    getAllAjax();