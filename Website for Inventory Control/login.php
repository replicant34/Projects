<?php
session_start(); // Start the session
if(isset($_SESSION['user'])) header('location: dushboard.php');

$error_message = '';

if ($_POST){

    include('database/connection.php');

    $username = $_POST['username'];
    $password = $_POST['password'];

    

    try {
        // Use prepared statements to prevent SQL injection
        $query = 'SELECT * FROM users WHERE users.email="'. $username .'" AND users.password="'. $password .'"';
        $stmt = $conn->prepare($query);
        $stmt->execute();

        

        if ($stmt->rowCount() > 0){ 
            // Successful login, set session variables and redirect
            $stmt->setFetchMode(PDO::FETCH_ASSOC);
            $user = $stmt->fetchAll()[0];
            $_SESSION['user'] = $user;
            header('Location: dushboard.php');
            
        } else {
            $error_message = 'Please make sure that your username and password are correct';
        }
    } catch (PDOException $e) {
        // Handle database errors
        $error_message = 'Database error: ' . $e->getMessage();
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Stock Control Login</title>
    <link rel="stylesheet" type="text/css" href="css/login.css">
</head>
<body id="loginBody">
    <?php 
        if(!empty($error_message)) { ?>
            <div id="errorMessage">
                <p>Error: <?= $error_message ?> </p>
            </div>
    <?php } ?>

    <div class="container">
        <div class="loginHeader">
            <h1>STOCK CONTROL</h1>
            <p>LLC "Random Company"</p>
        </div>

        <div class="loginBody">
            <form action="login.php" method="POST">
                <div class="loginInputContainer">
                    <label for="">Username</label>
                    <input placeholder="Username" name="username" type="text" />
                </div>
                <div class="loginInputContainer">
                    <label for="">Password</label>
                    <input placeholder="Password" name="password" type="password" />
                </div>
                <div class="loginButtonContainer">
                    <button>login</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
