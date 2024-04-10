<?php 
    session_start();
    if(!isset($_SESSION['user'])) header('location: index.php');
    $_SESSION['table'] = 'users';
    $user = $_SESSION['user'];
    $users = include('database/show-users.php');
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard-Stock Control</title>
    <link rel="stylesheet" type="text/css" href="css/login.css">
    <script src="https://kit.fontawesome.com/efd90a8dca.js" crossorigin="anonymous"></script>
</head>
<body>
    <div id="dashboardMainContainer">
        <?php include('partials/add-sidebar.php') ?>
        <div class="dashboard_content_container" id="dashboard_content_container">
            <?php include('partials/app-topNav.php') ?>
            <div class="dashboard_content"> 
                <div class="dashboard_content_main"> 
                    <div class="row">
                        <div class="column column-12">
                             <h1 class="section_header"><i class="fa fa-plus"></i>Add User</h1>
                             <div id="userAddFormContainer">
                                 <form action="database/add.php" method="POST" class="appForm" id="userAddForm">
                                    <div class="appFormInputContainer">
                                        <label for="first_name">First Name</label>
                                        <input type="text" class="appFormInput" id="first_name" name="first_name" />
                                    </div>
                                    <div class="appFormInputContainer">
                                        <label for="last_name">Last Name</label>
                                        <input type="text" class="appFormInput" id="last_name" name="last_name" />
                                    </div>
                                    <div class="appFormInputContainer">
                                        <label for="email">Email</label>
                                        <input type="text" class="appFormInput" id="email" name="email" />
                                    </div>
                                    <div class="appFormInputContainer">
                                        <label for="password">Password</label>
                                        <input type="password" class="appFormInput" id="password" name="password" />
                                    </div>
                                    <button type="submit" class="appBtn"><i class="fa fa-user-plus"></i> Add user </button>
                                </form>    
                                <?php 
                                    if(isset($_SESSION['response'])) { 
                                        $response_message = $_SESSION['response']['message'];
                                        $is_success = $_SESSION['response']['success']
                                ?>
                                    <div class="responseMessage">
                                        <p class="<?= $is_success ? 'respondMessage_success' : 'respondMessage_error' ?>" >
                                            <?= $response_message ?>
                                        </p>
                                    </div>
                                <?php unset($_SESSION['response']); } ?>
                            </div>
                        </div>
                    </div>  
                </div>
            </div>
        </div>
    </div>

   <script src="js/script.js"> </script>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    <script>
        $(document).ready(function() {
            $(".deleteUser").on("click", function(e) {
                e.preventDefault();
                var userId = $(this).data("userid");
                var fName = $(this).data("fname");
                var lName = $(this).data("lname");

                // Display confirmation popup
                var isConfirmed = confirm("Are you sure you want to delete " + fName + " " + lName + "?");

                if (isConfirmed) {
                    // Make an AJAX request to delete the user
                    $.ajax({
                        url: "database/delete-user.php",
                        type: "POST",
                        data: { userId: userId },
                        success: function(response) {
                            // Refresh the page on successful deletion
                            location.reload();
                        },
                        error: function(error) {
                            console.error("Error deleting user:", error);
                        }
                    });
                }
            });
        });

        var editPopup = document.getElementById("editUserPopup");

        function openEditPopup(userId, firstName, lastName, email) {
            console.log("Edit button clicked"); // Check if this log appears in the console
            document.getElementById("edit_first_name").value = firstName;
            document.getElementById("edit_last_name").value = lastName;
            document.getElementById("edit_email").value = email;

            // You can also store the user ID in a hidden input field for later use
            document.getElementById("editUserId").value = userId;

            editPopup.style.display = "block";
        }

        function closeEditPopup() {
            editPopup.style.display = "none";
        }

        function submitEditForm() {
            // Retrieve data from the form
            var userId = document.getElementById("editUserId").value;
            var firstName = document.getElementById("edit_first_name").value;
            var lastName = document.getElementById("edit_last_name").value;
            var email = document.getElementById("edit_email").value;

            // Make an AJAX request to update user data
            $.ajax({
                url: "database/edit_user.php",
                type: "POST",
                data: { userId: userId, firstName: firstName, lastName: lastName, email: email },
                success: function(response) {
                    // Close the edit popup and refresh the page on successful update
                    closeEditPopup();
                    location.reload();
                },
                error: function(error) {
                    console.error("Error updating user:", error);
                }
            });
        }
    </script>
</body>
</html>

