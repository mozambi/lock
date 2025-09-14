

<?php
// Database connection
$servername = "localhost";
$username   = "root";   // default for WAMP
$password   = "";       // default = empty
$dbname     = "dbase"; // change this to your database name

// Create connection using mysqli
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// ---------------------
// Example SQL Queries
// ---------------------

// 1. Display all employees
//$sql = "SELECT * FROM tb1";

// 2. Insert a new employee
//$sql = "INSERT INTO tb1 VALUES (7, 'bumble',22)";

// 3. Select only name and position where salary > 50000
// $sql = "SELECT name, age FROM tb1 WHERE age > 20";

// 4. Update salary for an employee named 'Saranya'
// $sql = "UPDATE tb1 SET age = 15 WHERE name = 'kabila'";

// 5. Order employees by name (Ascending)
//$sql = "SELECT * FROM tb1 ORDER BY name ASC";

// 6. Order employees by salary (Descending)
$sql = "SELECT * FROM tb1 ORDER BY age DESC";

// 7. Delete one employee by ID
//$sql = "DELETE FROM tb1 WHERE id = 3";

// 8. Count total employees
 //$sql = "SELECT COUNT(*) AS total FROM tb1";

// ---------------------

// Run the query
$result = $conn->query($sql);

// Display results if it's a SELECT
if ($result && $result instanceof mysqli_result) {
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "<pre>";
            print_r($row);
            echo "</pre>";
        }
    } else {
        echo "No records found.";
    }
} else {
    if ($result === TRUE) {
        echo "Query executed successfully!";
    } else {
        echo "Error: " . $conn->error;
    }
}

// Close connection
$conn->close();
?>
