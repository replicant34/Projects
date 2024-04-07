<?php
    $data = $_POST;
    $user_id = (int) $data['userId'];



    try {
        $command = "DELETE FROM users WHERE id=($user_id)";
        include('connection.php');

        $conn->exec($command);

        echo json_encode([
            'success' => true,
            'message' => 'User is deleted successfully!'
        ]);
    } catch (PDOException $e) {
        echo json_encode([
            'success' => false,
            'message' => 'Error!'
        ]);
    }
?>