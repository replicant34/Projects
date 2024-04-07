
        // JavaScript function to handle delete confirmation and refresh page
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