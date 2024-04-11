function script(){

    this.initialize = function(){
        this.registerEvents();
    }

    this.registerEvents = function(){
        document.addEventListener('click', function(e){
            targetElement = e.target;
            classList = targetElement.classList;

            if(classList.contains('deleteUser')){
                 e.preventDefault();
                 userId = targetElement.dataset.userid;
                 fname = targetElement.dataset.fname;
                 lname = targetElement.dataset.lname;
                 // console.log(userId, fname, lname);
                 fullName = fname + ' ' + lname;

                 if(window.confirm('Please confimn deletion of user '+ fullName +'?')){
                    $.ajax({
                        method: 'POST',
                        data: {
                            user_id: userId,
                        },
                        url: "database/delete-user.php",
                        dataType: 'json',
                        success: function(data){
                            if(data.success){
                                if(window.confirm(data.massege)){
                                    location.reload();
                                }
                            } else window.alert(data.message);
                        }
                    })
                 } else {
                    console.log('cancel deletion')
                 }
            }
        });
    }
}

var script = new script;
script.initialize();