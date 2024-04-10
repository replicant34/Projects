<?php 
    session_start();

    $table_name = $_SESSION['table'];

    $first_name = $_POST['first_name'];
    $last_name = $_POST['last_name'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $encrypted = password_hash($password, PASSWORD_DEFAULT);

    $command = "INSERT INTO $table_name (first_name, last_name, email, password) VALUES ('$first_name', '$last_name', '$email', '$encrypted')";

    include('connection.php');

    try {
        $response = [
            'success' => true,
            'message' => $first_name . ' ' . $last_name . ' ' . 'added successfully!'
        ];
        $conn->exec($command);
    } catch (PDOException $e) {
        $response = [
            'success' => false,
            'message' => $e->getMessage()
        ];
    }

    $_SESSION['response'] = $response;
    header('location: ../users-add.php');
?>

