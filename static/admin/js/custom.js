// show file name
  $('.custom-file input').change(function (e) {
    var files = [];
    for (var i = 0; i < $(this)[0].files.length; i++) {
      files.push($(this)[0].files[i].name);
    }
    $(this).next('.custom-file-label').html(files.join(', '));
  });

  //loading
  document.getElementById("ConfirmBtn").onclick = loadingFunction;
  
  function loadingFunction()
  {
    document.getElementById("confirmBox").style.display = "none";
    document.getElementById("loadingGif").style.display = "block";
    
  }

    //loaded
    function loadedFunction() {
      document.getElementById("loadingGif").style.display = "none";
      document.getElementById("confirmBox").style.display = "block";
    }


