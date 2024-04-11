<?php 

include('connection.php');

$stmt = $conn->prepare("SELECT * FROM users ORDER BY created DESC");
$stmt->execute();
$result = $stmt->setFetchMode(PDO::FETCH_ASSOC);


return $stmt->fetchAll();

?>