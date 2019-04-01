<?php
$email = filter_input(INPUT_POST, 'email');
$password = filter_input(INPUT_POST, 'password');
if (!empty($email)){
    if (!empty($password)){
        $host = "ec2-23-23-92-204.compute-1.amazonaws.com";
        $dbuser = "gxupvblzzfulmn";
        $dbpassword = "6f218f9e00cb85e2d96043b8a25898951fd0fbd475a5bcbeb9eb2ba4cc42d072";
        $dbname = "d1fs1cm170ct9t";
        // Create connection
        $conn = new mysqli ($host, $dbuser, $dbpassword, $dbname);
        if (mysqli_connect_error()){
            die('Connect Error ('. mysqli_connect_errno() .') '. mysqli_connect_error());
        }
        else{
            $sql = "INSERT INTO members (email, password)
                values ('$email','$password')";
            if ($conn->query($sql)){
                echo "New record is inserted sucessfully";
            }
            else{
                echo "Error: ". $sql ."c". $conn->error;
            }
            $conn->close();
        }
    }
    else{
        echo "Password should not be empty";
        die();
    }
}
else{
    echo "Email should not be empty";
    die();
}
?>
