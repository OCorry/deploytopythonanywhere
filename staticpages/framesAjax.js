// Ajax Functions
// These are imported to the frames.html page using <script src="framesAjax.js"></script>

    // Get All Frames
    function getAllAjax(){
        $.ajax({
            "url": "/frames",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                console.log("Showing all frames")
                console.log(result);
                for (frame of result){
                    addFrameToTable(frame);
                }            
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }

    // Create New Frame
    function createFrameAjax(frame){      
        console.log(JSON.stringify(frame));
        $.ajax({
            "url": "/frames",
            "method":"POST",
            "data":JSON.stringify(frame),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log("New frame created")
                console.log(result);
                frame.id = result.id
                addFrameToTable(frame)
                clearForm()
                showViewAll()
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }

    //Update an Exisitng Frame
    function updateFrameAjax(frame){    
        console.log(JSON.stringify(frame));
        $.ajax({
            "url": "/frames/"+encodeURI(frame.id),
            "method":"PUT",
            "data":JSON.stringify(frame),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
               console.log("Frame Updated")
               console.log(result);
                  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }


    //Delete a Frame
    function deleteFrameAjax(id){
        
        console.log(JSON.stringify('deleting '+id));
        $.ajax({
            "url": "/frames/"+encodeURI(id),
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