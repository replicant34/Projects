<?php
$data = $_POST;
$user_id = (int) $data['userId'];
$first_name = $data['firstName'];
$last_name = $data['lastName'];
$email = $data['email'];

try {
    include('connection.php');

    $stmt = $conn->prepare("UPDATE users SET first_name = ?, last_name = ?, email = ? WHERE id = ?");
    $stmt->execute([$first_name, $last_name, $email, $user_id]);

    echo json_encode([
        'success' => true,
        'message' => 'User updated successfully!'
    ]);
} catch (PDOException $e) {
    echo json_encode([
        'success' => false,
        'message' => 'Error updating user!'
    ]);
}
?>
