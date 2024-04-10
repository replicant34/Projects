<?php 
    session_start();
    if(!isset($_SESSION['user'])) header('location: index.php');

    $user = $_SESSION['user'];
        
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

                </div>
            </div>
        </div>
    </div>
<script src="js/script.js"> </script>
</body>
</html>