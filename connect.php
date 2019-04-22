<?php
//$email = filter_input(INPUT_POST, 'email');
//$password = filter_input(INPUT_POST, 'password');
echo "please insert your email\n";
$email = rtrim(fgets(STDIN));
echo "please insert your password\n";
$password = rtrim(fgets(STDIN));

if (!empty($email)){
  if (!empty($password)){
    $host = "ec2-23-23-92-204.compute-1.amazonaws.com";
    $port = "5432";
    $dbuser = "gxupvblzzfulmn";
    $dbpassword = "6f218f9e00cb85e2d96043b8a25898951fd0fbd475a5bcbeb9eb2ba4cc42d072";
    $dbname = "d1fs1cm170ct9t";
    $mode = "require";
    // Create connection
    // $conn = mysqli_connect($host, $dbuser, $dbpassword, $dbname);
    $conn = pg_connect("host=$host port=$port dbname=$dbname user=$dbuser password=$dbpassword sslmode=$mode");
    // if (mysqli_connect_error()){
    if($conn == false){
      die('Connection Error');
      // die('Connect Error ('. /*mysqli_connect_errno()*/ .') '. /*mysqli_connect_error()*/);
    }
    else{
      $sql = "INSERT INTO members (email, password, firstname, lastname)
        values ('$email','$password', 'test', 'input')";
      if ($conn->pg_query($sql)){
        echo "New record is inserted sucessfully";
      }
      else{
        echo "Error: ". $sql ."c"; //$conn->error;
      }
      $conn->pg_close();
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
