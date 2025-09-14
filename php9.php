<?php
// Step 1: Database connection
$servername = "localhost";
$username = "root";   // WAMP default username
$password = "";       // WAMP default password is empty
$dbname = "dbase";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Find Student Details</title>
</head>
<body>
    <h2>Search Student</h2>
    <!-- Step 2: Input form -->
    <form method="post" action="">
        Enter Student ID: <input type="number" name="id" required>
        <input type="submit" value="Search">
    </form>

<?php
// Step 3: When user submits the form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = $_POST['id'];

    // Step 4: Query the database
    $sql = "SELECT * FROM tb1 WHERE id = $id";
    $result = $conn->query($sql);


    // Step 5: Display result
    if ($result->num_rows > 0) {
        echo "<h3>Student Details</h3>";
        while ($row = $result->fetch_assoc()) {
            echo "Roll No: " . $row["id"] . "<br>";
            echo "Name: " . $row["name"] . "<br>";
        }
    } else {
        echo "<p style='color:red;'>No student found with ID: $id</p>";
    }
}
$conn->close();
?>
</body>
</html>